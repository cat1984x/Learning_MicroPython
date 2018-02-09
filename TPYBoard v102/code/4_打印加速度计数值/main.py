# main.py -- put your code here!
from pyb import Accel
accel = Accel()

while True:
    print(accel.x(), accel.y(), accel.z(), accel.tilt())
    pyb.delay(50)
