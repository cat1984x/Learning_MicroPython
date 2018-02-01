import pyb
from pyb import UART
from pyb import Pin
from pyb import Timer
from pyb import ExtInt

''' 电机驱动模块'''

#电机驱动管脚定义
left_motor1 = Pin('Y1', Pin.OUT_PP)#L298N,IN1 左侧电机1
left_motor2 = Pin('Y2', Pin.OUT_PP)#L298N,IN2 左侧电机2
right_motor1 = Pin('Y4', Pin.OUT_PP)#L298N,IN3,右侧电机1,前后反向，所以交换Y4,Y3定义
right_motor2 = Pin('Y3', Pin.OUT_PP)#L298N,IN4,右侧电机2

global left_motor_forward_flag #左电机正转标志位
global right_motor_forward_flag #右电机正转标志位
left_motor_forward_flag = 1 #赋值
right_motor_forward_flag = 1 #赋值


#设置电机PWM调速定时器
tim1 = Timer(1 , freq=125)
left_pwm = 0
right_pwm = 0

#设置左电机PWM通道，PWM_INVERTED时候占空比0-100为高电平比例
left_channel = tim1.channel(1, Timer.PWM_INVERTED, pin = Pin('Y6'))

#设置右电机PWM通道
right_channel = tim1.channel(2, Timer.PWM_INVERTED, pin = Pin('Y7'))

#左侧电机正转：
def left_motor_forward(left_pwm = 60):#默认PWM参数为60
    global left_motor_forward_flag
    left_motor_forward_flag = 1 #正转为1
    left_motor1.high()
    left_motor2.low()
    left_channel.pulse_width_percent(left_pwm)
    
#左侧电机反转：
def left_motor_reverse(left_pwm = 60):#默认PWM参数为60
    global left_motor_forward_flag
    left_motor_forward_flag = 0 #反转为0
    left_motor1.low()
    left_motor2.high()
    left_channel.pulse_width_percent(left_pwm)
    
#左侧电机停止：    
def left_motor_stop():
    left_motor1.high()
    left_motor2.high()

#右侧电机正转：
def right_motor_forward(right_pwm = 60):#默认PWM参数为60
    global right_motor_forward_flag
    right_motor_forward_flag = 1 #正转为1
    right_motor1.high()
    right_motor2.low()
    right_channel.pulse_width_percent(right_pwm)
    
#右侧电机正转：
def right_motor_reverse(right_pwm = 60):#默认PWM参数为60
    global right_motor_forward_flag
    right_motor_forward_flag = 0 #反转为0
    right_motor1.low()
    right_motor2.high()
    right_channel.pulse_width_percent(right_pwm)

#右侧电机停止：    
def right_motor_stop():
    right_motor1.high()
    right_motor2.high()


'''编码器模块'''

#码盘一圈20格

global left_encoder #声明全局变量，左电机码盘脉冲值
global right_encoder #声明全局变量，右电机码盘脉冲值
left_encoder = 0 #赋值
right_encoder =0 #赋值

#左编码器中断函数
def callback_left_encoder(line): 
    global left_encoder #再次声明，表示这里使用是全局变量
    global left_motor_forward_flag
    if left_motor_forward_flag: #判断正反转
        left_encoder += 1
    else:
        left_encoder -=1
    print("left_encoder=", left_encoder)
    
#右编码器中断函数    
def callback_right_encoder(line): 
    global right_encoder #再次声明，表示这里使用是全局变量
    global right_motor_forward_flag
    if right_motor_forward_flag: #判断正反转
        right_encoder += 1
    else:
        right_encoder -=1
    print("right_encoder=", right_encoder)

#定义左侧编码器中断
extint10 = pyb.ExtInt(Pin("B10"), ExtInt.IRQ_FALLING, pyb.Pin.PULL_UP,
    callback_left_encoder)  #左侧编码器中断，Y9脚

extint15 = pyb.ExtInt(Pin("B15"), ExtInt.IRQ_FALLING, pyb.Pin.PULL_UP,
    callback_right_encoder)  #右侧侧编码器中断，Y8脚
'''
中断使用：
extint = pyb.ExtInt(pin, mode, pull, callback)
中断行0-15，可以映射到任意端口，中断行0映射到Px0，x可以是A/B/C,中断行1映射到Px1，x可以是A/B/C，以此类推
pin 用来开启中断的IO口；
mode 外部中断模式，可以取值：ExtInt.IRQ_RISING 上升沿，ExtInt.IRQ_FALLING 下降沿，ExtInt.IRQ_RISING_FALLING 上升下降沿
pull 定义端口的上拉或下来电阻，可取值：pyb.Pin.PULL_NONE 无上下拉，pyb.Pin.PULL_UP 上拉，pyb.Pin.PULL_DOWN 下拉；
callback 回调函数，只能有一个变量，就是中断行
'''




