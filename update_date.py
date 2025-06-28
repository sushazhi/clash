import re
from datetime import datetime
import os

# 获取当天日期（两种格式）
today_slash = datetime.now().strftime("%Y/%m/%d")  # 2025/06/28
today_noslash = datetime.now().strftime("%Y%m%d")  # 20250628

# 读取clash.yaml文件
file_path = 'clash.yaml'
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# 精确匹配并替换（关键修复）
# 1. 先替换8位数字日期（YYYYMMDD）
content = re.sub(r'\b\d{8}\b', today_noslash, content)
# 2. 再替换带斜杠日期（YYYY/MM/DD）
content = re.sub(r'\b\d{4}/\d{2}/\d{2}\b', today_slash, content)

# 写回文件
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(content)

print(f"日期已更新: {today_slash} 和 {today_noslash}")
