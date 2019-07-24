## NumPy Ndarray 对象

Numpy 最重要的一个特点就是 N 维数组对象 ndarray, 它是一系列同类数据的集合，索引以 0 开始。

### 特点：
1. ndarray 对象适用于存放同类元素的多维数组。
2. ndarray 中的每个元素在内存中都有相同大小的存储区域。

### ndarray 内部由一下组成：

* 一个纸箱数据（内存或内存映射文件中的一块数据）的指针。
* 数据类型（dtype），描述在数组中的固定大小格子
* 一个表示数组的形状（shape）的元组，表示各维度的元组
* 一个跨度元组（stride），其中的整数是指为了前进到当前维度下一个元素需要跨过的字节数。

跨度可以是负数，这样数组在内存中就可以向后移动，例如切片object[::-1]就是如此。

### ndarray 创建
```python
numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
```
**参数说明**

|名称|描述|
| --- | --- |
|object|数组或嵌套的数列|
|dtype|数组元素的数据类型，可选|
|copy|对象是否需要复制，可选|
|order|创建数组的样式，C 为行方向，F 为列方向，A 为任意方向（默认）|
|subok|默认返回一个与基类类型一致的数组|
|ndmin|指定生成数组的最小维度|

**实例**
```python
import numpy as np
a = np.array([1, 2, 3])
print(a)

```


