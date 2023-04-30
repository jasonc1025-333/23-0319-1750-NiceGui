import numpy as np
from numpy.random import random

from datetime import datetime
from nicegui import ui

import time
import serial
from datetime import datetime

import random

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

###jwc n scoreboard_BotsAll_StringFull_ArrayList_2D =[{'#':0,'l':1,'m':2},{'#':10,'l':11,'m':12},{'#':20,'l':21,'m':22}]


_debug_Show_Priority_Hi_Bool = True

###jwc o line_plot = ui.line_plot(n=2, limit=20, figsize=(3, 2), update_every=5) \
###jwc o     .with_legend(['sin', 'cos'], loc='upper center', ncol=2)

###jwc every 1 sec
    ###jwc y .with_legend(['Light', 'Temp'], loc='upper center', ncol=2)
line_plot = ui.line_plot(n=2, limit=40, figsize=(6, 4), update_every=1) \
    .with_legend(['Light', 'Magnet'], loc='upper center', ncol=2)

def update_line_plot() -> None:

    now,network_DataMessage_Rcvd_Bytes,y1,y2 = 0, 0, 0, 0

    network_DataMessage_Rcvd_Bytes = ser.readline()
    if network_DataMessage_Rcvd_Bytes:
        dt = datetime.now()
        datestamp = str(dt)[:16]
        ###jwc o temp, light = network_DataMessage_Rcvd_Bytes.decode().split(':')
        ###jwc 23-0310-1120 y id, te, li, co = network_DataMessage_Rcvd_Bytes.decode().split(',')
        ###jwc n id, te, li, co, m1, m2, m3, m4 = network_DataMessage_Rcvd_Bytes.decode().split('|')
    
        ###jwc o newData = [datestamp,temp,light]
        ###jwc 23-0310-1120 y newData = [datestamp, id, te, li, co]
        ###jwc n newData = [datestamp, id, te, li, co, m1, m2, m3, m4]
        newData = [datestamp, network_DataMessage_Rcvd_Bytes]
    
        print(newData)

        ###jwc o network_DataMessage_Rcvd_Str = network_DataMessage_Rcvd_Bytes
        network_DataMessage_Rcvd_Str = str(network_DataMessage_Rcvd_Bytes)
        ##jwc workaround for '\r\n' tail
        network_DataMessage_Rcvd_Str = network_DataMessage_Rcvd_Str[0:len(network_DataMessage_Rcvd_Str)-10]

        if _debug_Show_Priority_Hi_Bool:
            ###jwc o print replaced by 'print'
            print("* A: Raw String: ")
            print("> " + str(network_DataMessage_Rcvd_Str))
        if True:
            scoreboard_DataNumNew_ArrayList = []
            ###jwc y scoreboard_DataStrNew_ArrayList = network_DataMessage_Rcvd_Str.split("|")
            scoreboard_DataStrNew_ArrayList = network_DataMessage_Rcvd_Str.split(",")

            for key_Value_Pair in scoreboard_DataStrNew_ArrayList:
                ###jwc o key_Value_Pair__Value = key_Value_Pair.substr(key_Value_Pair.index_of(":") + 1, len(key_Value_Pair))
                ###jwc o key_Value_Pair__Value = key_Value_Pair[key_Value_Pair.index_of(":") + 1:len(key_Value_Pair)]
                ## * Skip past "b'" prefix
                key_Value_Pair__Key = key_Value_Pair[2 : key_Value_Pair.index(":")-1]
                key_Value_Pair__Value = key_Value_Pair[key_Value_Pair.index(":") + 1:len(key_Value_Pair)]
                scoreboard_DataNumNew_ArrayList.append(int(key_Value_Pair__Value))
                if _debug_Show_Priority_Hi_Bool:
                    print("* B: Parsed Key:key_Value_Pair:")
                    print(key_Value_Pair, key_Value_Pair__Key, key_Value_Pair__Value)
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
                    network_DataMessage_Rcvd_Bytes = now.timestamp()
                    ###jwc o y1 = np.sin(network_DataMessage_Rcvd_Bytes)
                    ###jwc o y2 = np.cos(network_DataMessage_Rcvd_Bytes)
                    
                    ###jwc y print("*** ***" + str(y1) +" "+ str(y2))
                    ###jwc y line_plot.push([now], [[y1], [y2]])  
                    
                ###jwc n scoreboard_BotsAll_StringFull_ArrayList_2D[index2] = network_DataMessage_Rcvd_Bytes            

                index2 += 1
        if not (scoreboard_Bot_Found_Bool):
            scoreboard_BotsAll_ArrayList_2D.append(scoreboard_DataNumNew_ArrayList)
            if _debug_Show_Priority_Hi_Bool:
                print("* NewBotAdd:" + str(scoreboard_BotsAll_ArrayList_2D[len(scoreboard_BotsAll_ArrayList_2D) - 1]) + " " + str(len(scoreboard_BotsAll_ArrayList_2D)))
        

        ###jwc n prints twice: 2nd 0: now = datetime.now()
        ###jwc n prints twice: 2nd 0: network_DataMessage_Rcvd_Bytes = now.timestamp()
        ###jwc n prints twice: 2nd 0: ###jwc o y1 = np.sin(network_DataMessage_Rcvd_Bytes)
        ###jwc n prints twice: 2nd 0: ###jwc o y2 = np.cos(network_DataMessage_Rcvd_Bytes)
        ###jwc n prints twice: 2nd 0: 
        ###jwc n prints twice: 2nd 0: print("*** ***" + str(y1) +" "+ str(y2))
        ###jwc n prints twice: 2nd 0: line_plot.push([now], [[y1], [y2]])

    ###jwc 23-0423-2050 ? w = datetime.now()
    ###jwc 23-0423-2050 ? = now.timestamp()
    ###jwc 23-0423-2050 ? #jwc o y1 = np.sin(network_DataMessage_Rcvd_Bytes)
    ###jwc 23-0423-2050 ? #jwc o y2 = np.cos(network_DataMessage_Rcvd_Bytes)

    ###jwc 23-0423-2050 ? int("*** ***" + str(y1Value[1]) +" "+ str(y1Value[2]))
    ###jwc 23-0423-2050 ? ne_plot.push([now], [[y1Value[1]], [y1Value[2]]])  


def update_line_plot_02() -> None:
    now = datetime.now()

    print(">>> >>> " + str(y2Value[1]) +" "+ str(y2Value[2]) +": "+str(y2Value))
    line_plot.push([now.timestamp()], [[y2Value[1]], [y2Value[2]]])  


###jwc o line_updates = ui.timer(0.1, update_line_plot, active=False)
###jwc timer x2 speed: 0.1 to 0.05
###jwc o line_updates = ui.timer(0.05, update_line_plot, active=False)
## '0.05' sec
###jwc good for slow real-time y line_updates = ui.timer(0.05, update_line_plot, active=True)
###jwc y no more linegraph real-time to test chart realtime instead, 
###jwc TYJ LINE GRAPH DID SEEM TO SLOW DOWN TEXTCHART/DISPLAY BY 10-20 SEC :)+
line_updates = ui.timer(0.05, update_line_plot, active=False)
line_checkbox = ui.checkbox('active').bind_value(line_updates, 'active')

## '0.1' sec
### jwc ym line_updates_02 = ui.timer(0.1, update_line_plot_02, active=True)


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
##jwc n network_DataMessage_Rcvd_Bytes=ser.readline()
##jwc n if network_DataMessage_Rcvd_Bytes:
##jwc n     dt = datetime.now()
##jwc n     datestamp = str(dt)[:16]
##jwc n     ###jwc o temp, light = network_DataMessage_Rcvd_Bytes.decode().split(':')
##jwc n     ###jwc 23-0310-1120 y id, te, li, co = network_DataMessage_Rcvd_Bytes.decode().split(',')
##jwc n     ###jwc n id, te, li, co, m1, m2, m3, m4 = network_DataMessage_Rcvd_Bytes.decode().split('|')
##jwc n 
##jwc n     ###jwc o newData = [datestamp,temp,light]
##jwc n     ###jwc 23-0310-1120 y newData = [datestamp, id, te, li, co]
##jwc n     ###jwc n newData = [datestamp, id, te, li, co, m1, m2, m3, m4]
##jwc n     newData = [datestamp, network_DataMessage_Rcvd_Bytes]
##jwc n     print(newData)
##jwc n 


###jwc o grid = ui.aggrid({
###jwc o     'columnDefs': [
###jwc o         {'headerName': 'Name', 'field': 'name'},
###jwc o         {'headerName': 'Age', 'field': 'age'},
###jwc o         {'headerName': 'Weight', 'field': 'weight'},
###jwc o     ],
###jwc o     ###jwc n 'rowData': [
###jwc o     ###jwc n     scoreboard_BotsAll_StringFull_ArrayList_2D[0],
###jwc o     ###jwc n     scoreboard_BotsAll_StringFull_ArrayList_2D[1],
###jwc o     ###jwc n     scoreboard_BotsAll_StringFull_ArrayList_2D[2],
###jwc o     ###jwc n ],
###jwc o     'rowData': [
###jwc o         {'name': 'Alice', 'age': 10, 'weight':100},
###jwc o         {'name': 'Bob', 'age': 20, 'weight':200},
###jwc o         {'name': 'Carol', 'age': 30, 'weight':300},
###jwc o     ],
###jwc o     'rowSelection': 'multiple',
###jwc o }).classes('max-h-40')

dictionary_Scoreboard_BotsAll_Ids = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]

###jwc n dictionary_Scoreboard_BotsAll_Value_Default = {'botid':'', 'light_lastdelta':'', 'light_total':'', 'magnet_lastdelta':'', 'magnet_total':''},
dictionary_Scoreboard_BotsAll_Value_Default = {'botid':0, 'light_lastdelta':0, 'light_total':0, 'magnet_lastdelta':0, 'magnet_total':0},

###jwc n    'rowData' : dict.fromkeys( dictionary_Scoreboard_BotsAll_Ids, dictionary_Scoreboard_BotsAll_Value_Default),

###jwc n rowData' :[
###jwc n         {1:dictionary_Scoreboard_BotsAll_Value_Default},
###jwc n         {2:dictionary_Scoreboard_BotsAll_Value_Default},
###jwc n         {3:dictionary_Scoreboard_BotsAll_Value_Default},
###jwc n     ],

    ###jwc y 'rowData' :[
    ###jwc y     {'row#':1, 'botid':11, 'light_lastdelta':12, 'light_total':13, 'magnet_lastdelta':14, 'magnet_total':15},
    ###jwc y     {'row#':2, 'botid':21, 'light_lastdelta':22, 'light_total':23, 'magnet_lastdelta':24, 'magnet_total':25},
    ###jwc y     {'row#':3, 'botid':31, 'light_lastdelta':32, 'light_total':33, 'magnet_lastdelta':34, 'magnet_total':35},    
    ###jwc y ],

###jwc n rowData_Details =
###jwc n     {
###jwc n         '1': {'botid':11, 'light_lastdelta':12, 'light_total':13, 'magnet_lastdelta':14, 'magnet_total':15},
###jwc n         '2': {'botid':21, 'light_lastdelta':22, 'light_total':23, 'magnet_lastdelta':24, 'magnet_total':25},
###jwc n         '3': {'botid':31, 'light_lastdelta':32, 'light_total':33, 'magnet_lastdelta':34, 'magnet_total':35},
###jwc n     }

###jwc n     'rowData' : rowData_Details,
###jwc n rowData_Details = {
###jwc n     {'row#':1, 'botid':11, 'light_lastdelta':12, 'light_total':13, 'magnet_lastdelta':14, 'magnet_total':15},
###jwc n     {'row#':2, 'botid':21, 'light_lastdelta':22, 'light_total':23, 'magnet_lastdelta':24, 'magnet_total':25},
###jwc n     {'row#':3, 'botid':31, 'light_lastdelta':32, 'light_total':33, 'magnet_lastdelta':34, 'magnet_total':35},    
###jwc n }

grid = ui.aggrid({
    'columnDefs': [
        {'headerName': 'Row#', 'field': 'row#'},
        {'headerName': 'BotId', 'field': 'botid'},
        {'headerName': 'Light_LastDelta', 'field': 'light_lastdelta'},
        {'headerName': 'Light_Total', 'field': 'light_total'},
        {'headerName': 'Magnet_LastDelta', 'field': 'magnet_lastdelta'},
        {'headerName': 'Magnet_Total', 'field': 'magnet_total'},
    ],
    'rowData' :[
        {'row#':1, 'botid':11, 'light_lastdelta':12, 'light_total':13, 'magnet_lastdelta':14, 'magnet_total':15},
        {'row#':2, 'botid':21, 'light_lastdelta':22, 'light_total':23, 'magnet_lastdelta':24, 'magnet_total':25},
        {'row#':3, 'botid':31, 'light_lastdelta':32, 'light_total':33, 'magnet_lastdelta':34, 'magnet_total':35},    
    ],
    'rowSelection': 'multiple',
}).classes('max-h-40')


    ###jwc y grid.options['rowData'][1]['age'] += 1
    ###jwc y grid.options['rowData'][2]['weight'] += 2

tenp1 = 5
temp2 = 1


def updateGrid():
    ###jwc n grid.options[
    ###jwc n     'rowData': [
    ###jwc n     {'name': 'Alice', 'age': 28},
    ###jwc n     {'name': 'Bob', 'age': 31},
    ###jwc n     {'name': 'Carol', 'age': 52},
    ###jwc n]] 
    ###jwc y grid.options['rowData'][0]['age'] += 1
    grid.options['rowData'][0]['magnet_lastdelta'] += temp2
    grid.options['rowData'][0]['magnet_total'] += temp2
    grid.options['rowData'][1]['light_lastdelta'] += random.randint(1,100)
    ###jwc n grid.options['rowData']['Carol']['age'] = random(9)
    grid.options['rowData'][2]['light_total'] += random.randint(1,100)

    grid.update()

ui.button('Update', on_click=updateGrid)
ui.button('Select all', on_click=lambda: grid.call_api_method('selectAll'))

## '0.05' sec update
###jwc y update_Grid = ui.timer(0.05, updateGrid, active=True)
update_Grid = ui.timer(1, updateGrid, active=True)

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
