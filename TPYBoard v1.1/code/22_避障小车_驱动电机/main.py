import pyb
from pyb import UART
from pyb import Pin

#管脚定义

left_motor1 = Pin('Y1', Pin.OUT_PP)#L298N,IN1,
left_motor2 = Pin('Y2', Pin.OUT_PP)#L298N,IN2,
right_motor1 = Pin('Y4', Pin.OUT_PP)#L298N,IN3,右侧前后反向，所以交换Y4,Y3定义
right_motor2 = Pin('Y3', Pin.OUT_PP)#L298N,IN4,

'''
连接电脑，打开超级终端
确定左右电机及其转动方向是否正确
如果不正确，则修改接线或者管脚定义
左侧向前：
left_motor1.high()
left_motor2.low()
左侧向后：
left_motor1.low()
left_motor2.high()
左侧停止：
left_motor1.high()
left_motor2.high()
左侧停止：
left_motor1.low()
left_motor2.low()

右侧向前：
right_motor1.high()
right_motor2.low()
左侧向后：
right_motor1.low()
right_motor2.high()
右侧停止：
right_motor1.high()
right_motor2.high()
右侧停止：
right_motor1.low()
right_motor2.low()
'''
