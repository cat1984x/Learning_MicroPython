led = pyb.LED(4)
intensity = 0 #LED 亮度
while True:
    intensity = (intensity + 1) % 255 
    led.intensity(intensity) #只对LED4,LED3有效，能改变亮度
    pyb.delay(20)
