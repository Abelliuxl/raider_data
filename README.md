# 魔兽世界 Raider.io 多专精排名角色信息抓取
# World of Warcraft Raider.io Multi-Spec Ranking Character Info Scraping

这是一个Python脚本，用于从 [魔兽世界 Mythic+ 和 Raid 进度排名](https://raider.io/mythic-plus-spec-rankings/) 网站按照排名抓取并保存角色信息。获取之后可以用于通过 raider.io 的官方 API 获取天赋字符串等信息。
This is a Python script for scraping and saving character information from the [World of Warcraft Rankings for Mythic+ and Raid Progress](https://raider.io/mythic-plus-spec-rankings/) website according to the rankings. The obtained information can be used to get talent strings etc. through the official API of raider.io.

## 功能 Features

该脚本会遍历所有的职业和专精，从指定的赛季排名页面中获取前5名角色的名字、区域、服务器、职业和专精。这些数据被保存在一个JSON文件中。
This script will traverse all professions and specializations, get the names, regions, servers, professions, and specializations of the top 5 characters from the specified season ranking page. These data are saved in a JSON file.

## 使用方法 Usage

1. 安装所需的Python库，如：
    Install the required Python libraries, such as:

    ```bash
    pip install requests beautifulsoup4
    # Others omitted
    ```

2. 运行Python脚本：
    Run the Python script:

    ```bash
    python raider_data.py
    ```

## 结果 Results

所有角色的信息将被保存在一个名为 `/home/liuxl/raider_data/player_info.json` 的文件中（具体路径自己修改），格式如下：
All character information will be saved in a file named `/home/liuxl/raider_data/player_info.json` (modify the specific path yourself), the format is as follows:

```json
[
    {
        "name": "CharacterName",
        "region": "Region",
        "realm": "Realm",
        "class": "Class",
        "spec": "Spec"
    },
    ...
]
```

所有的日志信息（包括错误和更新记录）都会被写入到一个名为 `/home/liuxl/raider_data/logfile.log` 的文件中。（具体路径自己修改）
All log information (including errors and update records) will be written to a file named `/home/liuxl/raider_data/logfile.log`. (modify the specific path yourself)

## 注意 Note

该脚本是在Python 3环境下编写的，并需要安装 `requests` 和 `beautifulsoup4` 这两个库。在运行脚本前，请确保你已经正确安装了这些库。该脚本会在每次抓取数据后暂停1秒，以防止过于频繁的请求对服务器产生负担。
The script is written in a Python 3 environment and requires the installation of the `requests` and `beautifulsoup4` libraries. Before running the script, please make sure that you have correctly installed these libraries. The script will pause for 1 second after each data crawl to prevent too frequent requests from burdening the server.