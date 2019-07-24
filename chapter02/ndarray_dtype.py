import numpy as np


def demo1():
    # 使用标量类型
    dt = np.dtype(np.int32)
    print(dt)


def demo2():
    # int8, int16, int32, int64 四种数据类型可以使用字符串 'i1', 'i2','i4','i8' 代替
    dt = np.dtype('i4')
    print(dt)


# 结构化数据类型的使用，类型字段和对应的实际类型将被创建。
def demo3():
    # 首先创建结构化数据类型
    dt = np.dtype([('age', np.int8)])
    print(dt)
    # 将数据类型应用于 ndarray 对象
    a = np.array([(10,), (20,), (30,)], dtype=dt)
    print(a)
    print(a.shape)
    # 类型字段名可以用于存取实际的 age 列
    print(a['age'])


# 下面的示例定义一个结构化数据类型 student，包含字符串字段 name，
# 整数字段 age，及浮点字段 marks，并将这个 dtype 应用到 ndarray 对象。
def demo4():
    student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
    print(student)
    a = np.array([('abc', 21, 50), ('xyz', 18, 75)], dtype=student)
    print(a)


demo4()
