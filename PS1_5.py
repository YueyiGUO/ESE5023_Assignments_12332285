# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 18:20:06 2023

@author: Administrator
"""

# # 5 Dynamic programming

# In[690]:


#5.1
import random
#定义函数，参数为数字串、目标为1到100随机整数、当前表达式和当前结果
def Find_expression(str_nums, target, exp="", result=0):
    if not str_nums:           #若数字串为空，说明已经遍历完所有数字
        if result == target:   #若当前结果等于目标整数，就打印出表达式
            print(str(exp) + "=" + str(target))
            return 1           #找到1个对应结果的表达式
        else:
            return 0           #未找到对应结果的表达式
            pass               #do nothing
    else:
        count = 0
        for i in range(1, len(str_nums) + 1):  #遍历数字串中每个数字
            num = int(str_nums[ :i])            #提取当前已遍历的数字串
            if not exp:               #若为第一个数，则直接加入表达式和结果中，再递归剩余数字
                count += Find_expression(str_nums[i: ], target, str(num), num)
            else:   # 否则进行加法或减法
                count += Find_expression(str_nums[i: ], target, exp + "+" + str(num), result + num)   #插入加号，更新表达式和结果，再递归剩余的数字，表达式个数加1
                count += Find_expression(str_nums[i: ], target, exp + "-" + str(num), result - num)   #插入减号，更新表达式和结果，再递归剩余的数字，表达式个数加1
        return count

rr = random.randint(1,101)
Find_expression("123456789", rr)
print("结果等于"+ str(rr)+"的表达式有"+ str(count)+"个")


# In[691]:


#5.2
#5.1
import random
import matplotlib.pyplot as plt
#定义函数，参数为数字串、目标为1到100随机整数、当前表达式和当前结果
def Find_expression(str_nums, target, exp="", result=0):
    if not str_nums:           #若数字串为空，说明已经遍历完所有数字
        if result == target:   #若当前结果等于目标整数，就打印出表达式
            print(str(exp) + "=" + str(target))
            return 1           #找到1个对应结果的表达式
        else:
            return 0           #未找到对应结果的表达式
            pass               #do nothing
    else:
        count = 0
        for i in range(1, len(str_nums) + 1):  #遍历数字串中每个数字
            num = int(str_nums[ :i])            #提取当前已遍历的数字串
            if not exp:               #若为第一个数，则直接加入表达式和结果中，再递归剩余数字
                count += Find_expression(str_nums[i: ], target, str(num), num)
            else:   # 否则进行加法或减法
                count += Find_expression(str_nums[i: ], target, exp + "+" + str(num), result + num)   #插入加号，更新表达式和结果，再递归剩余的数字，表达式个数加1
                count += Find_expression(str_nums[i: ], target, exp + "-" + str(num), result - num)   #插入减号，更新表达式和结果，再递归剩余的数字，表达式个数加1
        return count

rr = random.randint(1,101)
Find_expression("123456789", rr)
print("结果为"+ str(rr)+"的表达式有"+ str(count)+"个")

#5.2

counts = np.zeros((100))
for i in range(100):
    counts[i] = Find_expression("123456789", i)
    print("结果为"+ str(i)+"的表达式有"+ str(count)+"个")
    # Append the number of solutions to the list
#    counts.append(str(count))
print(counts)

import numpy as np
print(np.where(counts==max(counts)))  #打印最大个数表达式
print(np.where(counts==min(counts)))  #打印最小个数表达式

plt.plot(range(1, 101), counts)  # 用matplotlib库来绘制列表，横轴是整数，纵轴是解的数量
plt.title("counts of the expression")   # 添加标题和坐标轴标签
plt.xlabel("Integer")
plt.ylabel("counts of solutions")
plt.show()
