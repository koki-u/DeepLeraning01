# coding: utf-8
import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('deep-learning-from-scratch/dataset/lena.png') # 画像の読み込み
plt.imshow(img)

plt.show()