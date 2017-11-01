import network
from machine import Pin
sta_if = network.WLAN(network.STA_IF)
p2 = Pin(2, Pin.OUT)
#我们在这里把接入点接口禁用，方便观看实验效果，非实验可以去掉
sta_if.active(False)
if not sta_if.isconnected():
        p2.off()
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('', '')
        while not sta_if.isconnected():
                pass
if sta_if.isconnected():
        print('connect success')
        p2.on()
        print('network config:', sta_if.ifconfig())
