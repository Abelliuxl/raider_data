# ✨ WoW Raider.io 数据采集工具

![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

这是一个功能强大的 Python 工具，旨在从 Raider.io 网站高效采集《魔兽世界》游戏角色的数据。它专注于获取各个职业和专精的**顶级玩家**信息，支持多种灵活的数据导出格式，并提供基础的数据分析功能，助您深入了解游戏数据。

---

## 🚀 功能特点

-   **全职业专精支持**: 能够采集所有魔兽世界职业和专精的玩家数据。
-   **智能数据采集**:
    -   自动重试机制和指数退避策略，确保数据采集的稳定性和可靠性。
    -   完善的错误处理，应对网络波动和API异常。
-   **灵活数据导出**: 支持将采集到的数据导出为多种常用格式：
    -   `JSON` (默认)
    -   `CSV`
    -   `Excel` (`.xlsx`)
-   **基础数据分析**: 提供对采集数据的基本统计分析功能，帮助您快速洞察数据概况。
-   **全面日志记录**: 详细的日志系统，包括主日志文件 (`logfile.log`) 和独立的错误日志文件 (`logfile_error.log`)，方便问题追踪和调试。
-   **代理支持**: 内置代理设置，优化海外网站访问速度和稳定性。

---

## 🛠️ 安装指南

1.  **克隆仓库**:
    ```bash
    git clone https://github.com/Abelliuxl/raider_data.git
    cd raider_data
    ```

2.  **安装依赖**:
    ```bash
    pip install -r requirements.txt
    ```

---

## ⚙️ 配置说明

### 📅 赛季配置

赛季配置通过项目根目录下的 `season_config.json` 文件进行管理。

```json
{
  "season": "season-tww-2"
}
```

**如何切换赛季？**
1.  打开 `season_config.json` 文件。
2.  修改 `"season"` 字段的值为当前所需的赛季标识（例如：`"season-tww-2"`）。
3.  保存文件。无需修改代码，工具将自动读取最新配置。

### 🌐 其他配置项

更多高级配置项位于 `config.py` 文件中，您可以根据需求进行调整：

-   **请求参数**: 请求延迟 (`REQUEST_DELAY`)、最大重试次数 (`MAX_RETRIES`)、请求超时 (`TIMEOUT`)。
-   **文件路径**: 日志文件 (`LOG_FILE`, `ERROR_LOG_FILE`) 和玩家信息存储文件 (`PLAYER_INFO_FILE`) 的路径。
-   **API URL模板**: Raider.io API 的访问地址模板。
-   **职业和专精**: 支持采集的魔兽世界职业及其专精列表。

### 🔒 代理配置

如果您的网络环境需要通过代理访问 Raider.io，可以在 `config.py` 中修改代理设置。默认配置为：

```python
PROXY = {
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890'
}
```

请根据您的实际代理地址和端口进行修改。

---

## 🚀 使用方法

运行主脚本 `raider_data.py` 即可开始数据采集。

**基本使用**:
```bash
python raider_data.py
```

**指定赛季**:
使用 `--season` 参数指定要采集数据的赛季。
```bash
python raider_data.py --season season-tww-2
```

**导出为CSV格式**:
使用 `--format` 参数指定输出数据格式。支持 `json` (默认), `csv`, `excel`。
```bash
python raider_data.py --format csv
```

**包含数据分析**:
使用 `--analyze` 标志在数据采集完成后执行并打印基本数据分析结果。
```bash
python raider_data.py --analyze
```

---

## 📊 数据格式

采集到的每条玩家数据记录包含以下字段：

-   `name`: 角色名称
-   `region`: 服务器区域 (例如：`us`, `eu`, `kr`)
-   `realm`: 服务器名称 (例如：`stormrage`, `draenor`)
-   `class`: 职业 (例如：`death-knight`, `mage`)
-   `spec`: 专精 (例如：`blood`, `fire`)
-   `last_updated`: 数据更新时间 (ISO 8601 格式)

---

## 📝 日志系统

本工具采用详细的日志记录系统，方便用户追踪程序运行状态和排查问题：

-   **主日志文件**: `logfile.log` - 记录所有信息级别及以上的日志，包括程序进度、采集详情等。
-   **错误日志文件**: `logfile_error.log` - 专门记录所有错误级别的日志，便于快速定位异常。
-   所有日志均包含时间戳、日志级别和详细信息。

---

## 📦 依赖

本工具依赖以下 Python 库：

-   `requests`: 用于发送HTTP请求。
-   `beautifulsoup4`: 用于解析HTML内容。
-   `pandas`: 用于数据处理和导出（CSV/Excel）。
-   `openpyxl`: (可选) 用于支持 Excel (`.xlsx`) 格式的数据导出。

---

## 🤝 贡献

欢迎对本项目进行贡献！如果您有任何改进建议、新功能想法或发现Bug，请随时提交Issue或Pull Request。

---

## 📄 许可

本项目采用 MIT License 开源。详情请参阅 `LICENSE` 文件。

---

**注意**: 本工具仅用于学习和研究目的，请遵守 Raider.io 的使用条款。
