#!/usr/bin/python
# -*- coding: UTF-8 -*-

class person:
    def __init__(self,name,age,sex,birthday):
        self.name = name
        self.age = age
        self.sex = sex
        self.birthday = birthday

    def display(self):
        print self.name,',',self.age,',',self.sex,',',self.birthday

p = person('小明', 21, '男', '1998-12-5')
p.display()
#print p.__module__
#print p.__class__
#print p.__doc__


class student(person):
    def __init__(self,name,age,sex,birthday,classNum):
        person.__init__(self,name,age,sex,birthday)
        self.classNum = classNum


    def display(self):
        print self.name,self.age,self.sex,self.birthday,self.classNum

s = student('小明',21,'男','1998-12-5',2)
s.display()