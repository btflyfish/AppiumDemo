#定义该文档的作者，公开源代码后能看到大名
__author__='Simon'
import sys
def test():
    args=sys.argv
    if len(args)==1:
        print('Hello World!')
    elif len(args)==2:
        print('Hello,%s!'%args[1])
    else:
        print('太多参数！')
#定义两个私有函数
def __private__1(name):
    return 'Hello,%s!'%name
def __private__2(name):
    return 'Hi,%s!'%name
#定义一个共有函数greeting
def greeting(name):    
    if len(name)>=5:
        print(__private__1(name))     
    else:
        print(__private__2(name))
#调用test函数
if __name__=='__main__':
    test()
#调用greeting函数
greeting('Simon')
greeting('John')