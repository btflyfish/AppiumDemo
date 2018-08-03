import math
#计算圆面积
def cal_Area(x=3):
    return(3.14159*x*x)
#计算圆球体积，先空出来
def cal_Volume(x):
    pass
#计算坐标值，根据三角函数
def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny

print('常见内置函数的使用')
print(abs(-10))
tmp_1=['Python',123]
print(all(tmp_1))
print(bytes(tmp_1[0],encoding='utf-8'))
print(str(b'\xe7\x8e\x8b',encoding='utf-8'))
print(pow(2,5))
print(hex(654))
print('计算圆面积，先输入半径：')
r=int(input())
print('圆面积为：%.2f'%cal_Area(r))
print('半径取默认值3')
print('圆面积为：%.2f'%cal_Area())
print('输出三角函数的使用')
r=move(100,100,60,math.pi/6)
print(r)



