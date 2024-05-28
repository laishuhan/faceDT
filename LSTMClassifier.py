import torch
import torch.nn as nn
import numpy as np
from util import *

#加载数据
X_train,y_train,X_test,y_test=data_load()
#print(y_test)
#print(X_train.shape,y_train.shape,X_test.shape,y_test.shape)

#训练模型
def train_model(model, X_train, y_train, num_epochs,batch_size):
    loss_list = []
    for epoch in range(num_epochs):
        for i in range(0, len(X_train), batch_size):
            inputs = torch.from_numpy(X_train[i:i + batch_size].astype(np.float64)).float().unsqueeze(1)
            labels = torch.from_numpy(y_train[i:i + batch_size]).long()

            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

        loss_list.append(loss.item())

        
        print('Epoch [{}/{}], Loss: {:.4f}'.format(epoch + 1, num_epochs, loss.item()))
    return loss_list

#评估
def evaluate_model(model, X, y,name):
    model.eval()
    with torch.no_grad():
        inputs = torch.from_numpy(X.astype(np.float64)).float().unsqueeze(1)
        labels = torch.from_numpy(y).long()
        outputs = model(inputs)
        # print(outputs)
        _, predicted = torch.max(outputs.data, 1)
        accuracy = (predicted == labels).sum().item() / labels.size(0)

    print(' {} Accuracy: {:.2f}%'.format(name,accuracy * 100))
    print("labels:",labels)
    print("predicted:",predicted)
    return labels,predicted

#绘制损失曲线
def plot_loss(loss_list):
    plt.plot(loss_list)
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title('Loss')
    plt.show()

#定义模型
class LSTMClassifier(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(LSTMClassifier, self).__init__()
        self.hidden_size = hidden_size
        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        _, (h_n, _) = self.lstm(x)
        output = self.fc(h_n[-1])
        return output

#设置参数
input_size = X_train.shape[1]  #特征数
output_size = 2    #分类数
#output_size = len(np.unique(y_train)) #分类数
hidden_size = 16
num_epochs = 50
batch_size=32
#print("input_size,output_size",input_size,output_size)

#实例化模型
model = LSTMClassifier(input_size, hidden_size, output_size)
#损失函数
criterion = nn.CrossEntropyLoss()
#优化器
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

#训练
loss_list = train_model(model, X_train, y_train, num_epochs,batch_size)

#评估测试集
#labels,predicted=evaluate_model(model, X_test, y_test,"X_test")

#评估训练集
labels,predicted=evaluate_model(model, X_train, y_train,"X_train")

#绘图
plot_loss(loss_list)

#绘制混淆矩阵
plot_confusion(labels,predicted)

#绘制散点图
drawScatter([labels, predicted], ['true', 'pred'])
