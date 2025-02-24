import pandas as pd

# 读取 Excel 文件，并将住院号和门诊号列的数据类型设置为字符串
excel_file = "220_192.xls"  # 替换为你的 Excel 文件路径
df = pd.read_excel(excel_file, dtype={'住院号': str, '门诊号': str})

# 替换列名为期望的格式
df.columns = ["姓名", "住院号", "门诊号"]

# 创建病人姓名和病人号字段
df["病人姓名"] = df["姓名"]
# 将住院号和门诊号转换为字符串，并去掉可能的 ".0"
df["住院号"] = df["住院号"].str.replace('\.0$', '', regex=True)
df["门诊号"] = df["门诊号"].str.replace('\.0$', '', regex=True)
df["病人号"] = df.apply(
    lambda row: row["住院号"].strip() if pd.notnull(row["住院号"]) and row["住院号"].strip() != '' 
    else (row["门诊号"].strip() if pd.notnull(row["门诊号"]) and row["门诊号"].strip() != '' else None),
    axis=1
)

# 移除原始的姓名、住院号、门诊号列（如果不需要保留）
df = df[["病人姓名", "病人号"]]

# 移除重复值和空值
df = df.drop_duplicates(subset=["病人姓名", "病人号"])
df = df.dropna()  # 移除包含空值的行

# 转换为 JSON 格式
json_data = df.to_json(orient="records", indent=4, force_ascii=False)

# 保存为 JSON 文件
with open("220_192.json", "w", encoding="utf-8") as json_file:
    json_file.write(json_data)

print("JSON 文件生成完成！")