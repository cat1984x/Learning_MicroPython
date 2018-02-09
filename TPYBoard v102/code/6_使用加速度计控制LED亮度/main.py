# main.py -- put your code here!
from pyb import Accel
accel = pyb.Accel() 
led = pyb.LED(4) #蓝灯
intensity = 0 #LED亮度，值为0到255


while True:
    x = accel.x() #返回值为-30到30
    intensity = int(abs(x)/30*255) #int取整
    led.intensity(intensity)
    pyb.delay(100)
