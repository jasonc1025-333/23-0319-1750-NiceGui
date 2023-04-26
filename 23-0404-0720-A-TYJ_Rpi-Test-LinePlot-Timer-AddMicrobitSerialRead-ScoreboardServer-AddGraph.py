import numpy as np
from numpy.random import random

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

y1Value = [0,0,0]
y2Value = [0,0,0]

###jwc n scoreboard_BotsAll_StringFull_ArrayList_2D =[{'#':0,'l':1,'m':2},{'#':10,'l':11,'m':12},{'#':20,'l':21,'m':22}]

_debug_Show_Priority_Hi_Bool = True

###jwc o line_plot = ui.line_plot(n=2, limit=20, figsize=(3, 2), update_every=5) \
###jwc o     .with_legend(['sin', 'cos'], loc='upper center', ncol=2)

###jwc every 1 sec
    ###jwc y .with_legend(['Light', 'Temp'], loc='upper center', ncol=2)
line_plot = ui.line_plot(n=2, limit=40, figsize=(6, 4), update_every=1) \
    .with_legend(['Light', 'Magnet'], loc='upper center', ncol=2)

def update_line_plot() -> None:

    now,x,y1,y2 = 0, 0, 0, 0

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
            print("* A: Raw String: ")
            print("> " + str(network_DataNew_Message_Str))
        if True:
            scoreboard_DataNumNew_ArrayList = []
            ###jwc y scoreboard_DataStrNew_ArrayList = network_DataNew_Message_Str.split("|")
            scoreboard_DataStrNew_ArrayList = network_DataNew_Message_Str.split(",")

            for value in scoreboard_DataStrNew_ArrayList:
                ###jwc o value22 = value.substr(value.index_of(":") + 1, len(value))
                ###jwc o value22 = value[value.index_of(":") + 1:len(value)]
                value22 = value[value.index(":") + 1:len(value)]
                scoreboard_DataNumNew_ArrayList.append(int(value22))
                if _debug_Show_Priority_Hi_Bool:
                    print("* B: Parsed Key:Value:")
                    print(value)
                    print(value22)
                    print("" + str((scoreboard_DataNumNew_ArrayList[len(scoreboard_DataNumNew_ArrayList) - 1])))
                    print(scoreboard_DataNumNew_ArrayList)

        if True:
            scoreboard_Bot_Found_Bool = False
            index2 = 0

            ###jwc o while index2 <= len(scoreboard_BotsAll_ArrayList_2D) - 1:
            while index2 <= len(scoreboard_BotsAll_ArrayList_2D) - 1:
                scoreboard_BotSingle_ArrayList_1D = scoreboard_BotsAll_ArrayList_2D[index2]

                print("*** DEBUG")
                print(scoreboard_BotsAll_ArrayList_2D)
                print(scoreboard_BotSingle_ArrayList_1D)
                print(scoreboard_DataNumNew_ArrayList)

                if scoreboard_DataNumNew_ArrayList[0] == scoreboard_BotSingle_ArrayList_1D[0]:
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
                    y1Value[index2] = scoreboard_BotSingle_ArrayList_1D[index22]
                    print('>>>  y1Value[index2]:' + str(y1Value[index2]))
                    

                    index22 += 1

                    if _debug_Show_Priority_Hi_Bool:
                        print("* M-: " + str(scoreboard_BotSingle_ArrayList_1D[index22]) + " " + str(scoreboard_DataNumNew_ArrayList[index22]))
                    ## Add the two above
                    scoreboard_BotSingle_ArrayList_1D[index22] = scoreboard_BotSingle_ArrayList_1D[index22] + scoreboard_DataNumNew_ArrayList[index22]
                    if _debug_Show_Priority_Hi_Bool:
                        print("* M+: " + str(scoreboard_BotSingle_ArrayList_1D[index22]))

                    y2 = scoreboard_DataNumNew_ArrayList[index22]
                    y2Value[index2] = scoreboard_BotSingle_ArrayList_1D[index22]
                    print('>>> y2Value[index2]:' + str(y2Value[index2]))


                    now = datetime.now()
                    x = now.timestamp()
                    ###jwc o y1 = np.sin(x)
                    ###jwc o y2 = np.cos(x)
                    
                    ###jwc y print("*** ***" + str(y1) +" "+ str(y2))
                    ###jwc y line_plot.push([now], [[y1], [y2]])  
                    
                ###jwc n scoreboard_BotsAll_StringFull_ArrayList_2D[index2] = x            

                index2 += 1
        if not (scoreboard_Bot_Found_Bool):
            scoreboard_BotsAll_ArrayList_2D.append(scoreboard_DataNumNew_ArrayList)
            if _debug_Show_Priority_Hi_Bool:
                print("* NewBotAdd:" + str(scoreboard_BotsAll_ArrayList_2D[len(scoreboard_BotsAll_ArrayList_2D) - 1]) + " " + str(len(scoreboard_BotsAll_ArrayList_2D)))
        

        ###jwc n prints twice: 2nd 0: now = datetime.now()
        ###jwc n prints twice: 2nd 0: x = now.timestamp()
        ###jwc n prints twice: 2nd 0: ###jwc o y1 = np.sin(x)
        ###jwc n prints twice: 2nd 0: ###jwc o y2 = np.cos(x)
        ###jwc n prints twice: 2nd 0: 
        ###jwc n prints twice: 2nd 0: print("*** ***" + str(y1) +" "+ str(y2))
        ###jwc n prints twice: 2nd 0: line_plot.push([now], [[y1], [y2]])

    ###jwc 23-0423-2050 ? w = datetime.now()
    ###jwc 23-0423-2050 ? = now.timestamp()
    ###jwc 23-0423-2050 ? #jwc o y1 = np.sin(x)
    ###jwc 23-0423-2050 ? #jwc o y2 = np.cos(x)

    ###jwc 23-0423-2050 ? int("*** ***" + str(y1Value[1]) +" "+ str(y1Value[2]))
    ###jwc 23-0423-2050 ? ne_plot.push([now], [[y1Value[1]], [y1Value[2]]])  


def update_line_plot_02() -> None:
    now = datetime.now()

    print(">>> >>> " + str(y2Value[1]) +" "+ str(y2Value[2]) +": "+str(y2Value))
    line_plot.push([now.timestamp()], [[y2Value[1]], [y2Value[2]]])  


###jwc o line_updates = ui.timer(0.1, update_line_plot, active=False)
###jwc timer x2 speed: 0.1 to 0.05
###jwc o line_updates = ui.timer(0.05, update_line_plot, active=False)
line_updates = ui.timer(0.05, update_line_plot, active=True)
line_checkbox = ui.checkbox('active').bind_value(line_updates, 'active')

line_updates_02 = ui.timer(0.1, update_line_plot_02, active=True)


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


grid = ui.aggrid({
    'columnDefs': [
        {'headerName': 'Name', 'field': 'name'},
        {'headerName': 'Age', 'field': 'age'},
        {'headerName': 'Weight', 'field': 'weight'},
    ],
    ###jwc n 'rowData': [
    ###jwc n     scoreboard_BotsAll_StringFull_ArrayList_2D[0],
    ###jwc n     scoreboard_BotsAll_StringFull_ArrayList_2D[1],
    ###jwc n     scoreboard_BotsAll_StringFull_ArrayList_2D[2],
    ###jwc n ],
    'rowData': [
        {'name': 'Alice', 'age': 10, 'weight':100},
        {'name': 'Bob', 'age': 20, 'weight':200},
        {'name': 'Carol', 'age': 30, 'weight':300},
    ],
    'rowSelection': 'multiple',
}).classes('max-h-40')

def updateGrid():
    ###jwc n grid.options[
    ###jwc n     'rowData': [
    ###jwc n     {'name': 'Alice', 'age': 28},
    ###jwc n     {'name': 'Bob', 'age': 31},
    ###jwc n     {'name': 'Carol', 'age': 52},
    ###jwc n]] 
    ###jwc y grid.options['rowData'][0]['age'] += 1
    grid.options['rowData'][1]['age'] += 1
    ###jwc n grid.options['rowData']['Carol']['age'] = random(9)
    grid.options['rowData'][2]['weight'] += 2

    grid.update()

ui.button('Update', on_click=updateGrid)
ui.button('Select all', on_click=lambda: grid.call_api_method('selectAll'))


###jwc n def update_table():
###jwc n     rows = [
###jwc n         {'name': 'Alice', 'age': random(9)},
###jwc n         {'name': 'Bob', 'age': random(9)},
###jwc n         {'name': 'Carol'},
###jwc n     ]


###jwc n columns = [
###jwc n     {'name': 'name', 'label': 'Name', 'field': 'name', 'required': True, 'align': 'left'},
###jwc n     {'name': 'age', 'label': 'Age', 'field': 'age', 'sortable': True},
###jwc n ]
###jwc n rows = [
###jwc n     {'name': 'Alice', 'age': 18},
###jwc n     {'name': 'Bob', 'age': 21},
###jwc n     {'name': 'Carol'},
###jwc n ]
###jwc n ###jwc n table_updates = ui.timer(0.05, update_table, active=True)
###jwc n 
###jwc n ui.table(columns=columns, rows=rows, row_key='name')


ui.run()
