# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 18:19:52 2023

@author: Administrator
"""

# # 4 Add or double

# In[362]:


import random
x = random.randint(1,100)
def Least_moves(x):           #定义函数
    if x == 1:
        return 0              #x==1时，返回0，表示0次即获得1元
    else:
        tt = 0                #初始化次数tt
        while x > 1:
            if x % 2 == 0:    
                x = x // 2    #若x为偶数，则将x除以2（即钱数double）
            else:
                x -= 1        #若x为奇数，则将x减去1（即钱数增加1元）
            tt += 1
        return tt
    
#Least_moves(x)
print(x)                     #打印随机整数x
print(Least_moves(x))        #打印计算所需最小次数

