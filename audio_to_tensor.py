

import librosa
import numpy as np

# 加载音频文件
audio_file = "D:\\projects\\dachuang\\dataset\\dfdc\\audio_45\\aaeflzzhvy.wav"
y, sr = librosa.load(audio_file, sr=None)

# 提取每秒的音频特征向量
features = []
for i in range(10):
    start_time = i * sr
    end_time = (i + 1) * sr
    # 提取特征向量
    feature_vector = librosa.feature.mfcc(y=y[start_time:end_time], sr=sr)
    features.append(feature_vector)

# 将特征向量写入文件
with open("D:\\projects\\dachuang\\code\\lab\\audio.txt", "w") as file:
    for feature_vector in features:
        #file.write(str(len(feature_vector[0])) + "\n")  # 写入特征向量长度
        # 将特征向量数据转换为整数并写入文件，用逗号分隔
        file.write("[[")
        np.savetxt(file, feature_vector.astype(int), delimiter=' ', fmt='%d')  
        file.write("]]")  
        file.write('\n')  
        # 写入空行，用于分隔不同时间段的特征向量
