# coding: utf-8

if '__file__' in globals():
    import os, sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from and_gate import AND_2
from or_gate import OR
from nand_gate import NAND
import matplotlib.pyplot as plt
import numpy as np


#2層にすることで、XORゲートが実現した。
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND_2(s1, s2)
    return y

if __name__ == '__main__':
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y = XOR(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))

#XORゲートをパーセプトロンで表現するためには？
#どのようなパラメータであればよいのか？

#グラフで考えればよい
#
x = np.arange(-3, 3, 0.1)
y = -x + 0.5
data = [0]
y_data = [0]
data_not = [1, 1, 0]
data_y_data_not = [0, 1, 1]
plt.plot(x, y)
plt.scatter(data, y_data, marker='o')
plt.scatter(data_not, data_y_data_not, marker='+')
plt.grid()
plt.show()
#lineよりも下のscatterは、出力という概念が、orゲート

#XORはどう考えても1本の線では無理がある。

#そこで非線形のグラフを考える。