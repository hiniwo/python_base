#coding=utf-8


# 格式化操作符（%）

string = "Hello\tWill\n"

print "%s" %string
print "%r" %string

num = 100

print "%d to hex is %x" %(num, num)
print "%d to hex is %X" %(num, num)
print "%d to hex is %#x" %(num, num)
print "%d to hex is %#X" %(num, num)

# 浮点数
f = 3.1415926
print "value of f is: %.4f" %f

# 指定宽度和对齐
students = [{"name":"Wilber", "age":27}, {"name":"Will", "age":28}, {"name":"June", "age":27}]
print "name: %10s, age: %10d" %(students[0]["name"], students[0]["age"])
print "name: %-10s, age: %-10d" %(students[1]["name"], students[1]["age"])
print "name: %*s, age: %0*d" %(10, students[2]["name"], 10, students[2]["age"])

# dict参数
# for student in students:
# print "%(name)s is %(age)d years old" %student

# 对于Python的格式化操作符，不仅可以接受tuple类型的参数，也可以支持dict，
# 象上面代码的最后一部分，那么格式化字符串中就可以直接使用"%(key)s"（
# 这里的s根据具体类型改变）的方式表示dict中对应的value了。

# 字符串内建函数format()

print "{0} is {1} years old".format("Wilber", 28)
print "{} is {} years old".format("Wilber", 28)
print "Hi, {0}! {0} is {1} years old".format("Wilber", 28)

S = 'nihoshohoiho'
print S.upper()