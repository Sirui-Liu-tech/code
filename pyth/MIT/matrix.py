import pandas as pd

# 读取包含所需列的Excel文件
excel_file_path = 'your_excel_file.xlsx'  # 替换成你的Excel文件路径
df = pd.read_excel(excel_file_path)

# 获取选手的名称，假设为 '选手A'
player_name = 'Alejandro Davidovich Fokina'

# 获取发球的数据
serve_column_name = 'server'  # 替换成实际的发球列名称
serve_data = df[serve_column_name]

