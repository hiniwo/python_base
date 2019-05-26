#coding=utf-8

# 函数不会状态提升

# import module

import math

# from module import sum

import module

print dir(module)

def printme(str):

    print(str)

    return 'false'

printme(dir(module))

# printme('nihaoma')
# python函数传参
# 必备参数
# 关键字参数
# 默认参数
# 不定长参数

def printinfo(arg1, *vartuple):
    # "打印任何传入的参数"
    print "输出: "
    print arg1
    for var in vartuple:
        print var
    return


# 调用printinfo 函数
printinfo(10)
printinfo(70, 60, {
    'name': 'wwm',
    'age': '18'
})




# 全局对象不能再函数中找到如果没有申明
Money = 2000


def AddMoney():
    # 想改正代码就取消以下注释:
    # global Money

    Money = 1
    Money = Money + 1
    printme(Money)


print Money
AddMoney()
print Money

print globals()



