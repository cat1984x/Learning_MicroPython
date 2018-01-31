import pyb
from pyb import UART
from pyb import Pin
from pyb import Timer

#管脚定义

left_motor1 = Pin('Y1', Pin.OUT_PP)#L298N,IN1
left_motor2 = Pin('Y2', Pin.OUT_PP)#L298N,IN2
right_motor1 = Pin('Y4', Pin.OUT_PP)#L298N,IN3,右侧前后反向，所以交换Y4,Y3定义
right_motor2 = Pin('Y3', Pin.OUT_PP)#L298N,IN4


#需要使用定时器来开启PWM，定时器有1-14，相应管脚与定时器的对应可以参考pyborad管脚图
#其中定时器2、3、5、6已被系统使用，一般不建议再使用。
#我们选择定时器1下面的Y6,Y7脚，分别是通道1，通道2
#相同定时器下的PWM频率都是相同的，但可以分别设置不同占空比
#PWM控制频率与具体的电机特性有关，不是越高越好，也不是越低越好
#这里设置为125，后续可做实验寻找最优频率
#Y6接到L298N上的ENA，左侧电机使能脚
#Y7接到L298N上的ENB，右侧电机使能脚

tim1 = Timer(1 , freq=125)
left_pwm = 0
right_pwm = 0
#设置左电机PWM通道，PWM_INVERTED时候占空比0-100为高电平比例
left_channel = tim1.channel(1, Timer.PWM_INVERTED, pin = Pin('Y6'))
#设置右电机PWM通道
right_channel = tim1.channel(2, Timer.PWM_INVERTED, pin = Pin('Y7'))

#开启左侧电机：
left_motor1.high()
left_motor2.low()

#开启右侧电机：
right_motor1.high()
right_motor2.low()

'''
连接电脑终端，开启左右电机，并调节占空比，观察电机转速
测试占空比有效范围
左侧电机：
left_channel.pulse_width_percent(50)
右侧电机：
right_channel.pulse_width_percent(50)

测出左侧电机45启动
右侧电机50启动

'''
