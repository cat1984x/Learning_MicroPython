import math
hid = pyb.USB_HID()

def osc(n,d):
    for i in range(n):
        hid.send((0, int(20 * math.sin(2*math.pi*i/100)), 0, 0))
        pyb.delay(d)

osc(100,50)
