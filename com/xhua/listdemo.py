#!/usr/bin/python
# -*- coding: UTF-8 -*-

list = ['welcome']
list.append('Google')  ## 使用 append() 添加元素
list.append('Runoob')
print list
#删除第二个元素
del list[1]
print list

list = ['a','b','b','a','b','b']
#判断某个元素出现的次数
print list.count('b')

#在列表后一次追加多条
list.extend(['3','4','5'])
list2 = ['he','ab']
list.extend(list2)
print list

#找出和元素匹配的索引位置
print list.index('4')

#移除列表中的某个元素
list.remove('5')
print  list

# 反向逆转
list.reverse()
print list

print list.pop()