import numpy as np
import csv

# 生成前90个向量
data_90 = np.random.uniform(low=-5, high=5, size=(900, 1280))
zeros = np.zeros((900, 1))
data_90 = np.hstack((data_90, zeros))

# 生成后10个向量
data_10 = np.random.uniform(low=-5, high=5, size=(100, 1280))
ones = np.ones((100, 1))
data_10 = np.hstack((data_10, ones))

# 合并成一个数组
data = np.vstack((data_90, data_10))

# 写入CSV文件
with open('D:\\projects\\dachuang\\code\\lab\\data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for row in data:
        writer.writerow(row)
