#定义一个返回求和的函数
def lasy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax=ax+n
        return ax
    return sum
#定义一个多个内部函数的返回函数
def count():
    fs=[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
#调用求和函数
print('调用求和函数示例:')
f=lasy_sum(1,3,5,7,9)
print('输出求和函数的返回值',f)
print('输出求和函数的计算值',f())
#比较返回函数的所在地址是否相同，f和f1即使参数值均相同时
f1=lasy_sum(1,3,5,7,9)
print('输出求和函数的返回值',f1)
print('输出闭包的值')
f2,f3,f4=count()
print('f2()=%d,f3()=%d,f4()=%d'%(f2(),f3(),f4()))
print(f2)
print('打印list(map(lambda x:x*x,[1,2,3,4,5,6,7,8,9])):',list(map(lambda x:x*x,[1,2,3,4,5,6,7,8,9])))
f5=lambda x:x*x*x
print('f5函数地址是:',f5)
print('f5(10)的结果值是：',f5(10))
#定义一个求奇偶的匿名函数
f6=lambda x:x%2==1
L=list(filter(f6,range(1,20)))
print('list(filter(f6,range(1,20)))中所有奇数是：',L)