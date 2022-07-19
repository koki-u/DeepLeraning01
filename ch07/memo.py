#Affineレイヤを全結合層として用いてきた。
#CNNでは、Affineレイヤ→Convレイヤ + Poolingレイヤ　として考える

#つまり
#Affine - ReLU　→　Convolution - ReLU - Pooling　とする

#-----------------------------------------------------

#全結合層
#問題点：画像なら3次元データだが、形状を無視してすべての入力データを同等のニューロンであつかうから、形状に関するデータを生かせない。
#形状を維持するのが大事ということ。特徴を生かせないから。そこで、畳み込みそうを使う

#畳み込み層：形状を維持して、そのまま次の層に出力できる。
#入出力データを特徴マップという。
#入力データを入力特徴マップ、出力マップを出力特徴マップと言う。

#畳み込み演算とパディングの話は知っているのでパス。
#畳み込み演算：フィルターをストライド毎に動かして計算する。
#パディング：出力サイズの調整

#３次元データの畳み込み層は、必ずチャンネル数を一致させなければならない。
#ただし、フィルタのサイズは自由

#バイアスを足すときには、broadcast機能を使えば自動で計算してくれる。
#--------------------------------------------------------
#Poolingの話

#一般的に、プーリング層のウィンドウサイズと、ストライドは同じ値に設定する。
#3×3のウィンドウは、ストライド3×3など。。。

#学習するパラメータはない；対象領域から最大値をとる or 平均値を取るだけの処理なので、学習スべきパラメータはない。
#チャンネル数も変化しない；チャンネル毎に独立して計算する。
#微小な位置変化に対してロバスト；入力データに微小なズレがあってもプーリングがそれを吸収してくれる。
#---------------------------------------------------------

#CNNでは、各層を流れるデータは4次元形状をしている。
#im2colによる展開を行なうことで、フィルターの計算をしやすくなる。
#例として、3次元ブロックを2次元の平面に直すことで、フィルター計算しやすくなる。
#image to column が語源らしい。

if '__file__' in globals():
    import os, sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import numpy as np

from common.util import im2col

x1 = np.random.rand(1, 3, 7, 7)
col1 = im2col(x1, 5, 5, stride=1, pad=0)
print(col1.shape)

x2 = np.random.rand(10, 3, 7, 7)
col2 = im2col(x2, 5, 5, stride=1, pad=0)
print(col2.shape)