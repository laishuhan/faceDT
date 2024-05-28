import torch
from torchvision import transforms
from PIL import Image

def image_to_tensor(image_path):
    # 定义转换
    preprocess = transforms.Compose([
        transforms.Resize((224, 224)),  # 调整大小为 224x224
        transforms.ToTensor()  # 转换为张量
    ])

    # 打开图像并应用转换
    image = Image.open(image_path)
    tensor = preprocess(image).unsqueeze(0)  # 添加批次维度

    return tensor

# 图片路径
image_path = "D:\\projects\\dachuang\\code\\pictures_trans\\frame0.jpg"

# 将图片转换为张量
tensor = image_to_tensor(image_path)
print(tensor)
