#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib2

response = urllib2.urlopen('http://www.baidu.com')
print response.read()

request = urllib2.Request('http://www.baidu.com')
response1 = urllib2.urlopen(request)
str = response.read()
print str