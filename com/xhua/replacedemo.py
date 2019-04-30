#!/usr/bin/python
# -*- coding: UTF-8 -*-

str = 'hello my python demo'
str2 = str.replace('my','your')
#string 的 replace 方法，需要注意 replace 不会改变原 string 的内容。
print str,"\n",str2

#返回字符串第一次出现的位置，如果没有匹配则返回-1
print str.rfind('my')
print str.rindex('my')
# 在字符串左边填充某个元素至指定长度
print str.rjust(30,'X')
