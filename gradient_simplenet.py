# coding: utf-8
# coding: utf-8
if '__file__' in globals():
    import os, sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import numpy as np
from common.functions import softmax, cross_entropy_error
from common.gradient import numerical_gradient


class simpleNet:
    def __init__(self):
        self.W = np.random.randn(2,3)

    def predict(self, x):
        return np.dot(x, self.W)

    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y, t)

        return loss

x = np.array([0.6, 0.9])
t = np.array([0, 0, 1])

net = simpleNet()


#簡単な関数ならlambdaで1行でかける。
"""
lambdaの例文
def add_def(a, b=1):
    return a + b

add_lambda = lambda a, b=1: a + b

print(add_def(3, 4))
# 7

print(add_def(3))
# 4

print(add_lambda(3, 4))
# 7

print(add_lambda(3))
# 4
"""
f = lambda w: net.loss(x, t)
dW = numerical_gradient(f, net.W)

print(net.W)
print(dW)
