import functools
import time
#定义一个能打印日志的decorator函数
def log(func):
    def wrapper(*args,**kw):
        print('call %s():'%func.__name__)
        return func(*args,**kw)
    return wrapper
@log
#设计一个函数，他作用在任何函数上，并打印函数的执行时间
def metric(fn):
    print('%s 执行时间为 %s ms'%(fn.__name__,10.24))
    return fn
def now():
    print('2018-1-2')
#调用装饰器
now()
#调用装饰器
@metric
def fast(x,y):
    time.sleep(0.12)
    return x+y
@metric 
def slow(x,y,z):
    time.sleep(0.35)
    return x*y*z
f=fast(11,22)
s=slow(2,3,4)
if f!=33:
    print('测试fast失败！')
elif s!=24:
    print('测试slow失败！')
else:
    print('两个装饰器均调用成功！')
#调用偏函数示例
int2=functools.partial(int,base=2)
print('输出偏函数示例',int2('10001001'))
print(int2('00000110',base=10))


