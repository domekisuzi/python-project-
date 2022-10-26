import numpy as np
a = np.array([[1,2,3,4],
          [2,3,4,5]
          ])
print(a.shape)
b = np.array([[1],
             [2],
             [4],
             [6]])
print(b.shape)
# 矩阵相乘
c = np.matmul(a,b)
print(c)