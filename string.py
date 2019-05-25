#coding=utf-8

var1 = 'Hello World!'

var2 = "Python Runoob"

print "var1[0]: ", var1[0]

print "var2[1:5]: ", var2[1:5]

print "更新字符串 :- ", var1[:6] + 'Runoob!' \
    + 'wwm' + '\n' + 'jinini'

print '更新字符串: 2', var2[:1] + 'wwm'

print 'H' in var1

print 'H' not in var1

var3 = var1[3:]

print var3

# 格式化字符串
print "My name is %s and weight is %d kg!" % ('Zara', 21)

hi = '''hi
        therr'''
print '%r', hi
print '%s', hi

string = "Hello\tWill\n"

print "%s" %string
print "%r" %string

print hi.capitalize()


