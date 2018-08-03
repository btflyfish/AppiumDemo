#定义递归函数，计算阶乘
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
#调用递归阶乘函数
print('5!的值是:',fact(5))
print('10!的值是:',fact(10))