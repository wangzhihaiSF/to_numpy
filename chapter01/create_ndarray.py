import numpy as np


# 创建一维数组
def create_one_dimensional():
    a = np.array([1, 2, 3])
    print(a)
    return a


# 创建多维数组
def create_n_dimensional():
    result = np.array([[1, 2], [3, 4]])
    print(result)
    return result


# 最小维度
def create_ndmin_dimensional(n):
    result = np.array([1, 2, 3, 4, 5], ndmin=n)
    print(result)
    return result


# dtype 类型指定
def create_dtype_dimensional(dtype=None):
    result = np.array([1, 2, 3], dtype=dtype)
    print(result)
    return result


# create_one_dimensional()
# create_n_dimensional()
# create_ndmin_dimensional(3)
create_dtype_dimensional(complex)
