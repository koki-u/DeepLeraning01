# coding: utf-8
#固有の重みを乗算される。送られてきた信号の総和が計算されたら、閾値を超えた場合に出力。
#閾値はちなみに<θ>で表される

#重みは電流でいうところの抵抗に相当する。抵抗は電流の流れに草を決めるパラメータ。
#抵抗が低ければ低いほど大きな電流が流れる。＝　重みが重ければ重いほど大きな影響を及ぼす。
import numpy as np

def AND_1(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

def AND_2(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    #np.sum()で各要素の総和が計算される。
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

if __name__ == '__main__':
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y = AND_2(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))
