import  pyb,sdcard ,os
#连接SD卡模块到SPI1,cs为A4脚，注意VCC需要接到5V,3.3将无法打开文件目录

sd= sdcard.SDCard(pyb.SPI(1),pyb.Pin('A4'))

pyb.mount(sd,'/sd2')
os.listdir('/')


#在终端中运行os.listdir('/sd2')，可以打开SD卡的文件目录
