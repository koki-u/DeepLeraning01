# coding: utf-8
import numpy as np
import matplotlib.pylab as plt

#ただしこの関数だと、浮動小数点しかだめなので、NumPyの配列をきょかするために、step_function関数を実装する
def step_function_00(x):
    if x > 0:
        return 1
    else:
        return 0


def step_function(x):
    #np.astype(np.int)を使うことで、True と　Falseを　0と１としてintに変換できる。
    return np.array(x > 0, dtype=np.int)

X = np.arange(-5.0, 5.0, 0.1)
Y = step_function(X)
plt.plot(X, Y)
plt.ylim(-0.1, 1.1)  # 図で描画するy軸の範囲を指定
plt.show()
