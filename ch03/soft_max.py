import numpy as np

a = np.array([1010, 1000, 990])
softmax =  np.exp(a) / np.sum(np.exp(a))
#これは正しく計算されない。
print(softmax)

#これにように、オーバーフロー対策として、最大の値を引いておけば安全。
c = np.max(a)
softmax = np.exp(a - c) / np.sum(np.exp(a - c))
print(softmax)

#softmaxは、確立的なアプローチになるから、分類に向いている。