import numpy as np

#教師ラベルが、one-hot表現でない時の交差エントロピー誤差の実装
#batch_sizeで正規化する。

def cross_entropy_error(y, t):
    if y.dim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    batch_size = y.shape[0]
    #↓one-hot専用になってしまう。
    #return -np.sum(t * np.log(y)) / batch_size
    return -np.sum(np.log([np.arange(batch_size), t])) / batch_size

#np.arange(batch_size) ：　0から batch_size - 1 まで配列を生成する。
t = [2, 7, 0, 9, 4]
batch_size = 5

sum = [np.arange(batch_size), t]
print(sum)