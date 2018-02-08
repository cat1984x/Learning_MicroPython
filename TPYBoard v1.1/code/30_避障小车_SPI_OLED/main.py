import pyb
from pyb import Pin
from machine import SPI
from ssd1306 import SSD1306_SPI

#软件驱动SPI
#Y10接D0脚(SCK)时钟线，Y11接D1脚(MOSI)数据线,Y12(MISO)悬空未接
#这个OLED屏的通信协议是一个没有MISO只有MOSI的SPI协议
#针脚定义：
#GND
#VCC,2.8-5.5V
#D0时钟脚
#D1数据脚
#RES复位脚
#DC数据/命令选择脚，DC这个引脚是单片机控制OLED写入命令还是数据，因为它的数据线和命令线共用一根线MOSI即主机输出从机接收端口
#即通过SPI连接MCU和OLED，DC接MCU，如果要向OLED写入命令，拉高DC，如果要向OLED写入数据，拉低DC
#CS片选线脚，6脚的OLED默认接地，可以不接。

spi = SPI(-1,baudrate=10000000, polarity=0, phase=0, sck=Pin('Y10'), 
    mosi=Pin('Y11'),miso=Pin('Y12')) #-1为自定义管脚，定义SPI对应的管脚

#定义OLED管脚
oled = SSD1306_SPI(128,64,spi,dc=Pin('X17'), res=Pin('X18'), cs=Pin('X19'))

oled.poweron()
oled.init_display()
oled.text("Hello chen",0,0)
oled.framebuf.hline(0,12,110,1)
oled.show()
