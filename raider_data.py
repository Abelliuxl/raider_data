import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, unquote_plus
import time
import logging
import os
import argparse
from datetime import datetime
from typing import List, Dict, Optional
import pandas as pd
from config import *

class RaiderDataCollector:
    def __init__(self, season: str = SEASON):
        self.season = season
        self.session = requests.Session()
        self.session.headers.update(HEADERS)
        self.session.proxies.update(PROXY)  # 添加代理配置
        self.setup_logging()
        self.existing_data = self.load_existing_data()
        self.log_season_info()
        logging.info("Session initialized with proxy settings")

    def log_season_info(self):
        """记录当前赛季信息"""
        logging.info(f"当前赛季: {self.season}")

    def setup_logging(self):
        """设置日志系统"""
        # 创建格式化器
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        # 设置主日志处理器
        file_handler = logging.FileHandler(LOG_FILE)
        file_handler.setFormatter(formatter)
        
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        # 设置错误日志处理器
        error_handler = logging.FileHandler(ERROR_LOG_FILE)
        error_handler.setLevel(logging.ERROR)
        error_handler.setFormatter(formatter)  # 为错误日志添加相同的格式化器

        # 配置根日志记录器
        logging.basicConfig(
            level=logging.INFO,
            handlers=[file_handler, console_handler, error_handler]
        )

    def load_existing_data(self) -> List[Dict]:
        """加载现有数据，用于增量更新"""
        try:
            if os.path.exists(PLAYER_INFO_FILE):
                with open(PLAYER_INFO_FILE, 'r', encoding='utf-8') as f:
                    return json.load(f)
            return []
        except Exception as e:
            logging.error(f"Failed to load existing data: {e}")
            return []

    def get_character_info(self, element, character_class: str, spec: str) -> Dict:
        """解析角色信息"""
        try:
            name = element.text.strip()
            link = element.get('href', '')
            
            # 解析URL路径
            parsed_url = urlparse(link)
            path_parts = [p for p in parsed_url.path.split('/') if p]
            
            region = path_parts[1] if len(path_parts) > 1 else ""
            realm = unquote_plus(path_parts[2]) if len(path_parts) > 2 else ""
            
            return {
                'name': name,
                'region': region,
                'realm': realm,
                'class': character_class,
                'spec': spec,
                'last_updated': datetime.now().isoformat()
            }
        except Exception as e:
            logging.error(f"Error parsing character info for {element.text if element else 'Unknown'}: {str(e)}")
            return None

    def fetch_and_parse(self, url: str, class_color: str) -> List:
        """获取和解析网页数据，带重试机制"""
        for attempt in range(MAX_RETRIES):
            try:
                response = self.session.get(url, timeout=TIMEOUT)
                response.raise_for_status()  # 检查HTTP错误
                response.encoding = 'utf-8'
                soup = BeautifulSoup(response.text, 'html.parser')
                elements = soup.find_all(class_=class_color)
                if len(elements) >= 7:
                    return elements[2:7]  # 返回前5个角色
                else:
                    logging.warning(f"Found fewer than expected elements for URL {url}")
                    return elements[2:] if len(elements) > 2 else []
            except requests.RequestException as e:
                logging.error(f"Attempt {attempt + 1}/{MAX_RETRIES} failed for URL {url}: {e}")
                if attempt < MAX_RETRIES - 1:
                    time.sleep(REQUEST_DELAY * (attempt + 1))  # 指数退避
                    continue
                return []
            except Exception as e:
                logging.error(f"Unexpected error for URL {url}: {e}")
                return []

    def collect_data(self) -> List[Dict]:
        """收集所有角色数据"""
        all_character_info = []
        total_specs = sum(len(specs) for specs in CHARACTER_CLASSES.values())
        processed_specs = 0

        for character_class, specs in CHARACTER_CLASSES.items():
            for spec in specs:
                processed_specs += 1
                url = API_URL_TEMPLATE.format(
                    season=self.season,
                    class_name=character_class,
                    spec=spec
                )
                
                logging.info(f"Processing {character_class}-{spec} ({processed_specs}/{total_specs})")
                elements = self.fetch_and_parse(url, CLASS_COLORS[character_class])
                
                for element in elements:
                    char_info = self.get_character_info(element, character_class, spec)
                    if char_info:
                        all_character_info.append(char_info)
                
                time.sleep(REQUEST_DELAY)

        return all_character_info

    def save_data(self, data: List[Dict], format: str = 'json'):
        """保存数据到文件"""
        try:
            if format == 'json':
                with open(PLAYER_INFO_FILE, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=4, ensure_ascii=False)
            elif format == 'csv':
                df = pd.DataFrame(data)
                df.to_csv(PLAYER_INFO_FILE.replace('.json', '.csv'), index=False)
            elif format == 'excel':
                df = pd.DataFrame(data)
                df.to_excel(PLAYER_INFO_FILE.replace('.json', '.xlsx'), index=False)
            
            logging.info(f"Successfully saved {len(data)} records to {format} format")
        except Exception as e:
            logging.error(f"Failed to save data: {e}")

    def analyze_data(self, data: List[Dict]):
        """简单的数据分析"""
        df = pd.DataFrame(data)
        analysis = {
            'total_characters': len(df),
            'characters_by_class': df['class'].value_counts().to_dict(),
            'characters_by_region': df['region'].value_counts().to_dict(),
            'characters_by_spec': df.groupby(['class', 'spec']).size().to_dict()
        }
        return analysis

def main():
    parser = argparse.ArgumentParser(description='Collect WoW character data from Raider.io')
    parser.add_argument('--season', default=SEASON, help='Season to collect data for')
    parser.add_argument('--format', choices=['json', 'csv', 'excel'], default='json',
                      help='Output format')
    parser.add_argument('--analyze', action='store_true',
                      help='Perform data analysis after collection')
    args = parser.parse_args()

    collector = RaiderDataCollector(season=args.season)
    data = collector.collect_data()
    collector.save_data(data, format=args.format)

    if args.analyze:
        analysis = collector.analyze_data(data)
        logging.info("Data Analysis Results:")
        logging.info(json.dumps(analysis, indent=2))

if __name__ == "__main__":
    main()
