import cv2
import os
from PIL import Image

# 从指定的路径读取视频
cam = cv2.VideoCapture("D:\\projects\\dachuang\\dataset\\dfdc\\video_45\\aaeflzzhvy.mp4")

try:
    # 创建名为data的文件夹
    if not os.path.exists('pictures'):
        os.makedirs('pictures')

except OSError:
    print('Error: Creating directory of data')

# 获取视频的帧率
fps = cam.get(cv2.CAP_PROP_FPS)

# 计数器，用于计算已经过去了多少帧
frame_counter = 0

while True:
    # 读取视频帧
    ret, frame = cam.read()

    # 如果读取失败，退出循环
    if not ret:
        break

    # 如果帧计数器能被帧率整除，表示已经过了一秒，提取当前帧
    if frame_counter % int(fps) == 0:
        # 创建文件名
        name = './pictures/frame' + str(frame_counter) + '.jpg'
        print('Creating...' + name)

        # 写入图像文件
        cv2.imwrite(name, frame)

    # 增加帧计数器
    frame_counter += 1

# 释放资源
cam.release()
cv2.destroyAllWindows()

def resize_images_in_folder(input_folder, output_folder, target_size=(224, 224), channels=3):
    # 创建输出文件夹
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # 如果是图片文件
        if os.path.isfile(input_path) and any(filename.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.bmp']):
            # 打开图片
            img = Image.open(input_path)
            
            # 将图片调整大小并转换通道数
            img = img.resize(target_size, Image.ANTIALIAS)
            if img.mode != 'RGB' and channels == 3:
                img = img.convert('RGB')
            
            # 保存调整后的图片
            img.save(output_path)
            print(f"Processed: {output_path}")

# 输入和输出文件夹路径
input_folder = "D:\\projects\\dachuang\\code\\pictures"
output_folder = "D:\\projects\\dachuang\\code\\pictures"

# 调用函数来处理图片
resize_images_in_folder(input_folder, output_folder)
