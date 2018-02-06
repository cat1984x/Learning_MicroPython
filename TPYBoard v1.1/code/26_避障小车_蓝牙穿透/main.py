import pyb
import select
from pyb import UART


'''定义蓝牙BLE模块连接的串口'''
#使用串口4，蓝牙模块1RX接X1，TX接X2,VCC接VIN，GND接GND
bluetooth = UART(4,115200)
bluetooth.init(115200, bits=8, parity=None, stop=1, timeout=50) #设置串口波特率及等待延时50ms

'''USB虚拟串口'''
usb = pyb.USB_VCP() #创建虚拟串口对象

def pass_through(usb, uart):#使得USB和蓝牙互通
    usb.setinterrupt(-1)#设置中断python运行键，默认是3（Ctrl+C）。-1是禁止中断功能，在需要发送原始字节时需要。
    while True:
        #等待流事件，轮询是在多个对象上等待读/写活动的有效方法。当前支持: pyb.UART，class:pyb.USB_VCP
        select.select([usb, uart], [], []) 
        if usb.any(): #如果缓冲区有数据等待接收，返回True
            uart.write(usb.read(256))#可以执行
        if uart.any():
            #print(uart.read(256))
            usb.write(uart.read(256).decode())#超级终端可以显示，XCOM无法显示

#使用超级终端连接微电脑鼠USB虚拟串口
#另外使用蓝牙模块2接CP2102接到电脑USB，使用蓝牙与蓝牙模块1相连，此端口使用XCOM
#可以看到发送和接收数据
pass_through(usb, bluetooth) #执行函数

#蓝牙模块的设定，需要使用CP2102接到电脑USB，使用XCOM发送AT指令
#蓝牙在未连接模式下，自动进入AT模式，可以使用AT指令设定参数。
#常见AT指令见蓝牙模块手册，JDY-08

#无法使用这里的绑定USB虚拟串口的超级终端来发送AT指令
#“自带的USB虚拟串口”不等于“串口接CP2012转成USB”
#USB虚拟串口与普通串口有比较大区别
#USB虚拟串口实时发送字符到蓝牙模块1

