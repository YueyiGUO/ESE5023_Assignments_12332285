# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 18:19:23 2023

@author: Administrator
"""

# # 1.Flowchart

# In[33]:


#定义函数
def Print_values():
    a = float(input('Enter number a:'))
    b = float(input('Enter number b:'))
    c = float(input('Enter number c:'))
    if a>b:
        if b>c:
            print(a,b,c)
        else:
            if a>c:
                print(a,c,b)
            else: 
                print(c,a,b)
    else: 
        if b>c:
            if a>c:
                print(a,c,b)
            else:
                print(c,a,b)
        else:
            print(c,b,a)
Print_values()
