from pyb import Timer
from time import sleep

# timer 5 will be created with a frequency of 100 Hz
tim = pyb.Timer(5, freq=100)
tchannel = tim.channel(1, Timer.PWM, pin=pyb.Pin.board.X1, pulse_width=0)

# maximum and minimum pulse-width, which corresponds to maximum
# and minimum brightness
max_width = 200000
min_width = 20000

# how much to change the pulse-width by each step
percent=0.01
wstep = 1+percent
cur_width = min_width

while True:
  tchannel.pulse_width(int(cur_width))

  sleep(0.01)
  #人眼对光亮的敏感程度为对数上升，所以要使光强看起来匀速变化需使光强以指数上升
  #使用PWM比ADC能更好的控制LED亮度。
  #因为PWM可保持LED的电流相同;而ADC方式控制，光强与电流变化不成线性关系
  cur_width *= wstep 
  if cur_width > max_width:
    cur_width = max_width
    wstep = 1-percent
  elif cur_width < min_width:
    cur_width = min_width
    wstep = 1+percent
