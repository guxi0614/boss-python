import pandas as pd

# 读取CSV文件
df = pd.read_csv('data.csv')

# 将DataFrame保存为Excel文件
df.to_excel('example.xlsx', index=False)
