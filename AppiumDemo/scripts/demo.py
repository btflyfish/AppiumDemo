from appium import webdriver
import time
#server启动参数
desired_caps={}
#设备信息安卓手机型号
desired_caps['platformName']='Android'  #设备版本号
desired_caps['platformVersion']='5.1'  #手机系统版本号
desired_caps['deviceName']='192.168.57.103:5555'  #手机或者模拟器类型
#app信息，得到包名和启动名，请查阅文章
# 参阅文章https://www.cnblogs.com/unknows/p/7736965.html
desired_caps['appPackage']='com.android.settings'
desired_caps['appActivity']='.Settings'
#支持中文输入，并且将键盘隐藏起来
desired_caps['UnicodeKeyboard']=True
desired_caps['resetKeyboard']=True
# 声明driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
