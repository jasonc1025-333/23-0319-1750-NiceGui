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

_debug_Show_Priority_Hi_Bool = True


###jwc o scoreboard_BotsAll_ArrayList_2D = [[]]
scoreboard_BotsAll_ArrayList_2D = [[0,0,0]]
scoreboard_BotSingle_ArrayList_1D = []

_debug_Show_Priority_Hi_Bool = True

line_plot = ui.line_plot(n=2, limit=20, figsize=(3, 2), update_every=5) \
    .with_legend(['sin', 'cos'], loc='upper center', ncol=2)

def update_line_plot() -> None:

    x,y1,y2 = 0, 0, 0

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

        ###jwc o network_DataNew_Message_Str = x
        network_DataNew_Message_Str = str(x)
        ##jwc workaround for '\r\n' tail
        network_DataNew_Message_Str = network_DataNew_Message_Str[0:len(network_DataNew_Message_Str)-10]

        if _debug_Show_Priority_Hi_Bool:
            ###jwc o print replaced by 'print'
            print("* A")
            print("> " + str(network_DataNew_Message_Str))
        if True:
            scoreboard_DataNumNew_ArrayList = []
            scoreboard_DataStrNew_ArrayList = network_DataNew_Message_Str.split("|")
            for value in scoreboard_DataStrNew_ArrayList:
                ###jwc o value22 = value.substr(value.index_of(":") + 1, len(value))
                ###jwc o value22 = value[value.index_of(":") + 1:len(value)]
                value22 = value[value.index(":") + 1:len(value)]
                scoreboard_DataNumNew_ArrayList.append(int(value22))
                if _debug_Show_Priority_Hi_Bool:
                    print("* B")
                    print(value)
                    print(value22)
                    print("" + str((scoreboard_DataNumNew_ArrayList[len(scoreboard_DataNumNew_ArrayList) - 1])))
                    print(scoreboard_DataNumNew_ArrayList)

        if True:
            scoreboard_Bot_Found_Bool = False
            index2 = 0

            ###jwc o while index2 <= len(scoreboard_BotsAll_ArrayList_2D) - 1:
            while index2 < len(scoreboard_BotsAll_ArrayList_2D) - 1:
                scoreboard_BotSingle_ArrayList_1D = scoreboard_BotsAll_ArrayList_2D[index2]

                print("*** DEBUG")
                print(scoreboard_BotsAll_ArrayList_2D)
                print(scoreboard_BotSingle_ArrayList_1D)

                if scoreboard_BotSingle_ArrayList_1D[0] == scoreboard_DataNumNew_ArrayList[0]:
                    scoreboard_Bot_Found_Bool = True
                    ###jwc o index22 = 0
                    ###jwc o while index22 <= len(scoreboard_BotSingle_ArrayList_1D) - 1:
                    ###jwc o     _codeComment_AsText = "Skip 0th Index: BotId"
                    ###jwc o     if index22 != 0:
                    ###jwc o         if _debug_Show_Priority_Hi_Bool:
                    ###jwc o             print("* C1: " + str(scoreboard_BotSingle_ArrayList_1D[index22]) + " " + str(scoreboard_DataNumNew_ArrayList[index22]))
                    ###jwc o         ## Add the two above
                    ###jwc o         scoreboard_BotSingle_ArrayList_1D[index22] = scoreboard_BotSingle_ArrayList_1D[index22] + scoreboard_DataNumNew_ArrayList[index22]
                    ###jwc o         if _debug_Show_Priority_Hi_Bool:
                    ###jwc o             print("* C2: " + str(scoreboard_BotSingle_ArrayList_1D[index22]))
                    ###jwc o     index22 += 1
                    ###jwc o while index22 <= len(scoreboard_BotSingle_ArrayList_1D) - 1:
                    ###jwc o     if index22 != 0:

                    _codeComment_AsText = "Skip 0th Index: BotId"
                    index22 = 1
                    if _debug_Show_Priority_Hi_Bool:
                        print("* L-: " + str(scoreboard_BotSingle_ArrayList_1D[index22]) + " " + str(scoreboard_DataNumNew_ArrayList[index22]))
                    ## Add the two above
                    scoreboard_BotSingle_ArrayList_1D[index22] = scoreboard_BotSingle_ArrayList_1D[index22] + scoreboard_DataNumNew_ArrayList[index22]
                    if _debug_Show_Priority_Hi_Bool:
                        print("* L+: " + str(scoreboard_BotSingle_ArrayList_1D[index22]))
                    
                    y1 = scoreboard_DataNumNew_ArrayList[index22]
                    
                    index22 += 1

                    if _debug_Show_Priority_Hi_Bool:
                        print("* T-: " + str(scoreboard_BotSingle_ArrayList_1D[index22]) + " " + str(scoreboard_DataNumNew_ArrayList[index22]))
                    ## Add the two above
                    scoreboard_BotSingle_ArrayList_1D[index22] = scoreboard_BotSingle_ArrayList_1D[index22] + scoreboard_DataNumNew_ArrayList[index22]
                    if _debug_Show_Priority_Hi_Bool:
                        print("* T+: " + str(scoreboard_BotSingle_ArrayList_1D[index22]))

                    y2 = scoreboard_DataNumNew_ArrayList[index22]

                index2 += 1
        if not (scoreboard_Bot_Found_Bool):
            scoreboard_BotsAll_ArrayList_2D.append(scoreboard_DataNumNew_ArrayList)
            if _debug_Show_Priority_Hi_Bool:
                print("* D:" + str(scoreboard_BotsAll_ArrayList_2D[len(scoreboard_BotsAll_ArrayList_2D) - 1]) + " " + str(len(scoreboard_BotsAll_ArrayList_2D)))
    

    now = datetime.now()
    x = now.timestamp()
    ###jwc o y1 = np.sin(x)
    ###jwc o y2 = np.cos(x)

    print("*** ***" + str(y1) +" "+ str(y2))
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
