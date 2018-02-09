# main.py -- put your code here!
led = pyb.LED(2) #定义led为LED2
while True:
    led.toggle() #开关LED
    pyb.delay(1000) #延时1s
