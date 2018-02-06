import pyb
import select

def pass_through(usb, uart):
    usb.setinterrupt(-1)
    while True:
        select.select([usb, uart], [], [])
        if usb.any():
            uart.write(usb.read(256))
        if uart.any():
            usb.write(uart.read(256))
            
#使用串口1（X9、X10）连接CP2102,连接电脑使用XCOM打开CP2102
#使用超级终端打开PYBOARD，使用XCOM打开PYBOARD可以发送但无法接收
pass_through(pyb.USB_VCP(), pyb.UART(1, 115200, timeout=0))
