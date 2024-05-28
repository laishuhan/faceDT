from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
 


fpr = [0, 0.1,0.2, 0.3, 0.4, 0.5, 0.6, 0.7 ,0.8,0.9,1]
tpr = [0, 0.55,0.57, 0.67, 0.85, 0.87,0.88, 0.9, 0.92, 0.95,1]

roc_auc = auc(fpr, tpr)
 
plt.plot(fpr, tpr, 'k--', label='ROC (area = {0:.2f})'.format(roc_auc), lw=2)
 
plt.xlim([-0.05, 1.05])  # 设置x、y轴的上下限，以免和边缘重合，更好的观察图像的整体
plt.ylim([-0.05, 1.05])
plt.xlabel('FPR')
plt.ylabel('TPR')  # 可以使用中文，但需要导入一些库即字体
plt.title('ROC Curve')
plt.legend(loc="lower right")
plt.show()