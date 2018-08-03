L1=list(range(1,11))
#循环从1到10
L2=[x*x for x in range(1,11)]
#还可以加if判断
L3=[x*x for x in range(1,11) if x%2==0]
#还可以使用双层循环
L4=[m+n for m in 'ABC' for n in 'XYZ']
L5=['Hello','Python',19,'Apple',None]
#isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。 
L6=[str.lower(x)  for x in L5 if isinstance(x,str)]
print('输出List生成式的值:',L1)
print('输出List生成式的值:',L2)
print('输出List生成式的值:',L3)
print('输出List生成式的值:',L4)
print(L5,'字符串转小写',L6)