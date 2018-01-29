import pyb
from pyb import UART
from pyb import Pin

M0 = Pin('X1', Pin.IN)#红外1，右前
M1 = Pin('X2', Pin.IN)#红外2，右侧45
M2 = Pin('X3', Pin.IN)#红外3，左侧45
M3 = Pin('X4', Pin.IN)#红外4，左前
N1 = Pin('Y1', Pin.OUT_PP)#L298N,IN1,
N2 = Pin('Y2', Pin.OUT_PP)#L298N,IN2,
N3 = Pin('Y3', Pin.OUT_PP)#L298N,IN3,
N4 = Pin('Y4', Pin.OUT_PP)#L298N,IN4,

print('while')
while True:
    print('while')
    pyb.LED(4).off()
    pyb.LED(3).off()
    pyb.LED(2).off()
    if(M0.value()==1):#检测到物体返回0。
        pyb.LED(4).on()
        pyb.delay(50)
        N1.low()
        N2.high()
        N3.low()
        N4.high()
        pyb.delay(30)
        #pyb.delay(5000)
    if(M3.value()==1):#检测到物体返回0。
        pyb.LED(3).on()
        pyb.delay(50)
        N1.high()
        N2.low()
        N3.high()
        N4.low()
        pyb.delay(30)
    if(M2.value()&M1.value()==1):
        pyb.LED(2).on()
        N1.low()
        N2.high()
        N3.high()
        N4.low()
        pyb.delay(70)
