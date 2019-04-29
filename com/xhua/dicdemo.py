#!/usr/bin/python
# -*- coding: UTF-8 -*-

dict = {'name':'花花','age':22,'class':'666'}
print dict['name']

#值可以是任何数据类型
list3 = ['a','b','c']
dict['list'] = list3
print dict

#添加内容
dict['name'] = '小明'
print dict

#删除内容
del dict['class']
print dict

#字典长度
print len(dict)

#返回字典所有的值
print dict.values()