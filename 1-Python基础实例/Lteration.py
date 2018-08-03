#查找列表中的最大值和最小值,直接使用List中函数
def findMinAndMax(L):  
    if L:        
        return(min(L),max(L))
    else:
        return(None,None)
#定义列表和元组以及字典
list1=['北京','上海','深圳','广州']
tuper1=('武汉','南京','天津')
dict1={'北京薪水':20000,'杭州薪水':15000,'武汉薪水':10000,'包头薪水':5000}
print('迭代列表')
for l1 in list1:
    print(l1,end=' ')
print()
print('迭代元组')
for t1 in tuper1:
    print(t1,end=' ')
print()
print('迭代字典key的值')
for d1 in dict1:
    print(d1)
print('迭代字典value的值')
for v1 in dict1.values():
    print(v1)
print('迭代字典key,value的值')
for k2,v2 in dict1.items():
    print(k2,v2)
print('测试列表最大值和最小值函数')
if findMinAndMax([])!=(None,None):
    print('测试findMinAndMax([])失败!')
elif findMinAndMax([7,5,6,9])!=(5,9):
    print('测试findMinAndMax([7,5,6,9])失败!')
elif findMinAndMax([7,6])!=(6,7):
    print('测试findMinAndMax([7,6])失败!')
elif findMinAndMax([18,11,14,12,13])!=(11,18):
    print('测试findMinAndMax([18,11,14,12,13])失败！')
elif findMinAndMax([7])!=(7,7):
    print('测试findMinAndMax([7])失败！')
else:
    print('测试成功')
