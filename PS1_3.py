# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 18:19:38 2023

@author: Administrator
"""

# # 3 Pascal triangle

# In[333]:


def Pascal_triangle(n):                   #定义帕斯卡函数，参数n为行数
    result = []
    for i in range(n):
        k = [1]
        if i > 0:
            for j in range(1, i):
                new_k = k[j - 1] + result[i - 1][j]   # 当前行各元素等于上一行对应位置元素之和
                k.append(new_k)
            k.append(1)
        result.append(k)
    return result

n1 = 100
n2 = 200
for r in Pascal_triangle(n1):  #打印前100行、前200行帕斯卡三角
    print(r)
print("\n——————————————————————————\n")
for r in Pascal_triangle(n2):
    print(r)

