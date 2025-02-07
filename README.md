# WoW Raider.io 数据采集工具

这是一个用于从 Raider.io 网站采集魔兽世界游戏角色数据的 Python 工具。该工具可以获取各个职业和专精的顶级玩家信息，支持多种数据导出格式，并提供基本的数据分析功能。

## 功能特点

- 支持所有魔兽世界职业和专精的数据采集
- 自动重试机制和错误处理
- 支持多种数据导出格式（JSON、CSV、Excel）
- 提供基本的数据分析功能
- 完整的日志记录系统
- 支持代理设置，优化海外网站访问

## 安装

1. 克隆仓库：
```bash
git clone [repository-url]
cd [repository-name]
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

## 配置

所有配置项都在 `config.py` 文件中，包括：
- 赛季设置
- 请求延迟和重试次数
- 文件路径
- API URL模板
- 职业和专精配置
- 代理设置（默认使用 127.0.0.1:7890）

### 代理配置

如果需要通过代理访问 Raider.io，可以在 `config.py` 中修改代理设置：

```python
PROXY = {
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890'
}
```

可以根据实际情况修改代理地址和端口。

## 使用方法

基本使用：
```bash
python raider_data.py
```

指定赛季：
```bash
python raider_data.py --season season-tww-2
```

导出为CSV格式：
```bash
python raider_data.py --format csv
```

包含数据分析：
```bash
python raider_data.py --analyze
```

## 数据格式

采集的数据包含以下字段：
- name: 角色名称
- region: 服务器区域
- realm: 服务器名称
- class: 职业
- spec: 专精
- last_updated: 数据更新时间

## 日志系统

- 主日志文件：`logfile.log`
- 错误日志文件：`logfile_error.log`
- 包含时间戳、日志级别和详细信息

## 依赖

- requests
- beautifulsoup4
- pandas
- openpyxl (用于Excel支持)

## 许可

MIT License