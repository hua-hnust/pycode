#coding=utf-8

name = "xhua"
age = 23
height = 174
print "My name is " + name + ",My age " + str(age) + ",My height " + str(height)

#这是一个注释，下面学习数组的用法
array = [2,1,5,3]
print array[2]
array.append(6)
print array

for num in array:
    print num

print "通过下标遍历"
for i in range(0,len(array)):
    print array[i]


print "逆序遍历"
array.reverse() #反转数组
for num in array:
    print num

print "判断成员是否在数组中"
if 2 in array:
    print "2 在数组中"
else:
    print "不在"

a = 0
b = 10
c = 20

if b and c:
    print "true"
else:
    print "false"

if a and b:
    print "true"
else:
    print "false"

if a or b:
    print "false"
else:
    print "true"

