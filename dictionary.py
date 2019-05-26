#coding=utf-8
dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}

seq = ('Google', 'Runoob', 'Taobao')

dict = dict.fromkeys(seq)
print "新字典为 : %s" % str(dict)

dict = dict.fromkeys(seq, 10)
print "新字典为 : %s" % str(dict)