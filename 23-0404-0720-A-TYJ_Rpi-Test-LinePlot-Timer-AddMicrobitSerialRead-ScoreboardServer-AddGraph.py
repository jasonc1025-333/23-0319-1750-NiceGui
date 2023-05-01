import numpy as np
from numpy.random import random as random_Numpy

from datetime import datetime
from nicegui import ui

import time
import serial
from datetime import datetime

import random as random_General


# array of dictionary
#
rowData_List = [
    {'row_base0_num':0, 'bot_id':11, 'light_lastdelta':12, 'light_total':13, 'magnet_lastdelta':14, 'magnet_total':15},
    {'row_base0_num':1, 'bot_id':21, 'light_lastdelta':22, 'light_total':23, 'magnet_lastdelta':24, 'magnet_total':25},
    {'row_base0_num':2, 'bot_id':31, 'light_lastdelta':32, 'light_total':33, 'magnet_lastdelta':34, 'magnet_total':35},    
    {'row_base0_num':3, 'bot_id':41, 'light_lastdelta':42, 'light_total':43, 'magnet_lastdelta':44, 'magnet_total':45},    
]

    ###jwc y {'row_base0_num':1, 'bot_id':11, 'light_lastdelta':110, 'light_total':1100, 'magnet_lastdelta':11000, 'magnet_total':110000},
rowData_ArrayList_OfDictionaryPairs_ForEachBot = [
    # 'row_base0_num=0 & bot_id=0' for testing purpposes
    {'row_base0_num':0, 'bot_id':0, 'light_lastdelta':100, 'light_total':1000, 'magnet_lastdelta':10000, 'magnet_total':100000},
]

rowData_OfDictionaryPairs_ForABot_Empty = {
    'row_base0_num':0, 'bot_id':0, 'light_lastdelta':0, 'light_total':0, 'magnet_lastdelta':0, 'magnet_total':0,
    }


scoreboard_DataMessage_Recvd_Dict = {}

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
        ###jwc o temp, light = network_DataMessage_Rcvd_Bytes.decode().split(':')
        ###jwc 23-0310-1120 y id, te, li, co = network_DataMessage_Rcvd_Bytes.decode().split(',')
        ###jwc n id, te, li, co, m1, m2, m3, m4 = network_DataMessage_Rcvd_Bytes.decode().split('|')
    
        ###jwc o newData = [datestamp,temp,light]
        ###jwc 23-0310-1120 y newData = [datestamp, id, te, li, co]
        ###jwc n newData = [datestamp, id, te, li, co, m1, m2, m3, m4]

        ###jwc o not neeeded: dt = datetime.now()
        ###jwc o not neeeded: datestamp = str(dt)[:16]
        ###jwc o not neeeded: newData = [datestamp, network_DataMessage_Rcvd_Bytes]
        ###jwc o not neeeded: print(newData)

        ###jwc o network_DataMessage_Rcvd_Str = network_DataMessage_Rcvd_Bytes
        network_DataMessage_Rcvd_Str = str(network_DataMessage_Rcvd_Bytes)
        ##jwc workaround for '\r\n' tail
        ##jwc y network_DataMessage_Rcvd_Str = network_DataMessage_Rcvd_Str[0:len(network_DataMessage_Rcvd_Str)-10]
        ###jwc n network_DataMessage_Rcvd_Str = network_DataMessage_Rcvd_Str[0:network_DataMessage_Rcvd_Str.index("\\r\\n")]
        ###jwc n network_DataMessage_Rcvd_Str = network_DataMessage_Rcvd_Str.rstrip("\r\n")
        ###jwc n network_DataMessage_Rcvd_Str = network_DataMessage_Rcvd_Str.strip()
        ###jwc n network_DataMessage_Rcvd_02_Str = network_DataMessage_Rcvd_Str.strip()
        ###jwc n network_DataMessage_Rcvd_02_Str = network_DataMessage_Rcvd_Str.rstrip()
        ###jwc n network_DataMessage_Rcvd_02_Str = network_DataMessage_Rcvd_Str.rstrip("\r\n")
        ###jwc n network_DataMessage_Rcvd_02_Str = network_DataMessage_Rcvd_Str.rstrip("\\r\\n")
        ###jwc n network_DataMessage_Rcvd_02_Str = network_DataMessage_Rcvd_Str.rstrip("\\\r\\\n")
        ###jwc n network_DataMessage_Rcvd_02_Str = network_DataMessage_Rcvd_Str.replace("\r\n","")

        ## ':-5' though only 4 length: '\r\n'
        network_DataMessage_Rcvd_Str = network_DataMessage_Rcvd_Str[:-5]
        ## Remove trailing spaces from both sides
        network_DataMessage_Rcvd_Str = network_DataMessage_Rcvd_Str.strip()
        network_DataMessage_Rcvd_Str = network_DataMessage_Rcvd_Str[network_DataMessage_Rcvd_Str.index("#"):]

        if _debug_Show_Priority_Hi_Bool:
            ###jwc o print replaced by 'print'
            print("* A: Raw String: ")
            ###jwc o print("  A1>" + str(network_DataMessage_Rcvd_Str) +"|")
            print("  1:" + str(network_DataMessage_Rcvd_Str) +"|")
        if True:
            scoreboard_DataNumNew_ArrayList = []
            ###jwc y scoreboard_DataStrNew_ArrayList = network_DataMessage_Rcvd_Str.split("|")
            scoreboard_DataStrNew_ArrayList = network_DataMessage_Rcvd_Str.split(",")

            for key_Value_Pair in scoreboard_DataStrNew_ArrayList:
                ###jwc o key_Value_Pair__Value = key_Value_Pair.substr(key_Value_Pair.index_of(":") + 1, len(key_Value_Pair))
                ###jwc o key_Value_Pair__Value = key_Value_Pair[key_Value_Pair.index_of(":") + 1:len(key_Value_Pair)]
                ## * Skip past "b'" prefix
                ##jwc ? key_Value_Pair__Key = key_Value_Pair[2 : key_Value_Pair.index(":")-1]
                ##jwc n key_Value_Pair__Key = key_Value_Pair[0:key_Value_Pair.index(":")-1]
                key_Value_Pair__Key = key_Value_Pair[key_Value_Pair.index(":")-1 : key_Value_Pair.index(":")]
                ##jwc y key_Value_Pair__Value = key_Value_Pair[key_Value_Pair.index(":") + 1:len(key_Value_Pair)]
                key_Value_Pair__Value = key_Value_Pair[key_Value_Pair.index(":") + 1:len(key_Value_Pair)]
                ##jwc yy scoreboard_DataNumNew_ArrayList.append(int(key_Value_Pair__Value))

                ##jwc n scoreboard_DataNumNew_ArrayList.append({key_Value_Pair__Key:int(key_Value_Pair__Value)})
                
                ### n scoreboard_DataNumNew_ArrayList['A']=int(key_Value_Pair__Value)
                ### scoreboard_DataNumNew_ArrayList.append(int(key_Value_Pair__Value))
                scoreboard_DataMessage_Recvd_Dict[key_Value_Pair__Key]=int(key_Value_Pair__Value)

                if _debug_Show_Priority_Hi_Bool:
                    print("* B: Parsed Key:key_Value_Pair:")
                    print("  1:key_Value_Pair|key_Value_Pair__Key|key_Value_Pair__Value: " + key_Value_Pair +"|"+ key_Value_Pair__Key +"|"+ key_Value_Pair__Value +"|")
                    
                    ###jwc o print("  2:"+ str((scoreboard_DataNumNew_ArrayList[len(scoreboard_DataNumNew_ArrayList) - 1])) +"|")
                    ###jwc o print("  3:"+ str(scoreboard_DataNumNew_ArrayList)
                          
                    print("  2:scoreboard_DataMessage_Recvd_Dict: "+ str(scoreboard_DataMessage_Recvd_Dict) +"|")
                   

        if True:
            scoreboard_Bot_Found_Bool = False
            print("* C")
            print("  C1:" + str(rowData_ArrayList_OfDictionaryPairs_ForEachBot))

            for bot_dictionary in rowData_ArrayList_OfDictionaryPairs_ForEachBot:
                print("  C2:" + str(bot_dictionary))
                if scoreboard_DataMessage_Recvd_Dict['#'] in bot_dictionary.values():
                    scoreboard_Bot_Found_Bool = True    
                    
                    print("  C3a:bot_dictionary: " + str(bot_dictionary))
                    bot_dictionary['magnet_lastdelta']=scoreboard_DataMessage_Recvd_Dict['M']
                    bot_dictionary['magnet_total']+=scoreboard_DataMessage_Recvd_Dict['M']
                    print("  C3b:bot_dictionary: " + str(bot_dictionary))
                    

            ###jwc o index2 = 0

            ###jwc o while index2 <= len(scoreboard_BotsAll_ArrayList_2D) - 1:
            ###jwc o while index2 <= len(scoreboard_BotsAll_ArrayList_2D) - 1:
            ###jwc o     scoreboard_BotSingle_ArrayList_1D = scoreboard_BotsAll_ArrayList_2D[index2]
            ###jwc o 
            ###jwc o     print("* C: DEBUG")
            ###jwc o     ##jwc o print("  1:scoreboard_BotsAll_ArrayList_2D: " + str(scoreboard_BotsAll_ArrayList_2D))
            ###jwc o     ##jwc o print("  2:scoreboard_BotSingle_ArrayList_1D: " + str(scoreboard_BotSingle_ArrayList_1D))
            ###jwc o     ##jwc o print("  3:scoreboard_DataNumNew_ArrayList: " + str(scoreboard_DataNumNew_ArrayList))
            ###jwc o 
            ###jwc o     print("  1:rowData_ArrayList_Of_SingleBot_DictionaryPairs: " + str(rowData_ArrayList_.Of_SingleBot_DictionaryPairs))
            ###jwc o     rowData_ArrayList_Of_SingleBot_DictionaryPairs.index
            ###jwc o 
            ###jwc o     if scoreboard_DataNumNew_ArrayList[0] == scoreboard_BotSingle_ArrayList_1D[0]:
            ###jwc o         scoreboard_Bot_Found_Bool = True
            ###jwc o         ###jwc o index22 = 0
            ###jwc o         ###jwc o while index22 <= len(scoreboard_BotSingle_ArrayList_1D) - 1:
            ###jwc o         ###jwc o     _codeComment_AsText = "Skip 0th Index: BotId"
            ###jwc o         ###jwc o     if index22 != 0:
            ###jwc o         ###jwc o         if _debug_Show_Priority_Hi_Bool:
            ###jwc o         ###jwc o             print("* C1: " + str(scoreboard_BotSingle_ArrayList_1D[index22]) + " " + str(scoreboard_DataNumNew_ArrayList[index22]))
            ###jwc o         ###jwc o         ## Add the two above
            ###jwc o         ###jwc o         scoreboard_BotSingle_ArrayList_1D[index22] = scoreboard_BotSingle_ArrayList_1D[index22] + scoreboard_DataNumNew_ArrayList[index22]
            ###jwc o         ###jwc o         if _debug_Show_Priority_Hi_Bool:
            ###jwc o         ###jwc o             print("* C2: " + str(scoreboard_BotSingle_ArrayList_1D[index22]))
            ###jwc o         ###jwc o     index22 += 1
            ###jwc o         ###jwc o while index22 <= len(scoreboard_BotSingle_ArrayList_1D) - 1:
            ###jwc o         ###jwc o     if index22 != 0:
            ###jwc o 
            ###jwc o         _codeComment_AsText = "Skip 0th Index: BotId"
            ###jwc o         index22 = 1
            ###jwc o         if _debug_Show_Priority_Hi_Bool:
            ###jwc o             ###jwc o print("* L-: " + str(scoreboard_BotSingle_ArrayList_1D[index22]) + " " + str(scoreboard_DataNumNew_ArrayList[index22]))
            ###jwc o             ###jwc ? print("* L-: " + str(scoreboard_BotSingle_ArrayList_1D[index22]) + " " + str(scoreboard_DataNumNew_ArrayList['L']))
            ###jwc o             ## Add the two above
            ###jwc o             ##? scoreboard_BotSingle_ArrayList_1D[index22] = scoreboard_BotSingle_ArrayList_1D[index22] + int(scoreboard_DataNumNew_ArrayList{'L'})
            ###jwc o             print("* L+: " + str(scoreboard_BotSingle_ArrayList_1D[index22]))
            ###jwc o         
            ###jwc o         y1 = scoreboard_DataNumNew_ArrayList[index22]
            ###jwc o         y1Value[index2] = scoreboard_BotSingle_ArrayList_1D[index22]
            ###jwc o         print('>>>  y1Value[index2]:' + str(y1Value[index2]))
            ###jwc o         
            ###jwc o 
            ###jwc o         index22 += 1
            ###jwc o 
            ###jwc o         if _debug_Show_Priority_Hi_Bool:
            ###jwc o             print("* M-: " + str(scoreboard_BotSingle_ArrayList_1D[index22]) + " " + str(scoreboard_DataNumNew_ArrayList[index22]))
            ###jwc o         ## Add the two above
            ###jwc o         scoreboard_BotSingle_ArrayList_1D[index22] = scoreboard_BotSingle_ArrayList_1D[index22] + scoreboard_DataNumNew_ArrayList[index22]
            ###jwc o         if _debug_Show_Priority_Hi_Bool:
            ###jwc o             print("* M+: " + str(scoreboard_BotSingle_ArrayList_1D[index22]))
            ###jwc o 
            ###jwc o         y2 = scoreboard_DataNumNew_ArrayList[index22]
            ###jwc o         y2Value[index2] = scoreboard_BotSingle_ArrayList_1D[index22]
            ###jwc o         print('>>> y2Value[index2]:' + str(y2Value[index2]))
            ###jwc o 
            ###jwc o 
            ###jwc o         now = datetime.now()
            ###jwc o         network_DataMessage_Rcvd_Bytes = now.timestamp()
            ###jwc o         ###jwc o y1 = np.sin(network_DataMessage_Rcvd_Bytes)
            ###jwc o         ###jwc o y2 = np.cos(network_DataMessage_Rcvd_Bytes)
            ###jwc o         
            ###jwc o         ###jwc y print("*** ***" + str(y1) +" "+ str(y2))
            ###jwc o         ###jwc y line_plot.push([now], [[y1], [y2]])  
            ###jwc o         
            ###jwc o     ###jwc n scoreboard_BotsAll_StringFull_ArrayList_2D[index2] = network_DataMessage_Rcvd_Bytes            
            ###jwc o 
            ###jwc o     index2 += 1
            
            print("* D")
            if not (scoreboard_Bot_Found_Bool):
                ##jwc o scoreboard_BotsAll_ArrayList_2D.append(scoreboard_DataNumNew_ArrayList)
                ##jwc o if _debug_Show_Priority_Hi_Bool:
                ##jwc o     print("* NewBotAdd:" + str(scoreboard_BotsAll_ArrayList_2D[len(scoreboard_BotsAll_ArrayList_2D) - 1]) + " " + str(len(scoreboard_BotsAll_ArrayList_2D)))

                rowData_OfDictionaryPairs_ForABot_Empty['row_base0_num'] = len(rowData_ArrayList_OfDictionaryPairs_ForEachBot)
                rowData_OfDictionaryPairs_ForABot_Empty['bot_id'] = scoreboard_DataMessage_Recvd_Dict['#']
                rowData_OfDictionaryPairs_ForABot_Empty['magnet_lastdelta'] = scoreboard_DataMessage_Recvd_Dict['M']
                rowData_OfDictionaryPairs_ForABot_Empty['magnet_total'] = 0


                print("  D1aa:" + str(rowData_ArrayList_OfDictionaryPairs_ForEachBot))
                print("  D1ab:" + str(rowData_OfDictionaryPairs_ForABot_Empty))
                rowData_ArrayList_OfDictionaryPairs_ForEachBot.append(rowData_OfDictionaryPairs_ForABot_Empty)
                print("  D1b:" + str(rowData_ArrayList_OfDictionaryPairs_ForEachBot))


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
    ###jwc n update_line_plot
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
###jwc y line_updates = ui.timer(0.05, update_line_plot, active=False)
line_updates = ui.timer(1, update_line_plot, active=True)
line_checkbox = ui.checkbox('active').bind_value(line_updates, 'active')

## '0.1' sec
### jwc ym line_updates_02 = ui.timer(0.1, update_line_plot_02, active=True)
###jwc 23-0501-1400 yy line_updates_02 = ui.timer(2, update_line_plot_02, active=True)


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

    ###jwc yy 'rowData' :[
    ###jwc yy     {'row#':1, 'botid':11, 'light_lastdelta':12, 'light_total':13, 'magnet_lastdelta':14, 'magnet_total':15},
    ###jwc yy     {'row#':2, 'botid':21, 'light_lastdelta':22, 'light_total':23, 'magnet_lastdelta':24, 'magnet_total':25},
    ###jwc yy     {'row#':3, 'botid':31, 'light_lastdelta':32, 'light_total':33, 'magnet_lastdelta':34, 'magnet_total':35},    
    ###jwc yy ],

###jwc y ## tuple (static) but prefer dict (dynamic) since latter more flexile, extnedible 
###jwc y rowData_List = (
###jwc y     {'row#':1, 'botid':11, 'light_lastdelta':12, 'light_total':13, 'magnet_lastdelta':14, 'magnet_total':15},
###jwc y     {'row#':2, 'botid':21, 'light_lastdelta':22, 'light_total':23, 'magnet_lastdelta':24, 'magnet_total':25},
###jwc y     {'row#':3, 'botid':31, 'light_lastdelta':32, 'light_total':33, 'magnet_lastdelta':34, 'magnet_total':35},    
###jwc y     {'row#':4, 'botid':41, 'light_lastdelta':42, 'light_total':43, 'magnet_lastdelta':44, 'magnet_total':45},    
###jwc y )

###jwc yy ## array of dictionary
###jwc yy ##
###jwc yy rowData_List = [
###jwc yy     {'row#':1, 'botid':11, 'light_lastdelta':12, 'light_total':13, 'magnet_lastdelta':14, 'magnet_total':15},
###jwc yy     {'row#':2, 'botid':21, 'light_lastdelta':22, 'light_total':23, 'magnet_lastdelta':24, 'magnet_total':25},
###jwc yy     {'row#':3, 'botid':31, 'light_lastdelta':32, 'light_total':33, 'magnet_lastdelta':34, 'magnet_total':35},    
###jwc yy     {'row#':4, 'botid':41, 'light_lastdelta':42, 'light_total':43, 'magnet_lastdelta':44, 'magnet_total':45},    
###jwc yy ]

## list
##
###jwc ? rowData_List = [
###jwc ?     {
###jwc ?         0 : {'botid':11, 'light_lastdelta':12, 'light_total':13, 'magnet_lastdelta':14, 'magnet_total':15},
###jwc ?         1 : {'botid':21, 'light_lastdelta':22, 'light_total':23, 'magnet_lastdelta':24, 'magnet_total':25},
###jwc ?         2 : {'botid':31, 'light_lastdelta':32, 'light_total':33, 'magnet_lastdelta':34, 'magnet_total':35},    
###jwc ?         3 : {'botid':41, 'light_lastdelta':42, 'light_total':43, 'magnet_lastdelta':44, 'magnet_total':45},
###jwc ?     }
###jwc ? ]
###jwc yn legal db, but fails for web, blank chart: ## nested dictionary
###jwc yn legal db, but fails for web, blank chart: ##
###jwc yn legal db, but fails for web, blank chart: rowData_List = {
###jwc yn legal db, but fails for web, blank chart:         0 : {'botid':11, 'light_lastdelta':12, 'light_total':13, 'magnet_lastdelta':14, 'magnet_total':15},
###jwc yn legal db, but fails for web, blank chart:         1 : {'botid':21, 'light_lastdelta':22, 'light_total':23, 'magnet_lastdelta':24, 'magnet_total':25},
###jwc yn legal db, but fails for web, blank chart:         2 : {'botid':31, 'light_lastdelta':32, 'light_total':33, 'magnet_lastdelta':34, 'magnet_total':35},    
###jwc yn legal db, but fails for web, blank chart:         3 : {'botid':41, 'light_lastdelta':42, 'light_total':43, 'magnet_lastdelta':44, 'magnet_total':45},
###jwc yn legal db, but fails for web, blank chart:     }
###jwc n ##
###jwc n ##
###jwc n rowData_List = [
###jwc n         0 : {'botid':11, 'light_lastdelta':12, 'light_total':13, 'magnet_lastdelta':14, 'magnet_total':15},
###jwc n         1 : {'botid':21, 'light_lastdelta':22, 'light_total':23, 'magnet_lastdelta':24, 'magnet_total':25},
###jwc n         2 : {'botid':31, 'light_lastdelta':32, 'light_total':33, 'magnet_lastdelta':34, 'magnet_total':35},    
###jwc n         3 : {'botid':41, 'light_lastdelta':42, 'light_total':43, 'magnet_lastdelta':44, 'magnet_total':45},
###jwc n ]

###jwc n ##
###jwc n ##
###jwc n rowData_List = [
###jwc n         {0 : {'botid':11, 'light_lastdelta':12, 'light_total':13, 'magnet_lastdelta':14, 'magnet_total':15}},
###jwc n         {1 : {'botid':21, 'light_lastdelta':22, 'light_total':23, 'magnet_lastdelta':24, 'magnet_total':25}},
###jwc n         {2 : {'botid':31, 'light_lastdelta':32, 'light_total':33, 'magnet_lastdelta':34, 'magnet_total':35}},    
###jwc n         {3 : {'botid':41, 'light_lastdelta':42, 'light_total':43, 'magnet_lastdelta':44, 'magnet_total':45}},
###jwc n ]
###jwc n ##
###jwc n ##
###jwc n rowData_List = {
###jwc n         {0 : {'botid':11, 'light_lastdelta':12, 'light_total':13, 'magnet_lastdelta':14, 'magnet_total':15}},
###jwc n         {1 : {'botid':21, 'light_lastdelta':22, 'light_total':23, 'magnet_lastdelta':24, 'magnet_total':25}},
###jwc n         {2 : {'botid':31, 'light_lastdelta':32, 'light_total':33, 'magnet_lastdelta':34, 'magnet_total':35}},    
###jwc n         {3 : {'botid':41, 'light_lastdelta':42, 'light_total':43, 'magnet_lastdelta':44, 'magnet_total':45}},
###jwc n     }
## nested dictionary
##
###jwc n rowData_List = (
###jwc n         {0 : {'botid':11, 'light_lastdelta':12, 'light_total':13, 'magnet_lastdelta':14, 'magnet_total':15}},
###jwc n         {1 : {'botid':21, 'light_lastdelta':22, 'light_total':23, 'magnet_lastdelta':24, 'magnet_total':25}},
###jwc n         {2 : {'botid':31, 'light_lastdelta':32, 'light_total':33, 'magnet_lastdelta':34, 'magnet_total':35}},    
###jwc n         {3 : {'botid':41, 'light_lastdelta':42, 'light_total':43, 'magnet_lastdelta':44, 'magnet_total':45}},
###jwc n )


###jwc y }).classes('max-h-40')
###jwc y }).classes('max-h-80')
###jwc ? }).classes('max-h-500')
###jwc ? }).classes('max-h-full')
###jwc y }).classes('max-h-[128rem]')
###jwc y }).classes('h-[128rem]')

###jwc 23-0501-1500 yy    'rowData' : rowData_List,

###jwc 23-0501-1520        {'headerName': 'Row#', 'field': 'row#'},
###jwc 23-0501-1520        {'headerName': 'BotId', 'field': 'botid'},
###jwc 23-0501-1520        {'headerName': 'Light_LastDelta', 'field': 'light_lastdelta'},
###jwc 23-0501-1520        {'headerName': 'Light_Total', 'field': 'light_total'},
###jwc 23-0501-1520        {'headerName': 'Magnet_LastDelta', 'field': 'magnet_lastdelta'},
###jwc 23-0501-1520        {'headerName': 'Magnet_Total', 'field': 'magnet_total'},

grid = ui.aggrid({
    'columnDefs': [
        {'headerName': 'Row_Base0_Num', 'field': 'row_base0_num'},
        {'headerName': 'Bot_Id', 'field': 'bot_id'},
        {'headerName': 'Light_LastDelta', 'field': 'light_lastdelta'},
        {'headerName': 'Light_Total', 'field': 'light_total'},
        {'headerName': 'Magnet_LastDelta', 'field': 'magnet_lastdelta'},
        {'headerName': 'Magnet_Total', 'field': 'magnet_total'},
    ],
    'rowData' : rowData_ArrayList_OfDictionaryPairs_ForEachBot,
    'rowSelection': 'multiple',
# Defaults to 'h-64'
# 1 rem = 16px, 2 rem = 1 full font height     
}).classes('h-[128rem]')


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
    ###jwc yy grid.options['rowData'][0]['magnet_lastdelta'] += temp2
    grid.options['rowData'][0]['magnet_lastdelta'] += temp2
    grid.options['rowData'][0]['magnet_total'] += temp2
    grid.options['rowData'][0]['light_lastdelta'] += random_General.randint(1,100)
    ###jwc n grid.options['rowData']['Carol']['age'] = random_Numpy(9)
    grid.options['rowData'][0]['light_total'] += random_General.randint(1,100)

    grid.update()


def updateGrid02():
    rowData_List[0]['light_lastdelta']+=1
    rowData_List[0]['light_total']+=rowData_List[0]['light_lastdelta']
    rowData_List[0]['magnet_lastdelta']+=2
    rowData_List[0]['magnet_total']+=rowData_List[1]['magnet_lastdelta']
    rowData_List.append({'row_base0_num':5, 'bot_id':51, 'light_lastdelta':52, 'light_total':53, 'magnet_lastdelta':54, 'magnet_total':55})


ui.button('Update', on_click=updateGrid)
ui.button('Update02', on_click=updateGrid02)
ui.button('Select all', on_click=lambda: grid.call_api_method('selectAll'))

## '0.05' sec update
###jwc y update_Grid = ui.timer(0.05, updateGrid, active=True)
update_Grid = ui.timer(1, updateGrid, active=True)

###jwc n def update_table():
###jwc n     rows = [
###jwc n         {'name': 'Alice', 'age': random_Numpy(9)},
###jwc n         {'name': 'Bob', 'age': random_Numpy(9)},
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
