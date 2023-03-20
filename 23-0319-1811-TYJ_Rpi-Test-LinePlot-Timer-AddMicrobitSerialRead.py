import numpy as np
from datetime import datetime
from nicegui import ui

import time
import serial
from datetime import datetime

ser = serial.Serial(
        ##jwc o port='/dev/ttyACM0',
        ##jwc o port='COM3',
        port='/dev/ttyACM0',
        baudrate = 115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

line_plot = ui.line_plot(n=2, limit=20, figsize=(3, 2), update_every=5) \
    .with_legend(['sin', 'cos'], loc='upper center', ncol=2)

def update_line_plot() -> None:

    x=ser.readline()
    if x:
        dt = datetime.now()
        datestamp = str(dt)[:16]
        ###jwc o temp, light = x.decode().split(':')
        ###jwc 23-0310-1120 y id, te, li, co = x.decode().split(',')
        ###jwc n id, te, li, co, m1, m2, m3, m4 = x.decode().split('|')
    
        ###jwc o newData = [datestamp,temp,light]
        ###jwc 23-0310-1120 y newData = [datestamp, id, te, li, co]
        ###jwc n newData = [datestamp, id, te, li, co, m1, m2, m3, m4]
        newData = [datestamp, x]
    
        print(newData)

    now = datetime.now()
    x = now.timestamp()
    y1 = np.sin(x)
    y2 = np.cos(x)
    line_plot.push([now], [[y1], [y2]])

line_updates = ui.timer(0.1, update_line_plot, active=False)
line_checkbox = ui.checkbox('active').bind_value(line_updates, 'active')

##jwc n ser = serial.Serial(
##jwc n         ##jwc o port='/dev/ttyACM0',
##jwc n         port='COM3',
##jwc n         baudrate = 115200,
##jwc n         parity=serial.PARITY_NONE,
##jwc n         stopbits=serial.STOPBITS_ONE,
##jwc n         bytesize=serial.EIGHTBITS,
##jwc n         timeout=1
##jwc n )

##jwc n ##jwc READ ONCE AND PRINTED ONCE THEN SAME 'NO PERMISSION FAIL'
##jwc n x=ser.readline()
##jwc n if x:
##jwc n     dt = datetime.now()
##jwc n     datestamp = str(dt)[:16]
##jwc n     ###jwc o temp, light = x.decode().split(':')
##jwc n     ###jwc 23-0310-1120 y id, te, li, co = x.decode().split(',')
##jwc n     ###jwc n id, te, li, co, m1, m2, m3, m4 = x.decode().split('|')
##jwc n 
##jwc n     ###jwc o newData = [datestamp,temp,light]
##jwc n     ###jwc 23-0310-1120 y newData = [datestamp, id, te, li, co]
##jwc n     ###jwc n newData = [datestamp, id, te, li, co, m1, m2, m3, m4]
##jwc n     newData = [datestamp, x]
##jwc n     print(newData)
##jwc n 

ui.run()
