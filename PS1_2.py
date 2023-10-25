# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 18:18:19 2023

@author: Administrator
"""

# # 2.Matrix multiplication

# In[247]:


# 2.1 创建矩阵M1、M2
import random
r1 = 5      #定义矩阵M1、M2行列数
c1 = 10
r2 = 10
c2 = 5
M1 = [[0 for j in range(c1)] for i in range(r1)]     #创建空的二维list作为矩阵M1、M2
M2 = [[0 for j in range(c2)] for i in range(r2)]
for i in range(r1):
    for j in range(c1):
        M1[i][j] = random.randint(0,50)
for j in range(r2):
    for k in range(c2):
        M2[j][k] = random.randint(0,50)
print(M1)
print(M2)
# 2.2 矩阵乘法运算
def Matrix_multip(M1, M2):                           #定义矩阵乘法函数
    result = [[0] * len(M2[0]) for _ in range(r1)]   #矩阵result行数为M1的行数，列数为M2的列数
    for i in range(len(M1)):                         #按行遍历M1矩阵
        for j in range(len(M2[0])):                  #按列遍历M2矩阵
            for k in range(len(M2)):                 #按行遍历M2矩阵
                result[i][j] += M1[i][k] * M2[k][j]  
    return result

print(result)                                       #打印矩阵乘法结果

