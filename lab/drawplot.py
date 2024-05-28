import matplotlib.pyplot as plt
import matplotlib

# 设置支持中文的字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号

# 数据
guess = ["伪造", "真实"]
fact = ["伪造", "真实"]
classes = list(set(fact))
classes.sort(reverse=True)
confusion_train = [[900, 0], [1, 99]]  # 训练集的混淆矩阵
confusion_test = [[84, 6], [2, 8]]  # 假设的测试集混淆矩阵

fig, ax = plt.subplots(1, 2, figsize=(14, 7))  # 设置plt窗口的大小，并创建两个子图

# 绘制训练集混淆矩阵
ax[0].imshow(confusion_train, cmap=plt.cm.Blues)
indices = range(len(confusion_train))
ax[0].set_xticks(indices)
ax[0].set_xticklabels(classes, rotation=40, fontsize=18)
ax[0].set_yticks(indices)
ax[0].set_yticklabels(classes, fontsize=18)
ax[0].set_ylim(1.5, -0.5)  # 设置y轴的上下限

ax[0].set_title("训练集", fontdict={'weight': 'normal', 'size': 25})
cb = fig.colorbar(ax[0].images[0], ax=ax[0])
cb.ax.tick_params(labelsize=18)
ax[0].set_xlabel('#预测标签', fontsize=15)
ax[0].set_ylabel('#真实标签', fontsize=15)




for first_index in range(len(confusion_train)):
    for second_index in range(len(confusion_train[first_index])):
        color = "white" if confusion_train[first_index][second_index] > 100 else "black"
        ax[0].text(second_index, first_index, confusion_train[first_index][second_index], fontsize=18, color=color,
                   verticalalignment='center', horizontalalignment='center')

# 绘制测试集混淆矩阵
ax[1].imshow(confusion_test, cmap=plt.cm.Blues)
indices = range(len(confusion_test))
ax[1].set_xticks(indices)
ax[1].set_xticklabels(classes, rotation=40, fontsize=18)
ax[1].set_yticks(indices)
ax[1].set_yticklabels(classes, fontsize=18)
ax[1].set_ylim(1.5, -0.5)  # 设置y轴的上下限

ax[1].set_title("测试集", fontdict={'weight': 'normal', 'size': 25})
cb = fig.colorbar(ax[1].images[0], ax=ax[1])
cb.ax.tick_params(labelsize=18)
ax[1].set_xlabel('#预测标签', fontsize=15)
ax[1].set_ylabel('#真实标签', fontsize=15)



for first_index in range(len(confusion_test)):
    for second_index in range(len(confusion_test[first_index])):
        color = "white" if confusion_test[first_index][second_index] > 50 else "black"
        ax[1].text(second_index, first_index, confusion_test[first_index][second_index], fontsize=18, color=color,
                   verticalalignment='center', horizontalalignment='center')

plt.tight_layout()
plt.show()
