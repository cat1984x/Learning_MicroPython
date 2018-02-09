from pyb import ADC

#连接陀螺仪输出到X1脚
gyro= ADC(pyb.Pin.cpu.A0)
while True:
    print(gyro.read())
    pyb.delay(100)
