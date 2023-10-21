import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, unquote
import time
import logging

# 设置日志
logging.basicConfig(
    filename='/home/liuxl/raider_data/logfile.log', 
    level=logging.INFO,
    format='%(asctime)s %(message)s',  # Include timestamp
    datefmt='%m/%d/%Y %I:%M:%S %p'  # Timestamp format
)

def get_character_info(element, character_class, spec):
    name = element.text
    link = element.get('href')

    path_segments = urlparse(link).path.split('/')
    region, realm = "", ""
    if len(path_segments) >= 4:
        region = path_segments[2]
        realm = unquote(path_segments[3])
    
    return {'name': name, 'region': region, 'realm': realm, 'class': character_class, 'spec': spec}

def fetch_and_parse(url, class_color):
    session = requests.Session()
    try:
        response = session.get(url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        return [element for element in soup.find_all(class_=class_color)[2:7]]
    except Exception as e:
        logging.error(f"Failed to fetch and parse URL: {url}. Error: {e}")
        return []

# 参数
season = "season-df-2"
character_classes = {
    "death-knight": ["blood", "frost", "unholy"],
    "demon-hunter": ["havoc", "vengeance"],
    "druid": ["balance", "feral", "guardian", "restoration"],
    "evoker": ["devastation", "preservation", "augmentation"],
    "hunter": ["beast-mastery", "marksmanship", "survival"],
    "mage": ["arcane", "fire", "frost"],
    "monk": ["brewmaster", "windwalker", "mistweaver"],
    "paladin": ["holy", "protection", "retribution"],
    "priest": ["discipline", "holy", "shadow"],
    "rogue": ["assassination", "outlaw", "subtlety"],
    "shaman": ["elemental", "enhancement", "restoration"],
    "warlock": ["affliction", "demonology", "destruction"],
    "warrior": ["arms", "fury", "protection"]
    }  
class_colors = {
    "death-knight": "class-color--6",
    "demon-hunter": "class-color--12",
    "druid": "class-color--11",
    "evoker": "class-color--13",
    "hunter": "class-color--3",
    "mage": "class-color--8",
    "monk": "class-color--10",
    "paladin": "class-color--2",
    "priest": "class-color--5",
    "rogue": "class-color--4",
    "shaman": "class-color--7",
    "warlock": "class-color--9",
    "warrior": "class-color--1"
    }  

# 将结果存储在这个列表中
all_character_info = []

for character_class, specs in character_classes.items():
    for spec in specs:
        # 构造网址
        url = f'https://raider.io/mythic-plus-spec-rankings/{season}/world/{character_class}/{spec}'
        elements = fetch_and_parse(url, class_colors[character_class])
        character_info_list = [get_character_info(element, character_class, spec) for element in elements]
        all_character_info.extend(character_info_list)
        logging.info(f"Successfully fetched data for {character_class} {spec}")

        # 暂停1秒
        time.sleep(1)

# 将结果写入JSON文件
try:
    with open('/home/liuxl/raider_data/player_info.json', 'w', encoding='utf-8') as f:
        json.dump(all_character_info, f, indent=4, ensure_ascii=False)
except Exception as e:
    logging.error(f"Failed to write data to JSON file. Error: {e}")