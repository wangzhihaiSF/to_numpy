import numpy as np


def demo1():
    a = np.arange(24)
    print(a.ndim)  # a 现在只有一个维度
    print(a)
    #  调整维度
    b = a.reshape(2, 4, 3)  # b 现在有三个维度
    print(b.ndim)
    print(b)


demo1()
