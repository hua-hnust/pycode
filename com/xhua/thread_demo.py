#!/usr/bin/python
# -*- coding: UTF-8 -*-

import thread
import time

def print_time(threadName,delay):
    count = 0
    while count<3:
        time.sleep(delay)
        count += 1
        print "%s : %s" % (threadName,time.ctime(time.time()))


try:
    thread.start_new_thread(print_time,("thread-1",2,))
    thread.start_new_thread(print_time,("thread-2",4,))
except:
    print "Error"
while 1:
    pass