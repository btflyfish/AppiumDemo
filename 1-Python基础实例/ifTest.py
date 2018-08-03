print('请输入体重(KG)：')
weight=int(input())
print('请输入身高（CM）')
height=int(input())
bmi=round((weight*10000)/(height*height),2)
print('身高{0}CM，体重{1}KG，BMI是{2}'.format(height,weight,bmi))
if bmi<18.5:
    print('过轻，要增肥')
elif bmi<25:
    print('正常')
elif bmi<=28:
    print('过重')
elif bmi<=32:
    print('肥胖')
else:
    print('严重肥胖')
print('请输入2018年期望年收入(万元)：')
salary=int(input())
if salary<3:
    print('2018年吃土，家里蹲')
elif salary<=6:
    print('2018年窘迫，包头周边游')
elif salary<=9:
    print('2018年温饱，国内背包游')
elif salary<=12:
    print('2018年小康,国内度假游')
else:
    print('2018年富裕，海外度假游')