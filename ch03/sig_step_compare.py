# coding: utf-8
import numpy as np
import matplotlib.pylab as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-x))    


def step_function(x):
    return np.array(x > 0, dtype=np.int)

x = np.arange(-5.0, 5.0, 0.1)
y1 = sigmoid(x)
y2 = step_function(x)

plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, y1)
plt.plot(x, y2, 'k--')
#ylimのlimはlimit
plt.ylim(-0.1, 1.1) #図で描画するy軸の範囲を指定
plt.grid()
plt.show()

#sigmoidとstep_functionの違いは、水の量を例にとると<ししおどし>と<水車>
#どれぐらいの水を反映するか？
#<ししおどし>ならば一斉に水を放出するので、０ or 1しかとらない
#<水車>ならば、徐々に水を出すが、最終的な達成点は限界がある。