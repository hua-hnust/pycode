#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time  # 引入time模块
import calendar  #引入日历模块

ticks = time.time()
print "当前时间戳为:", ticks

localtime = time.localtime(time.time())
print localtime

#获取格式化的时间
lt = time.asctime(time.localtime(time.time()))
print lt

# 格式化成2016-03-20 11:45:39形式
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# 格式化成Sat Mar 28 22:24:24 2016形式
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print '将格式化时间转化成时间戳：',time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))

cal = calendar.month(2019,4)
print '2019-5日历：',cal