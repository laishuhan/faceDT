import csv

# 从a.txt文件中提取所有数字
numbers = []
try:
    with open('D:\\projects\\dachuang\\code\\lab\\data.txt', 'r') as file:
        for line in file:
            numbers.extend(line.strip().split())
            # 或者使用以下代码过滤非数字内容：
            # numbers.extend([x for x in line.strip().split() if x.isdigit()])
except FileNotFoundError:
    print("文件不存在或无法打开。")


# 指定要插入的行数
insert_row = 4

# 读取现有的CSV文件内容
existing_data = []
try:
    with open('D:\\projects\\dachuang\\code\\lab\\data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            existing_data.append(row)
except FileNotFoundError:
    pass  # 如果文件不存在，那么继续就好

# 将新的行插入到现有数据中的指定位置
existing_data.insert(insert_row - 1, numbers)

# 重新写入b.csv文件
try:
    with open('D:\\projects\\dachuang\\code\\lab\\data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in existing_data:
            writer.writerow(row)
except IOError:
    print("写入文件时出错。")
