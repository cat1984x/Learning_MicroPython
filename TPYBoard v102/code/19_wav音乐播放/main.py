import wave
from pyb import DAC
dac = DAC(1)

#连接X5(PA4)到耳机左或右声道，GND到耳机的地，声音可能比较小
while True:
    f = wave.open('test.wav')
    dac.write_timed(f.readframes(f.getnframes()), f.getframerate())
    pyb.delay(1000)
