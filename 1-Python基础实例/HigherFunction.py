#导入函数
from functools import reduce
#定义一个高阶函数
def add(x,y,f):
    return f(x)+f(y)
#定义一个函数求平方
def sqr(x):
    return x*x
#定义一个函数求和
def add1(x,y):
    return x+y
#定义一个变换整数的函数
def fn(x,y):
    return x*10+y
#定义一个过滤函数，保留奇数
def is_odd(n):
    return n%2==1
#定义一个奇数序列，从3开始
def odd_iter():
    n=1
    while True:
        n=n+2
        yield n
#定义一个筛选函数，下面表达式其实是一个简易函数
def not_divisible(n):
    return lambda x:x%n>0
#定义一个生成器，不断返回下一个素数
def primes():
    yield 2
    it=odd_iter()
    while True:
        #返回序列的第一个数
        n=next(it)
        #yield返回一个生成器
        yield n
        it=filter(not_divisible(n),it)
#按名字排序
def by_name(t):
    return t[0].lower()
#按分数升序排序
def by_score(t):
    return t[1]
     
print('高阶函数map和reduce调用')
x=-5
y=6
f=abs
print(add(x,y,f))
r=map(sqr,[1,2,3,4,5,6])
print(list(r))
print(list(map(str,[1,2,3,4])))
print(reduce(add1,[1,3,5,7,9]))
print(reduce(fn,[1,3,5,7,9]))
print('高阶函数filter调用')
print(list(filter(is_odd,[1,2,3,6,7,10])))
print('strip方法实例')
str = "0000000this is string example....wow!!!0000000"
print(str.strip('0'))
str1 = "0000000this is string 00000 example....wow!!!0000000"
print(str1.strip('0'))
#打印1000内的素数
count=0
print('打印1000内的素数')
for n in primes():
    
    #每20个数一行
    if count%20==0:
        print()
    if n<1000:
        print('%3d'%(n),end=' ')
    else:
        break
    count=count+1
print()
print('sorted函数演示示例：')
print('sorted([36,5,-12,9,-21])排序结果是',sorted([36,5,-12,9,-21]))
print('sorted([36,5,-12,9,-21],key=abs)排序结果是',sorted([36,5,-12,9,-21],key=abs))
print('sorted([\'bob\',\'about\',\'Zoo\',\'Credit\'])的排序结果是:',sorted(['bob','about','Zoo','Credit']))
#下面代码在VS2017调试不了
#print(sorted(['bob','about','Zoo','Credit'],key=str.lower))
L=[('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]
print('按名字排序：',sorted(L,key=by_name))
print('按分数排序：',sorted(L,key=by_score))