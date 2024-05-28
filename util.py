# -*- coding: utf-8 -*-

# 导入必要的库
import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

#加载数据
def data_load():
    data = pd.read_csv('D:\\projects\\dachuang\\code\\lab\\data.csv')
    #data = pd.read_excel('data/data.xlsx')
    data=data.fillna(0) #缺失值处理
    # print(data.max())
    data = data.sample(frac=1, random_state=42)  # frac=1 表示打乱全部数据
    data = data.values #转化为numpy
    row = data.shape[0]
    # 训练集与测试集划分
    num_train = int(row * 0.9)  # 训练集数量
    # num_train = 100
    x_train = data[:num_train, :-1]
    y_train = data[:num_train, -1]
    x_test = data[num_train:, :-1]
    y_test = data[num_train:, -1]
    # 归一化
    ss_X = StandardScaler().fit(x_train)
    x_train = ss_X.transform(x_train)
    x_test = ss_X.transform(x_test)

    return x_train,y_train,x_test,y_test


import seaborn as sns
from sklearn.metrics import confusion_matrix
#绘制损失曲线
def plot_confusion(labels,predicted):
    # 绘图属性
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体
    # 真实标签和预测标签计算混淆矩阵
    cm = confusion_matrix(labels, predicted)
    # 设置类别标签
    class_names = ['0', '1']
    # 创建图表
    fig, ax = plt.subplots()
    # 绘制混淆矩阵的热力图
    sns.heatmap(cm, annot=True, cmap='Blues', fmt='d', xticklabels=class_names, yticklabels=class_names, ax=ax)
    # 添加坐标轴标签
    ax.set_xlabel('预测标签')
    ax.set_ylabel('真实标签')
    # 设置图表标题
    ax.set_title('分类预测结果混淆矩阵')
    # 自动调整布局
    plt.tight_layout()
    plt.savefig("D:\\projects\\dachuang\\code\\fig\\confusion.png")
    # 显示图表
    plt.show()

def drawScatter(ds,names):
    markers = ["x", "o"]
    fig, ax = plt.subplots()
    x = range(len(ds[0]))
    for d,name,marker in zip(ds,names,markers):
        ax.scatter(x,d,alpha=0.6,label=name,marker=marker)
        ax.legend(fontsize=16, loc='upper left')
        ax.grid(c='gray')
    plt.savefig("D:\\projects\\dachuang\\code\\fig\\pre.png")
    plt.show()