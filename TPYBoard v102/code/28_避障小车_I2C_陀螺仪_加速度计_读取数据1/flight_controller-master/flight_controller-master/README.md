# flight_controller
A stabilization system for drones using a pyboard, for educational purposes.

The main.py is based is this link:
http://owenson.me/build-your-own-quadcopter-autopilot/ 

The mpu6050.py is a modified version from here:
https://github.com/cTn-dev/PyComms/tree/master/MPU6050

The pid.py is based from here: 
https://github.com/diydrones/ardupilot 

To receive the PWM from the RC receiver, I took the code from here: 
http://wiki.micropython.org/platforms/boards/pyboard/modpyb/Timer-Examples 

To control the speed controls, I take the code from here:
https://hackaday.io/project/6877-micropython-quadruped-robot


The actual code for the pyboard are divided in 5 scripts:

rc.py -> read pwm from receiver

esc.py -> send pwm to speeds

mpu.py -> read accelerometer and gyroscope

pid.py -> stabilize the multicopter

main.py -> joins all scripts

And 1 script for the simulator on the laptop:

MPUTeapot.py

Now I'm working with the telemetry