#!/usr/bin/python
# -*- coding: UTF-8 -*-

#演示循环的用法
i = 2
while (i < 100):
    j = 2
    while (j <= (i / j)):
        if not (i % j): break
        j = j + 1
    if (j > i / j): print i, " 是素数"
    i = i + 1

print "Good bye!"

#演示break语句的用法
for letter in 'python':
    if letter == 'h':
        break
    print '当前字母：',letter

var = 10
while var > 0:
    print '当前变量值：',var
    var = var - 1
    if var == 5:
        break
print "Good bye!"


#演示 continue 的用法
for letter in 'Python':  # 第一个实例
    if letter == 'h':
        continue
    print '当前字母 :', letter

var = 10  # 第二个实例
while var > 0:
    var = var - 1
    if var == 5:
        continue
    print '当前变量值 :', var
print "Good bye!"
