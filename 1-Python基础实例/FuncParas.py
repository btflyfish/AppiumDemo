#注册学生信息
def enroll(name,gender,age=6,city='包头'):
    print('姓名:',name,'性别:',gender,'年龄:',age,'城市:',city)
#可变参数函数演示
def calc(numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum
#可变参数函数演示，使用指针
def calc1(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum
#关键字参数的使用
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)
#命名关键字参数的使用
def person1(name,age,*,city,job):
    print('name:',name,'age:',age,'city:',city,'job:',job)
#演示参数组合的使用
def f1(a,b,c=0,*args,**kw):
    print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)
def f2(a,b,c=0,*,d,**kw):
    print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)
#计算多个数的乘积，可以接受1个或者多个数
def multi(a,*nums):
    sum=a
    for num in nums:
        sum=sum*num
    return(sum)
print('学生注册信息打印')
enroll('余珂蒙','女',11,'蕲春')
enroll('余瑶瑶','女')
enroll('江雨','女',22,'黄石')
print('可变参数函数演示')
print(calc([1,2,3]))
print(calc((1,2,3)))
print(calc1(2,3,5))
nums=[4,6,8]
print(calc1(nums[0],nums[1],nums[2]))
print('关键字参数演示实例')
person('李宁',40)
person('耐克',100,城市='北京')
person('匹克',30,城市='晋江',渠道='网购')
person('特朗普',70,爱好='减税')
print('命名关键字参数演示实例')
#注意区分位置参数和命名关键字参数
person1('陈初友',40,city='广州',job='教育机构')
#参数组合调用
print('调用组合参数实例')
f1(1,2)
f1(1,2,3)
f1(1,2,3,args=('a','b'),x=99)
f2(1,2,5,d=99,simon=95,Mary=85,Tom=70)
#计算多个数的乘积，并加测试代码
print('计算1个数的乘积:',multi(2))
print('计算2个数的乘积:',multi(2,4))
print('计算3个数multi(2,4,5)的乘积:',multi(2,4,5))
print('计算4个数multi(2,4,6,7)的乘积:',multi(2,4,6,7))
print('计算5个数multi(2,3,8,9,10)的乘积:',multi(2,3,8,9,10))
#测试代码
if multi(2,4,5)!=40:
    print('测试失败')
elif multi(2,4,6,7)!=336:
    print('测试失败')
elif multi(2,3,8,9,10)!=4320:
    print('测试失败')
else:
    try:
        #抛出一个异常
        multi()
        print('测试失败！')
    except TypeError:
        print('测试成功')

