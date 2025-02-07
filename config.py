import os

# 基础配置
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SEASON = "season-tww-1"
REQUEST_DELAY = 1  # 请求延迟时间（秒）
MAX_RETRIES = 3    # 最大重试次数
TIMEOUT = 10       # 请求超时时间（秒）

# 代理配置
PROXY = {
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890'
}

# 文件路径
LOG_FILE = os.path.join(BASE_DIR, 'logfile.log')
ERROR_LOG_FILE = os.path.join(BASE_DIR, 'logfile_error.log')
PLAYER_INFO_FILE = os.path.join(BASE_DIR, 'player_info.json')

# 请求头
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
}

# API URL模板
API_URL_TEMPLATE = 'https://raider.io/mythic-plus-spec-rankings/{season}/world/{class_name}/{spec}'

# 职业和专精配置
CHARACTER_CLASSES = {
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

CLASS_COLORS = {
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