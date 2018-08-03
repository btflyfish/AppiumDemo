from PIL import Image,ImageDraw
from PIL import ImageFilter
from PIL import ImageFont
import random
im=Image.open('Images/test.jpg')
w,h=im.size
print('原始尺寸是%s,%s'%(w,h))
im.thumbnail((w//2,h//2))
print('缩放后尺寸是%s,%s'%(w//2,h//2))
im.save('Images/test1.jpg','jpeg')
#应用模糊效果
im2=im.filter(ImageFilter.BLUR)
im2.save('Images/testBlur.jpg','jpeg')
#生成字母验证码图片
#随机字母
def rndChar():
    return chr(random.randint(65,90))
#随机颜色1
def rndColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
#随机颜色2
def rndColor2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))
#定义图像大小宽度和高度
width=60*4
height=60
#创建1个图像
image=Image.new('RGB',(width,height),(255,255,255))
#创建Font对象
font1=ImageFont.truetype('arial.ttf',36)
#创建Draw对象
draw=ImageDraw.Draw(image)
#填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=rndColor())
#输出文字
for t in range(4):
    draw.text((60*t+10,10),rndChar(),font=font1,fill=rndColor2())
#模糊
image=image.filter(ImageFilter.BLUR)
image.save('Images/code.jpg','jpeg')