#!/usr/bin/python
# -*- coding: UTF-8 -*-

#传入字符串
def printme(str):
    print str
    return
printme("你好")

#传参
def count(a,b):
    print a+b
    return
count(3,2)

#传可变参数
def printList(list):
    list.append(4)
    return
list = [1,2,3]
printList(list)
print list

#传不可变参数
def unchange(a):
    a=10
    return
a=2
unchange(a)
print a

#lambda表达式  匿名函数
sum = lambda a,b:a+b
print '拉姆达表达式：',sum(2,3)

#返回值，乘法
def mult(a,b):
    return a*b
print '返回乘法结果：',mult(4,5)

# 全局变量与局部变量
total =5
def comtotal(a,b):
    total = a*b
    print '局部变量：',total
    return total
comtotal(4,2)
print '全局变量：',total
