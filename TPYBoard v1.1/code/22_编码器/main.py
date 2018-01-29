tim = pyb.Timer(4)
tim.init(freq=10000)
tim.callback(encoder())
