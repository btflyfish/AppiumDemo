L1=[x*x for x in range(11)]
G1=(x*x for x in range(11))
print(L1)
print(G1)
print('使用next函数依次输出生成器前4个元素的值')
print(next(G1),next(G1),next(G1),next(G1))
print('使用for循环输出生成器各个元素的值')
for g1 in G1:
    print(g1,end=' ')
