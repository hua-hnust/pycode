#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = curPath[:curPath.find('codePy\\')+len('codePy\\')]
print rootPath

print '***获取当前路径***'
print os.getcwd()
print os.path.abspath(os.path.dirname(__file__))

print '***获取上级目录***'
print os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
print os.path.abspath(os.path.dirname(os.getcwd()))
print os.path.abspath(os.path.join(os.getcwd(), ".."))

datadir = os.path.abspath(os.path.dirname(os.getcwd())) + '\\data'
print datadir

fo = open(datadir + '\\test.txt','a')
print "文件名: ", fo.name
print "是否已关闭 : ", fo.closed
print "访问模式 : ", fo.mode
print "末尾是否强制加空格 : ", fo.softspace
#fo.close()
#print "是否已关闭 : ", fo.closed

fo.write('123'.decode('utf-8'))
str = fo.read(10)
print str
fo.close()

if os.path.isdir(datadir + '\\mydata'):
    print '文件已存在'
else:
    os.mkdir(datadir + '\\mydata')
    print '创建文件成功'