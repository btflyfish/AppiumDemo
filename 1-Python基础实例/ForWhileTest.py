
names=['飞鸟工作室','软件测试','数据分析']
for name in names:
    print(name)
print('计算1-10的和')
sum=0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum=sum+x
print(sum)
print('计算1-100的和')
sum=0
for x in list(range(101)):
    sum=sum+x
print(sum)
dreams=['身心健康','成为软测专家','旅行30天']
i=0
while i<=2:
    print('Hello,2018年的个人梦想是',dreams[i])
    i=i+1
print('理解Break和Continue语句')
print('当循环到10时，结束整个循环')
n=1
while n<=100:
    if n>10:
        break;
    print(n)
    n=n+1
print('循环整个结束')
print('打印1-100之间能被19整除的数')
n=0
while n<=100:
    n=n+1
    if(n%19!=0):
        continue;
    else:
        print(n)    
print('循环整个结束')