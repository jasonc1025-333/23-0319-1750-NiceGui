import numpy as np
from numpy.random import random as random_Numpy

from datetime import datetime
from nicegui import ui
from nicegui.events import ValueChangeEventArguments

import time
import serial
from datetime import datetime

import random as random_General
import string


# array of dictionary
#
rowData_Test_List = [
    {'row_id':2, 'bot_id':31, 'light_lastdelta':32, 'light_total':33, 'magnet_lastdelta':34, 'magnet_total':35},    
    {'row_id':3, 'bot_id':41, 'light_lastdelta':42, 'light_total':43, 'magnet_lastdelta':44, 'magnet_total':45},    
    {'row_id':1, 'bot_id':21, 'light_lastdelta':22, 'light_total':23, 'magnet_lastdelta':24, 'magnet_total':25},
    {'row_id':0, 'bot_id':11, 'light_lastdelta':12, 'light_total':13, 'magnet_lastdelta':14, 'magnet_total':15},
]

    ###jwc y {'row_id':1, 'bot_id':11, 'light_lastdelta':110, 'light_total':1100, 'magnet_lastdelta':11000, 'magnet_total':110000},
    ###jwc y {'row_id':1, 'bot_id':14, 'light_lastdelta':110, 'light_total':1100, 'magnet_lastdelta':11000, 'magnet_total':110000},
    # 'row_id=0 & bot_id=0' for testing purpposes

###jwc 23-0504-0700 TYJ rowData_ArrayList_OfDictionaryPairs_ForAllBots = [
###jwc 23-0504-0700 TYJ     {'row_id':'Test_Row', 'bot_id':'Test_Bot', 'light_lastdelta':100, 'light_total':1000, 'magnet_lastdelta':10000, 'magnet_total':100000},
###jwc 23-0504-0700 TYJ ]
rowData_ArrayList_OfDictionaryPairs_ForAllBots = [
    {'row_id':'Test_Row', 'bot_id':'Test_Bot', 'mission_status':'-', 'team_id':'-', 'light_lastdelta':100, 'light_total':1000, 'magnet_lastdelta':10000, 'magnet_total':100000},
]

###jwc global inerferes with .append so move to local: rowData_OfDictionaryPairs_ForABot_Empty = {
###jwc global inerferes with .append so move to local:     'row_id':0, 'bot_id':0, 'light_lastdelta':0, 'light_total':0, 'magnet_lastdelta':0, 'magnet_total':0,
###jwc global inerferes with .append so move to local:     }


scoreboard_DataMessage_Rcvd_Dict = {}

ser = serial.Serial(
        ##jwc o port='/dev/ttyACM0',
        ###jwc y port='/dev/ttyACM1',

        ##jwc o port='COM3',
        port='/dev/ttyACM0',
        baudrate = 115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

###jwc o scoreboard_BotsAll_ArrayList_2D = [[]]
scoreboard_BotsAll_ArrayList_2D = [[0,0,0]]
scoreboard_BotSingle_ArrayList_1D = []

y1Value = [0,0,0]
y2Value = [0,0,0]

###jwc n scoreboard_BotsAll_StringFull_ArrayList_2D =[{'#':0,'l':1,'m':2},{'#':10,'l':11,'m':12},{'#':20,'l':21,'m':22}]

###jwc n scoreboard_BotsAll_StringFull_ArrayList_2D =[{'#':0,'l':1,'m':2},{'#':10,'l':11,'m':12},{'#':20,'l':21,'m':22}]

# Debug Prints
#
###jwc y _debug_Show_Priority_Hi_Bool = True
_debug_Show_Priority_Hi_Bool = True
_debug_Show_Priority_Lo_Bool = False

class update_WebGrid_UiTimer_Initialization_Class:
        def __init__(self):
            ###jwc y self.timer_Sec_Int = 8
            self.timer_Sec_Int = 4
            ###jwc y self.active_Bool = False
            self.active_Bool = True

update_WebGrid_UiTimer_Initialization_Object = update_WebGrid_UiTimer_Initialization_Class()

###jwc n update_WebGrid_UiTimer_Active_Bool = False

bot_TeamAssigned_Base0_Int = [0,0,0]

update_WebGrid_UiTimer_Interval_Sec_Int = 4


###jwc o line_plot = ui.line_plot(n=2, limit=20, figsize=(3, 2), update_every=5) \
###jwc o     .with_legend(['sin', 'cos'], loc='upper center', ncol=2)

### ### jwc yyy tyj: ###jwc every 1 sec
### ### jwc yyy tyj:     ###jwc y .with_legend(['Light', 'Temp'], loc='upper center', ncol=2)
### ### jwc yyy tyj: line_plot = ui.line_plot(n=2, limit=40, figsize=(6, 4), update_every=1) \
### ### jwc yyy tyj:     .with_legend(['Light', 'Magnet'], loc='upper center', ncol=2)

#
# receive_Microbit_Messages_Fn
#
def receive_Microbit_Messages_Fn() -> None:

    now,network_DataMessage_Rcvd_Bytes,y1,y2 = 0, 0, 0, 0

    rowData_OfDictionaryPairs_ForABot_Empty_Local = {
    ###jwc 23-0504-0710 y 'row_id':'A', 'bot_id':0, 'light_lastdelta':0, 'light_total':0, 'magnet_lastdelta':0, 'magnet_total':0,
    'row_id':'A', 'bot_id':0, 'mission_status':'-', 'team_id':'-', 'light_lastdelta':0, 'light_total':0, 'magnet_lastdelta':0, 'magnet_total':0,
    }


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
        
        if _debug_Show_Priority_Hi_Bool:
            print("* A: Raw String: ")
            print("  A1:network_DataMessage_Rcvd_Bytes:" + str(network_DataMessage_Rcvd_Bytes) +"|")

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

        # ':-5' though only 4 length: '\r\n'
        network_DataMessage_Rcvd_Str = network_DataMessage_Rcvd_Str[:-5]
        # Remove trailing spaces from both sides
        network_DataMessage_Rcvd_Str = network_DataMessage_Rcvd_Str.strip()
        # invalid 'network_DataMessage_Rcvd_Str' will be detected here 'ValueError: substring not found' 
        # \ and thus abort and retry w/ new 'network_DataMessage_Rcvd_Str'
        network_DataMessage_Rcvd_Str = network_DataMessage_Rcvd_Str[network_DataMessage_Rcvd_Str.index("#"):]

        ###jwc o if _debug_Show_Priority_Lo_Bool:
        ###jwc o     ###jwc o print replaced by 'print'
        ###jwc o     print("* A: Raw String: ")
        ###jwc o     ###jwc o print("  A1>" + str(network_DataMessage_Rcvd_Str) +"|")
        ###jwc o     print("  1:" + str(network_DataMessage_Rcvd_Str) +"|")
        if _debug_Show_Priority_Hi_Bool:
            print("  A2:network_DataMessage_Rcvd_Str:" + str(network_DataMessage_Rcvd_Str) +"|")

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
                # Add new 'key_Value_Pair'
                scoreboard_DataMessage_Rcvd_Dict[key_Value_Pair__Key]=int(key_Value_Pair__Value)

                if _debug_Show_Priority_Lo_Bool:
                    print("* B: Parsed Key:key_Value_Pair:")
                    print("  1:key_Value_Pair|key_Value_Pair__Key|key_Value_Pair__Value: " + key_Value_Pair +"|"+ key_Value_Pair__Key +"|"+ key_Value_Pair__Value +"|")
                    
                    ###jwc o print("  2:"+ str((scoreboard_DataNumNew_ArrayList[len(scoreboard_DataNumNew_ArrayList) - 1])) +"|")
                    ###jwc o print("  3:"+ str(scoreboard_DataNumNew_ArrayList)
                          
                    print("  2:scoreboard_DataMessage_Recvd_Dict: "+ str(scoreboard_DataMessage_Rcvd_Dict) +"|")
                   

        if True:
            scoreboard_Bot_Found_Bool = False
            if _debug_Show_Priority_Lo_Bool:
                print("* C")
                print("  C1:" + str(rowData_ArrayList_OfDictionaryPairs_ForAllBots))

            for bot_dictionary in rowData_ArrayList_OfDictionaryPairs_ForAllBots:
                if _debug_Show_Priority_Lo_Bool:
                    print("  C2:" + str(bot_dictionary))
                ###jwc y? if scoreboard_DataMessage_Rcvd_Dict['#'] in bot_dictionary.values():
                if scoreboard_DataMessage_Rcvd_Dict['#'] == bot_dictionary['bot_id']:
    
                    scoreboard_Bot_Found_Bool = True    
                    
                    if _debug_Show_Priority_Hi_Bool:
                        print("  C3a:bot_dictionary: " + str(bot_dictionary))
                    bot_dictionary['light_lastdelta'] = scoreboard_DataMessage_Rcvd_Dict['L']
                    bot_dictionary['light_total'] += scoreboard_DataMessage_Rcvd_Dict['L']
                    bot_dictionary['magnet_lastdelta'] = scoreboard_DataMessage_Rcvd_Dict['M']
                    bot_dictionary['magnet_total'] += scoreboard_DataMessage_Rcvd_Dict['M']
                    if _debug_Show_Priority_Hi_Bool:
                        print("  C3b:bot_dictionary: " + str(bot_dictionary))
                    

            
            if _debug_Show_Priority_Lo_Bool:
                print("* D")
            if not (scoreboard_Bot_Found_Bool):
                ##jwc o scoreboard_BotsAll_ArrayList_2D.append(scoreboard_DataNumNew_ArrayList)
                ##jwc o if _debug_Show_Priority_Lo_Bool:
                ##jwc o     print("* NewBotAdd:" + str(scoreboard_BotsAll_ArrayList_2D[len(scoreboard_BotsAll_ArrayList_2D) - 1]) + " " + str(len(scoreboard_BotsAll_ArrayList_2D)))

                # base_0 needed for letter
                rowData_OfDictionaryPairs_ForABot_Empty_Local['row_id'] = chr( ord('A') + (len(rowData_ArrayList_OfDictionaryPairs_ForAllBots) ) -1 )


                rowData_OfDictionaryPairs_ForABot_Empty_Local['bot_id'] = scoreboard_DataMessage_Rcvd_Dict['#']
                rowData_OfDictionaryPairs_ForABot_Empty_Local['light_lastdelta'] = scoreboard_DataMessage_Rcvd_Dict['L']
                rowData_OfDictionaryPairs_ForABot_Empty_Local['light_total'] += scoreboard_DataMessage_Rcvd_Dict['L']
                rowData_OfDictionaryPairs_ForABot_Empty_Local['magnet_lastdelta'] = scoreboard_DataMessage_Rcvd_Dict['M']
                rowData_OfDictionaryPairs_ForABot_Empty_Local['magnet_total'] += scoreboard_DataMessage_Rcvd_Dict['M']


                if _debug_Show_Priority_Hi_Bool:
                    print("  D1aa:" + str(rowData_ArrayList_OfDictionaryPairs_ForAllBots))
                    print("  D1ab:" + str(rowData_OfDictionaryPairs_ForABot_Empty_Local))
                rowData_ArrayList_OfDictionaryPairs_ForAllBots.append(rowData_OfDictionaryPairs_ForABot_Empty_Local)
                if _debug_Show_Priority_Hi_Bool:
                    print("  D1b:" + str(rowData_ArrayList_OfDictionaryPairs_ForAllBots))
    else:
        print("*** No Serial Read *** ")


### ### jwc yyy tyj: def update_line_plot_02() -> None:
### ### jwc yyy tyj:     ###jwc n receive_Microbit_Messages_Fn
### ### jwc yyy tyj:     now = datetime.now()
### ### jwc yyy tyj: 
### ### jwc yyy tyj:     print(">>> >>> " + str(y2Value[1]) +" "+ str(y2Value[2]) +": "+str(y2Value))
### ### jwc yyy tyj:     line_plot.push([now.timestamp()], [[y2Value[1]], [y2Value[2]]])  



###jwc test only: done: dictionary_Scoreboard_BotsAll_Ids = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
###jwc test only: done: 
###jwc test only: done: ###jwc n dictionary_Scoreboard_BotsAll_Value_Default = {'botid':'', 'light_lastdelta':'', 'light_total':'', 'magnet_lastdelta':'', 'magnet_total':''},
###jwc test only: done: ###jwc 23-0504-0700 y dictionary_Scoreboard_BotsAll_Value_Default = {'botid':0, 'light_lastdelta':0, 'light_total':0, 'magnet_lastdelta':0, 'magnet_total':0},
###jwc test only: done: dictionary_Scoreboard_BotsAll_Value_Default = {'botid':0, 'status':'-', 'team':'-', 'light_lastdelta':0, 'light_total':0, 'magnet_lastdelta':0, 'magnet_total':0},
###jwc test only: done: 
###jwc test only: done: ###jwc n    'rowData' : dict.fromkeys( dictionary_Scoreboard_BotsAll_Ids, dictionary_Scoreboard_BotsAll_Value_Default),

    ###jwc y 'rowData' :[
    ###jwc y     {'row#':1, 'botid':11, 'light_lastdelta':12, 'light_total':13, 'magnet_lastdelta':14, 'magnet_total':15},
    ###jwc y     {'row#':2, 'botid':21, 'light_lastdelta':22, 'light_total':23, 'magnet_lastdelta':24, 'magnet_total':25},
    ###jwc y     {'row#':3, 'botid':31, 'light_lastdelta':32, 'light_total':33, 'magnet_lastdelta':34, 'magnet_total':35},    
    ###jwc y ],

    ###jwc yy 'rowData' :[
    ###jwc yy     {'row#':1, 'botid':11, 'light_lastdelta':12, 'light_total':13, 'magnet_lastdelta':14, 'magnet_total':15},
    ###jwc yy     {'row#':2, 'botid':21, 'light_lastdelta':22, 'light_total':23, 'magnet_lastdelta':24, 'magnet_total':25},
    ###jwc yy     {'row#':3, 'botid':31, 'light_lastdelta':32, 'light_total':33, 'magnet_lastdelta':34, 'magnet_total':35},    
    ###jwc yy ],

###jwc y ## tuple (static) but prefer dict (dynamic) since latter more flexile, extnedible 
###jwc y rowData_Test_List = (
###jwc y     {'row#':1, 'botid':11, 'light_lastdelta':12, 'light_total':13, 'magnet_lastdelta':14, 'magnet_total':15},
###jwc y     {'row#':2, 'botid':21, 'light_lastdelta':22, 'light_total':23, 'magnet_lastdelta':24, 'magnet_total':25},
###jwc y     {'row#':3, 'botid':31, 'light_lastdelta':32, 'light_total':33, 'magnet_lastdelta':34, 'magnet_total':35},    
###jwc y     {'row#':4, 'botid':41, 'light_lastdelta':42, 'light_total':43, 'magnet_lastdelta':44, 'magnet_total':45},    
###jwc y )

###jwc yy ## array of dictionary
###jwc yy ##
###jwc yy rowData_Test_List = [
###jwc yy     {'row#':1, 'botid':11, 'light_lastdelta':12, 'light_total':13, 'magnet_lastdelta':14, 'magnet_total':15},
###jwc yy     {'row#':2, 'botid':21, 'light_lastdelta':22, 'light_total':23, 'magnet_lastdelta':24, 'magnet_total':25},
###jwc yy     {'row#':3, 'botid':31, 'light_lastdelta':32, 'light_total':33, 'magnet_lastdelta':34, 'magnet_total':35},    
###jwc yy     {'row#':4, 'botid':41, 'light_lastdelta':42, 'light_total':43, 'magnet_lastdelta':44, 'magnet_total':45},    
###jwc yy ]


def clear_Stats_Fn():
    for bot_dictionary in rowData_ArrayList_OfDictionaryPairs_ForAllBots:
        print("  E1:" + str(bot_dictionary))
        ###jwc y? if scoreboard_DataMessage_Rcvd_Dict['#'] in bot_dictionary.values():
          
        print("  E2a:bot_dictionary: " + str(bot_dictionary))
        bot_dictionary['light_lastdelta'] = 0
        bot_dictionary['light_total'] = 0
        bot_dictionary['magnet_lastdelta'] = 0
        bot_dictionary['magnet_total'] = 0
        print("  E2b:bot_dictionary: " + str(bot_dictionary))
    scoreboardServer_WebGrid.update()
    ###jwc 23-0506-1700 y reduce to one scoreboardServer_WebGrid: grid2.update()
#
ui.button('Clear Stats', on_click=clear_Stats_Fn)

# update_WebGrid_03_Fn
#
def update_WebGrid_03_Fn():
    scoreboardServer_WebGrid.update()
#
###jwc y update_WebGrid_UiTimer_Active_Switch02 = ui.switch('active').bind_value_to(update_WebGrid__UiTimer_Active_n_Interval__Object, 'active')
###jwc y update_WebGrid_UiTimer_Active_Switch02 = ui.checkbox('update_WebGrid').bind_value_to(update_WebGrid__UiTimer_Active_n_Interval__Object, 'active')
###jwc y ui.label('Check!').bind_visibility_from(update_WebGrid_UiTimer_Active_Switch02, 'value')
#
## '0.1' sec
### jwc ym line_updates_02 = ui.timer(0.1, update_line_plot_02, active=True)
###jwc 23-0501-1400 yy line_updates_02 = ui.timer(2, update_line_plot_02, active=True)
#
## '0.05' sec update
###jwc y update_WebGrid__UiTimer_Active_n_Interval__Object = ui.timer(0.05, update_WebGrid_Fn, active=True)
### ###jwc y was 1 now to 10 >> 5: update_WebGrid__UiTimer_Active_n_Interval__Object = ui.timer(1, update_WebGrid_Fn, active=True)
###jwc 23-0506-1720 y Hold off to not compete w/ main update: update_WebGrid__UiTimer_Active_n_Interval__Object = ui.timer(5, update_WebGrid_Fn, active=True)
#
###jwc y update_WebGrid__UiTimer_Active_n_Interval__Object = ui.timer(0.05, update_WebGrid_Fn, active=True)
###jwc 20msec
###jwc ? update_WebGrid__UiTimer_Active_n_Interval__Object = ui.timer(0.020, update_WebGrid_Fn, active=True)
#
###jwc 30sec update_WebGrid__UiTimer_Active_n_Interval__Object = ui.timer(1, update_WebGrid_03_Fn, active=True)
###jwc 15 sec update_WebGrid__UiTimer_Active_n_Interval__Object = ui.timer(0.5, update_WebGrid_03_Fn, active=True)
###jwc 18 sec update_WebGrid__UiTimer_Active_n_Interval__Object = ui.timer(0.25, update_WebGrid_03_Fn, active=True)
###jwc 15-30 sec update_WebGrid__UiTimer_Active_n_Interval__Object = ui.timer(0.125, update_WebGrid_03_Fn, active=True)
###jwc 10-15sec update_WebGrid__UiTimer_Active_n_Interval__Object = ui.timer(0.5, update_WebGrid_03_Fn, active=True)
###jwc 8-10sec update_WebGrid__UiTimer_Active_n_Interval__Object = ui.timer(1, update_WebGrid_03_Fn, active=True)
###jwc 6-8sec update_WebGrid__UiTimer_Active_n_Interval__Object = ui.timer(2, update_WebGrid_03_Fn, active=True)
###jwc 6sec update_WebGrid__UiTimer_Active_n_Interval__Object = ui.timer(3, update_WebGrid_03_Fn, active=True)
###jwc 5sec update_WebGrid__UiTimer_Active_n_Interval__Object = ui.timer(4, update_WebGrid_03_Fn, active=True)
###jwc 6-8 sec update_WebGrid__UiTimer_Active_n_Interval__Object = ui.timer(5, update_WebGrid_03_Fn, active=True)
###jwc 4-6 sec update_WebGrid__UiTimer_Active_n_Interval__Object = ui.timer(4, update_WebGrid_03_Fn, active=True)
###jwc 5-9 sec update_WebGrid__UiTimer_Active_n_Interval__Object = ui.timer(5, update_WebGrid_03_Fn, active=True)
###jwc yy update_WebGrid__UiTimer_Active_n_Interval__Object = ui.timer(4, update_WebGrid_03_Fn, active=True)
###jwc yyy update_WebGrid__UiTimer_Active_n_Interval__Object = ui.timer(update_WebGrid_UiTimer_Initialization_Object.timer_Sec_Int, update_WebGrid_03_Fn, active=update_WebGrid_UiTimer_Initialization_Object.active_Bool)
###jwc yyy update_WebGrid__UiTimer_Active_n_Interval__Object = ui.timer(update_WebGrid_UiTimer_Initialization_Object.timer_Sec_Int, update_WebGrid_03_Fn, active = update_WebGrid_UiTimer_Initialization_Object.active_Bool)
###jwc n 'interval' error: update_WebGrid__UiTimer_Active_n_Interval__Object = ui.timer(interval=update_WebGrid_UiTimer_Initialization_Object.timer_Sec_Int, update_WebGrid_03_Fn, active=update_WebGrid_UiTimer_Initialization_Object.active_Bool)

# 1st Paramater: Initial Value Only 
# 3rd Paramater: Initial Value Only
update_WebGrid__UiTimer_Active_n_Interval__Object = ui.timer(update_WebGrid_UiTimer_Initialization_Object.timer_Sec_Int, update_WebGrid_03_Fn, active = update_WebGrid_UiTimer_Initialization_Object.active_Bool)



def update_WebGrid_UiTimer_Active_Toggle_Fn(event: ValueChangeEventArguments):
    ###jwc n AttributeError: 'dict' object has no attribute 'sender': name = type(event.sender).__name__
    ###jwc n ui.notify(f'{name}: {event.value}')
    ###jwc n update_WebGrid__UiTimer_Active_n_Interval__Object = ui.timer(updat e_WebGrid_UiTimer_Object.timer_Sec_Int, update_WebGrid_03_Fn, active=update_WebGrid_UiTimer_Initialization_Object.active_Bool)
    ###jwc y print("****** update_WebGrid_UiTimer_Active_Toggle_Fn: " + str(update_WebGrid_UiTimer_Initialization_Object.active_Bool))
    print("****** update_WebGrid_UiTimer_Active_Toggle_Fn: " + str(update_WebGrid__UiTimer_Active_n_Interval__Object.active))
#
###jwc n ###jwc ? update_WebGrid_UiTimer_Active_Switch = ui.switch ('update_WebGrid_UiTimer_Active_Switch', on_change=update_WebGrid_UiTimer_Active_Toggle_Fn).bind_value(update_WebGrid_UiTimer_Initialization_Object, 'active_Bool')
#
# 'Toggle' has  real-time feedback vs. 'Checkbox' and 'Switch' 
###jwc yyy update_WebGrid_UiTimer_Active_Toggle_Object = ui.toggle({0: 'WebGrid_Update:Off', 1: 'WebGrid_Update:On'}).bind_value(update_WebGrid__UiTimer_Active_n_Interval__Object, 'active')
update_WebGrid_UiTimer_Active_Toggle_Object = ui.toggle({0: 'WebGrid_Update:Off', 1: 'WebGrid_Update:On'}).on('click', update_WebGrid_UiTimer_Active_Toggle_Fn).bind_value(update_WebGrid__UiTimer_Active_n_Interval__Object, 'active')



def update_WebGrid_UiTimer_Timer_Toggle_Fn(event: ValueChangeEventArguments):
    ###jwc n 'sender' unknown':  name = type(event.sender).__name__
    ###jwc n ui.notify(f'{name}: {event.value}')
    ###jwc n AttributeError: 'dict' object has no attribute 'value': ui.notify(f'{event.value}')
    ###jwc n update_WebGrid__UiTimer_Active_n_Interval__Object = ui.timer(update_WebGrid_UiTimer_Initialization_Object.timer_Sec_Int, update_WebGrid_03_Fn, active=update_WebGrid_UiTimer_Initialization_Object.active_Bool)
    ###jwc y print("****** update_WebGrid_UiTimer_Timer_Toggle_Fn: " + str(update_WebGrid_UiTimer_Initialization_Object.timer_Sec_Int))
    print("****** update_WebGrid_UiTimer_Timer_Toggle_Fn: " + str(update_WebGrid__UiTimer_Active_n_Interval__Object.interval))
#
###jwc n update_WebGrid_UiTimer_Timer_Toggle_Object = ui.toggle({1: 'F', 2: 'G', 3: 'H'}).on('click', update_WebGrid_UiTimer_Active_Toggle_Fn).bind_value_from(bool,'update_WebGrid_UiTimer_Active_Bool')
###jwc ? update_WebGrid_UiTimer_Timer_Toggle_Object = ui.toggle({3: '3sec', 4: '4sec', 5: '5sec', 60: '60sec'}).on('click', update_WebGrid_UiTimer_Timer_Toggle_Fn).bind_value(update_WebGrid_UiTimer_Initialization_Object, 'timer_Sec_Int')
update_WebGrid_UiTimer_Timer_Toggle_Object = ui.toggle({3: '3sec', 4: '4sec', 5: '5sec', 60: '60sec'}).on('click', update_WebGrid_UiTimer_Timer_Toggle_Fn).bind_value(update_WebGrid__UiTimer_Active_n_Interval__Object, 'interval')
    


async def selectedRows_TeamBlue_Fn():
        ###jwc n rows = await scoreboardServer_WebGrid.get_selected_rows()
        ###jwc y rows = await grid2.get_selected_rows()
        rows = await scoreboardServer_WebGrid.get_selected_rows()

        ###jwc ? rows.forEach(function( selectedRow, index){
        ###jwc y  ui.notify("Notify")

        ###jwc ? })
        ###jwc y if len(rows) == 0:
        if rows:
            for row in rows:
                row['team_id'] = 'Blue'
                print("*** selectedRows_Fn:" + str(row))
                ui.notify(f"{row['bot_id']}, {row['team_id']}")
        else:
            ui.notify("No Data Selected")
            return
        scoreboardServer_WebGrid.update()
###jwc n selectedRows_TeamBlue_Object = ui.button('selectedRows_TeamBlue', on_click=selectedRows_TeamBlue_Fn)
ui.button('selectedRows_TeamBlue', on_click=selectedRows_TeamBlue_Fn)

def selectedRows_TeamBlue02_Fn():
        ###jwc n rows = await scoreboardServer_WebGrid.get_selected_rows()
        ###jwc y rows = await grid2.get_selected_rows()
        rows = scoreboardServer_WebGrid.get_selected_rows()
        row = scoreboardServer_WebGrid.get_selected_row()

        ###jwc ? rows.forEach(function( selectedRow, index){
        ###jwc y  ui.notify("Notify")

        ###jwc ? })
        ###jwc y if len(rows) == 0:

        if row:
            ###jwc y for row in rows:
            ###jwc row['team_id'] = 'Blue'
            print("*** selectedRow_Fn:" + str(row))

        if rows:
            ###jwc for row in rows:
                ###jwc row['team_id'] = 'Blue'
                ###jwc print("*** selectedRows_Fn:" + str(row))
            print("*** selectedRows_Fn:" + str(rows))

        else:
            ui.notify("No Data Selected")
            return
        scoreboardServer_WebGrid.update()
###jwc n selectedRows_TeamBlue02_Object = ui.button('selectedRows_TeamBlue', on_click=selectedRows_TeamBlue02_Fn)
ui.button('selectedRows_TeamBlue', on_click=selectedRows_TeamBlue02_Fn)


temp1 = 1
temp2 = 2

def update_WebGrid_Fn():
    ###jwc n scoreboardServer_WebGrid.options[
    ###jwc n     'rowData': [
    ###jwc n     {'name': 'Alice', 'age': 28},
    ###jwc n     {'name': 'Bob', 'age': 31},
    ###jwc n     {'name': 'Carol', 'age': 52},
    ###jwc n]] 
    ###jwc y scoreboardServer_WebGrid.options['rowData'][0]['age'] += 1
    ###jwc yy scoreboardServer_WebGrid.options['rowData'][0]['magnet_lastdelta'] += temp2
    rowData_Test_List[0]['light_lastdelta'] += temp1
    rowData_Test_List[0]['light_total'] += rowData_Test_List[0]['light_lastdelta']
    rowData_Test_List[0]['magnet_lastdelta'] += temp2
    rowData_Test_List[0]['magnet_total'] += rowData_Test_List[0]['magnet_lastdelta']

    ###jwc n scoreboardServer_WebGrid.options['rowData'] = sorted(rowData_ArrayList_OfDictionaryPairs_ForAllBots, key=lambda data:data['bot_id'] )
    scoreboardServer_WebGrid.update()

ui.button('update_WebGrid_Fn', on_click=update_WebGrid_Fn)



ui.label('*** ARCHIVE ***')

def update_WebGrid_02_Fn():
    ###jwc n scoreboardServer_WebGrid.options['rowData']['Carol']['age'] = random_Numpy(9)
    scoreboardServer_WebGrid.options['rowData'][0]['light_lastdelta'] += random_General.randint(1,100)
    scoreboardServer_WebGrid.options['rowData'][0]['light_total'] += random_General.randint(1,100)
    scoreboardServer_WebGrid.options['rowData'][0]['magnet_lastdelta'] += temp2
    scoreboardServer_WebGrid.options['rowData'][0]['magnet_total'] += temp2

    ###jwc 23-0504-0720 y rowData_Test_List.append({'row_id':5, 'bot_id':51, 'light_lastdelta':52, 'light_total':53, 'magnet_lastdelta':54, 'magnet_total':55})
    rowData_Test_List.append({'row_id':5, 'bot_id':1, 'mission_status':0, 'team_id':0, 'light_lastdelta':52, 'light_total':53, 'magnet_lastdelta':54, 'magnet_total':55})
    ###jwc y grid2.options['rowData'] = sorted(rowData_Test_List, key=lambda data:data['bot_id'] )
    ###jwc n grid2.options['rowData'] = sorted(rowData_ArrayList_OfDictionaryPairs_ForAllBots, key=lambda data:data['bot_id'] )
    scoreboardServer_WebGrid.update()

with ui.row():
    ui.button('update_WebGrid_02_Fn', on_click=update_WebGrid_02_Fn)
    ui.button('Select all', on_click=lambda: scoreboardServer_WebGrid.call_api_method('selectAll'))


### Test UI
###

def toggle_value_fn(bot_id_in:int):
    bot_TeamAssigned_Base0_Int[bot_id_in] += 1
    print("****** bot_TeamAssigned_Base0_Int[bot_id_in]: " + str(bot_TeamAssigned_Base0_Int[bot_id_in]))


def toggle_value_fn2():
    bot_TeamAssigned_Base0_Int[0] += 1
    print("****** bot_TeamAssigned_Base0_Int[0]: " + str(bot_TeamAssigned_Base0_Int[0]))
toggle5 = ui.toggle({1: 'F', 2: 'G', 3: 'H'}).on('click', toggle_value_fn2)


async def toggle_value_fn2A():
    bot_TeamAssigned_Base0_Int[0] += 1
    print("****** bot_TeamAssigned_Base0_Int[0]: " + str(bot_TeamAssigned_Base0_Int[0]))

def toggle_value_fn3():
    print("****** bot_TeamAssigned_Base0_Int[1]: " + str(bot_TeamAssigned_Base0_Int[1]))

if True: 
    def badge_fn():
        if badge1.text == '1':
            badge1.set_text('2')
        else:
            badge1.set_text('1')

def badge_fn2():
    if badge2.text == '-':
        badge2.set_text('A')
    elif badge2.text == 'A':
        badge2.set_text('B')
    elif badge2.text == 'B':
        badge2.set_text('-')

def badge_fn3():
    if badge3.text == '-':
        badge3.set_text('A')
    elif badge3.text == 'A':
        badge3.set_text('B')
    elif badge3.text == 'B':
        badge3.set_text('-')

    
with ui.row():
    toggle1 = ui.toggle([1, 2, 3], value=1)

    toggle2 = ui.toggle({1: 'A', 2: 'B', 3: 'C'}).bind_value(toggle1, 'value')

    ###jwc n toggle3 = ui.toggle({1: 'C', 2: 'D', 3: 'E'}).bind_value(toggle1, 'value').run_method('toggle_value_fn(1)', 'value')
    ###jwc n toggle3 = ui.toggle({1: 'C', 2: 'D', 3: 'E'}).bind_value(toggle1, 'value').run_method('toggle_value_fn(value)', 'value')
    ###jwc n toggle3 = ui.toggle({1: 'C', 2: 'D', 3: 'E'}).bind_value(toggle1, 'value').run_method('toggle_value_fn()', 'value')

    ###jwc n compiles but no response: toggle4 = ui.toggle({1: 'A', 2: 'B', 3: 'C'}).run_method('toggle_value_fn2')
    ###jwc n compiles but no response: toggle5 = ui.toggle({1: 'A', 2: 'B', 3: 'C'}).run_method('toggle_value_fn3')

    update2_Object = ui.button('Update2', on_click=toggle_value_fn2)
    update3_Object = ui.button('Update3', on_click=toggle_value_fn3)

    ###jwc n ui.toggle({1: 'A', 2: 'B', 3: 'C'}, on_click=toggle_value_fn2)
    ###jwc n toggle6A = ui.toggle({1: 'I', 2: 'J', 3: 'K'}).on('click', toggle_value_fn, ['1'])
    ###jwc n toggle6A = ui.toggle({1: 'I', 2: 'J', 3: 'K'}).on('click', toggle_value_fn, ['value'])

    ###jwc n compiles but no response: ui.toggle({1: 'A', 2: 'B', 3: 'C'}).run_method('toggle_value_fn2')
    ###jwc n compiles but no response: toggle6B = ui.toggle({1: 'A', 2: 'B', 3: 'C'}).run_method('toggle_value_fn2')

    ###jwc n compiles but no response: ui.toggle({1: 'A', 2: 'B', 3: 'C'}).run_method('toggle_value_fn2A')
    ###jwc n compiles but no response: toggle7 = ui.toggle({1: 'A', 2: 'B', 3: 'C'}).run_method('toggle_value_fn2A')

    ###jwc n compiles but no response: line_checkbox = ui.checkbox('active').bind_value(receive_Microbit_Messages_Object, 'active').run_method('toggle_value_fn2')
    ###jwc n compiles but no response: select1 = ui.select([1, 2, 3], value=1).run_method('toggle_value_fn2')

    ###jwc n not compile line_checkbox = ui.checkbox('active').on_click=toggle_value_fn2
    ###jwc n not compile ui.select([1, 2, 3], value=1).on_click=toggle_value_fn2


    with ui.button('Click me!', on_click=lambda: badge.set_text(str(int(badge.text) + 1))): 
        badge = ui.badge('0', color='red').props('floating')
    ###jwc n visibility still on: with ui.button('Click me1A'): 
    ###jwc n visibility still on:     badge1A = ui.badge('0', color='red').props('floating').set_visibility('False')

    if True:
        with ui.button('Click me1!', on_click=badge_fn): 
            badge1 = ui.badge('0', color='red').props('floating')

    with ui.button('Cl2!', on_click=badge_fn2): 
        badge2 = ui.badge('-', color='red').props('floating')
    with ui.button(rowData_ArrayList_OfDictionaryPairs_ForAllBots[0]['bot_id'], on_click=badge_fn3): 
        badge3 = ui.badge('-', color='red').props('floating')

    ##jwc n if True:
        ##jwc n with ui.button(rowData_ArrayList_OfDictionaryPairs_ForAllBots[0]['bot_id'], on_click=badge_fn3): 
            ##jwc n badge3 = ui.badge('-', color='red').props('floating').set_visibility('False')
        ##jwc n with ui.button(rowData_ArrayList_OfDictionaryPairs_ForAllBots[0]['bot_id'], on_click=badge_fn3): 
            ##jwc n badge3 = ui.badge('-', color='red').props('floating').set_visibility('True')
    ###jwc ? with ui.button(rowData_ArrayList_OfDictionaryPairs_ForAllBots[2]['bot_id'], on_click=badge_fn2): 
    ###jwc ?     badge5 = ui.badge('-', color='red').props('floating').set_visibility('False')
    ###jwc ? if False:
    ###jwc ?     with ui.button(rowData_ArrayList_OfDictionaryPairs_ForAllBots[0]['bot_id'], on_click=badge_fn2): 
    ###jwc ?         badge = ui.badge('-', color='red').props('floating')


# jwc Only evaluated at startup, then is ignored, thus not good for realtime
#
if len(rowData_ArrayList_OfDictionaryPairs_ForAllBots) >= 2:
###jwc if True:
    def badge_fn4():
        if badge4.text == '-':
            badge4.set_text('A')
        elif badge4.text == 'A':
            badge4.set_text('B')
        elif badge4.text == 'B':
            badge4.set_text('-')

    with ui.button(rowData_ArrayList_OfDictionaryPairs_ForAllBots[1]['bot_id'], on_click=badge_fn4): 
        badge4 = ui.badge('-', color='red').props('floating')



###jwc y }).classes('max-h-40')
###jwc y }).classes('max-h-80')
###jwc ? }).classes('max-h-500')
###jwc ? }).classes('max-h-full')
###jwc y }).classes('max-h-[128rem]')
###jwc y }).classes('h-[128rem]')

###jwc 23-0501-1500 yy    'rowData' : rowData_Test_List,

###jwc 23-0501-1520        {'headerName': 'Row#', 'field': 'row#'},
###jwc 23-0501-1520        {'headerName': 'BotId', 'field': 'botid'},
###jwc 23-0501-1520        {'headerName': 'Light_LastDelta', 'field': 'light_lastdelta'},
###jwc 23-0501-1520        {'headerName': 'Light_Total', 'field': 'light_total'},
###jwc 23-0501-1520        {'headerName': 'Magnet_LastDelta', 'field': 'magnet_lastdelta'},
###jwc 23-0501-1520        {'headerName': 'Magnet_Total', 'field': 'magnet_total'},

#
# scoreboardServer_WebGrid
#
scoreboardServer_WebGrid = ui.aggrid({
    'columnDefs': [
        {'headerName': 'Row_Id', 'field': 'row_id', 'sortable':'true'},
        ###jwc y {'headerName': 'Bot_Id', 'field': 'bot_id','sortable':'true'},
        {'headerName': 'Bot_Id', 'field': 'bot_id','sortable':'true', 'sort': 'asc', 'checkboxSelection': True},
        {'headerName': 'Mission_Status', 'field': 'mission_status'},
        {'headerName': 'Team_Id', 'field': 'team_id'},
        {'headerName': 'Light_LastDelta', 'field': 'light_lastdelta'},
        {'headerName': 'Light_Total', 'field': 'light_total', 'sortable':'true'},
        {'headerName': 'Magnet_LastDelta', 'field': 'magnet_lastdelta'},
        {'headerName': 'Magnet_Total', 'field': 'magnet_total', 'sortable':'true'},
    ],
    'rowData' : rowData_ArrayList_OfDictionaryPairs_ForAllBots,
    'rowSelection': 'multiple', 
    'rowSelectionWithClick': 'True', 
    ###jwc n not seem to work 'rowMultiSelectWithClick': 'True',

    'onGridReady': ui.notify("Grid Ready")

# Defaults to 'h-64'
# 1 rem = 16px, 2 rem = 1 full font height     
###jwc y }).classes('h-[128rem]')
###jwc y }).classes('h-64')
}).classes('h-[128rem]')




scoreboardServer_WebGrid_02 = ui.aggrid({
    'columnDefs': [
        {'headerName': 'Row_Id', 'field': 'row_id', 'sortable':'true'},
        ###jwc y {'headerName': 'Bot_Id', 'field': 'bot_id','sortable':'true'},
        {'headerName': 'Bot_Id', 'field': 'bot_id','sortable':'true', 'sort': 'asc', 'checkboxSelection': True},
        {'headerName': 'Mission_Status', 'field': 'mission_status'},
        {'headerName': 'Team_Id', 'field': 'team_id'},
        {'headerName': 'Light_LastDelta', 'field': 'light_lastdelta'},
        {'headerName': 'Light_Total', 'field': 'light_total', 'sortable':'true'},
        {'headerName': 'Magnet_LastDelta', 'field': 'magnet_lastdelta'},
        {'headerName': 'Magnet_Total', 'field': 'magnet_total', 'sortable':'true'},
    ],
    'rowData' : rowData_ArrayList_OfDictionaryPairs_ForAllBots,
    'rowSelection': 'multiple', 
    'rowSelectionWithClick': 'True', 
    ###jwc n not seem to work 'rowMultiSelectWithClick': 'True',

    'onGridReady': ui.notify("Grid Ready")

# Defaults to 'h-64'
# 1 rem = 16px, 2 rem = 1 full font height     
###jwc y }).classes('h-[128rem]')
###jwc y }).classes('h-64')
}).classes('h-64')


###jwc 20 scoreboardServer_WebGrid_02 = ui.aggrid({
###jwc 20     'columnDefs': [
###jwc 20         {'headerName': 'Name', 'field': 'name', 'checkboxSelection': True},
###jwc 20         {'headerName': 'Age', 'field': 'age'},
###jwc 20     ],
###jwc 20     'rowData': [
###jwc 20         {'name': 'Alice', 'age': 18},
###jwc 20         {'name': 'Bob', 'age': 21},
###jwc 20         {'name': 'Carol', 'age': 42},
###jwc 20     ],
###jwc 20     'rowSelection': 'multiple',
###jwc 20 }).classes('max-h-4



import asyncio

###jwc n async def output_selected_rows():
###jwc n     ###jwc n async with async_timeout
###jwc n     ###jwc n await asyncio.sleep(10)
###jwc n 
###jwc n     try:
###jwc n         ###jwc o rows = await scoreboardServer_WebGrid_02.get_selected_rows()
###jwc n         ###jwc n rows = await asyncio.shield(scoreboardServer_WebGrid_02.get_selected_rows())
###jwc n         rows = await scoreboardServer_WebGrid_02.get_selected_rows()
###jwc n         if rows:
###jwc n             for row in rows:
###jwc n                 ###jwc o ui.notify(f"{row['name']}, {row['age']}")
###jwc n                 ui.notify(f"{row['bot_id']}, {row['Row_Id']}, {row['light_lastdelta']}")
###jwc n                 print(f"*** *** {row['bot_id']}, {row['Row_Id']}, {row['light_lastdelta']}")
###jwc n         else:
###jwc n             ui.notify('No rows selected.')
###jwc n     except TimeoutError:
###jwc n         print('*** *** except TimeoutError *** ***')
###jwc n         temp = output_selected_rows()
###jwc n     print('*** *** output_selected_rows DONE *** ***')

async def output_selected_rows():
    ###jwc n async with async_timeout
    ###jwc n await asyncio.sleep(10)

    ###jwc o rows = await scoreboardServer_WebGrid_02.get_selected_rows()
    ###jwc n rows = await asyncio.shield(scoreboardServer_WebGrid_02.get_selected_rows())
    rows = await scoreboardServer_WebGrid_02.get_selected_rows()
    if rows:
        for row in rows:
            ###jwc o ui.notify(f"{row['name']}, {row['age']}")
            ui.notify(f"{row['bot_id']}, {row['row_id']}, {row['light_lastdelta']}")
            print(f"*** *** {row['bot_id']}, {row['row_id']}, {row['light_lastdelta']}")
    else:
        ui.notify('No rows selected.')


async def output_selected_row():
    row = await scoreboardServer_WebGrid_02.get_selected_row()
    if row:
        ###jwc o ui.notify(f"{row['name']}, {row['age']}")
        ui.notify(f"{row['bot_id']}, {row['row_id']}, {row['light_lastdelta']}")
        print(f"*** *** {row['bot_id']}, {row['row_id']}, {row['light_lastdelta']}")
    else:
        ui.notify('No row selected!')


async def main_01():
    task = asyncio.create_task(
        output_selected_rows()
    )
    print("*** *** main_01 *** ***")
    MAX_TIMEOUT = 20
    try:
        await asyncio.wait_for(task, timeout=MAX_TIMEOUT)
    except TimeoutError:
        print('The task was cancelled due to a timeout')      

async def main_02():
    task = asyncio.create_task(
        output_selected_rows()
    )

    MAX_TIMEOUT = 20
    try:
        await asyncio.wait_for(asyncio.shield(task), timeout=MAX_TIMEOUT)
    except TimeoutError:
        print('The task took more than expected and will complete soon.')
        result = await task
        print(result)


###jwc o ui.button('Output selected rows', on_click=output_selected_rows)
###jwc n ui.button('Output selected rows', on_click=main_02)
ui.button('Output selected rows', on_click=output_selected_rows)
ui.button('Output selected row', on_click=output_selected_row)



grid = ui.aggrid({
    'columnDefs': [
        {'headerName': 'Name', 'field': 'name', 'checkboxSelection': True},
        {'headerName': 'Age', 'field': 'age'},
    ],
    'rowData': [
        {'name': 'Alice', 'age': 18},
        {'name': 'Bob', 'age': 21},
        {'name': 'Carol', 'age': 42},
    ],
    'rowSelection': 'multiple',
}).classes('max-h-40')

async def output_selected_rows_02():
    rows = await grid.get_selected_rows()
    if rows:
        for row in rows:
            ui.notify(f"{row['name']}, {row['age']}")
    else:
        ui.notify('No rows selected.')

async def output_selected_row_02():
    row = await grid.get_selected_row()
    if row:
        ui.notify(f"{row['name']}, {row['age']}")
    else:
        ui.notify('No row selected!')

ui.button('Output selected rows', on_click=output_selected_rows_02)
ui.button('Output selected row', on_click=output_selected_row_02)




#
# Seems #1: receive_Microbit_Messages_Object 0.0001sec (0.1msec) -&- update_WebGrid__UiTimer_Active_n_Interval__Object 4 sec seems optimum :)+
# Seems #2: receive_Microbit_Messages_Object 0.001sec (1msec) -&- update_WebGrid__UiTimer_Active_n_Interval__Object 3 sec seems optimum :)+
#

###jwc o receive_Microbit_Messages_Object = ui.timer(0.1, receive_Microbit_Messages_Fn, active=False)
###jwc timer x2 speed: 0.1 to 0.05
###jwc o receive_Microbit_Messages_Object = ui.timer(0.05, receive_Microbit_Messages_Fn, active=False)
## '0.05' sec
###jwc good for slow real-time y receive_Microbit_Messages_Object = ui.timer(0.05, receive_Microbit_Messages_Fn, active=True)
###jwc y no more linegraph real-time to test chart realtime instead, 
###jwc TYJ LINE GRAPH DID SEEM TO SLOW DOWN TEXTCHART/DISPLAY BY 10-20 SEC :)+
###jwc y receive_Microbit_Messages_Object = ui.timer(0.05, receive_Microbit_Messages_Fn, active=False)
### ### jwc yyy tyj: was 1 now to 10: receive_Microbit_Messages_Object = ui.timer(1, receive_Microbit_Messages_Fn, active=True)
###jwc 23-0506-1640 50 sec: receive_Microbit_Messages_Object = ui.timer(1, receive_Microbit_Messages_Fn, active=True)
###jwc 23-0506-1640 25 sec: receive_Microbit_Messages_Object = ui.timer(0.5, receive_Microbit_Messages_Fn, active=True)
###jwc 23-0506-1640 10 sec: receive_Microbit_Messages_Object = ui.timer(0.25, receive_Microbit_Messages_Fn, active=True)
###jwc 23-0506-1640 2-3 sec: receive_Microbit_Messages_Object = ui.timer(0.125, receive_Microbit_Messages_Fn, active=True)
###jwc 23-0506-1640 2-3 sec :)+ 0.05sec=20fps
###jwc ? receive_Microbit_Messages_Object = ui.timer(0.05, receive_Microbit_Messages_Fn, active=True)
###jwc ? receive_Microbit_Messages_Object = ui.timer(0.01, receive_Microbit_Messages_Fn, active=True)

###jwc 2nd bot '12' not show: n receive_Microbit_Messages_Object = ui.timer(1, receive_Microbit_Messages_Fn, active=True)
###jwc ? receive_Microbit_Messages_Object = ui.timer(0.5, receive_Microbit_Messages_Fn, active=True)
###jwc ? receive_Microbit_Messages_Object = ui.timer(0.05, receive_Microbit_Messages_Fn, active=True)
###jwc y receive_Microbit_Messages_Object = ui.timer(0.1, receive_Microbit_Messages_Fn, active=True)
###jwc y receive_Microbit_Messages_Object = ui.timer(0.05, receive_Microbit_Messages_Fn, active=True)
###jwc 20msec: 30 sec  receive_Microbit_Messages_Object = ui.timer(0.020, receive_Microbit_Messages_Fn, active=True)

###jwc 10-20sec receive_Microbit_Messages_Object = ui.timer(0.010, receive_Microbit_Messages_Fn, active=True)
###jwc 1 NoSerialRead every 2-3 messages y receive_Microbit_Messages_Object = ui.timer(0.001, receive_Microbit_Messages_Fn, active=True)
###jwc 2.5' receive_Microbit_Messages_Object = ui.timer(0.0001, receive_Microbit_Messages_Fn, active=True)
###jwc 7-8sec / 1 NoSerialRead every 2 messages:  receive_Microbit_Messages_Object = ui.timer(0.001, receive_Microbit_Messages_Fn, active=True)
###jwc 1 NoSerialRead after each wave (11,12): receive_Microbit_Messages_Object = ui.timer(0.0001, receive_Microbit_Messages_Fn, active=True)
###jwc same as 0.0001 receive_Microbit_Messages_Object = ui.timer(0.00001, receive_Microbit_Messages_Fn, active=True)
###jwc same as 0.0001 receive_Microbit_Messages_Object = ui.timer(0.001, receive_Microbit_Messages_Fn, active=True)
###jwc same as 0.0001 receive_Microbit_Messages_Object = ui.timer(0.01, receive_Microbit_Messages_Fn, active=True)
###jwc same receive_Microbit_Messages_Object = ui.timer(0.1, receive_Microbit_Messages_Fn, active=True)
###jwc 1 NoSerialRead every 7-8 messages: receive_Microbit_Messages_Object = ui.timer(1, receive_Microbit_Messages_Fn, active=True)
###jwc 1 NoSerialRead every 2 (BotId 11,12) messages: receive_Microbit_Messages_Object = ui.timer(0.1, receive_Microbit_Messages_Fn, active=True)
###jwc 1 NoSerialRead every 2 (BotId 11,12) messages: receive_Microbit_Messages_Object = ui.timer(0.01, receive_Microbit_Messages_Fn, active=True)
###jwc 1 NoSearialRead every 2-5-8 (BotId 11,12,14) messages: receive_Microbit_Messages_Object = ui.timer(0.01, receive_Microbit_Messages_Fn, active=True)
###jwc 1 NoSearialRead every 2-5-8 (BotId 11,12,14) messages: receive_Microbit_Messages_Object = ui.timer(0.001, receive_Microbit_Messages_Fn, active=True)
###jwc 1 NoSearialRead every 2-5 (BotId 11,12,14) messages: 0.1msec
receive_Microbit_Messages_Object = ui.timer(0.0001, receive_Microbit_Messages_Fn, active=True)

###jwc ? line_checkbox = ui.checkbox('active').bind_value(receive_Microbit_Messages_Object, 'active')
###jwc y line_checkbox = ui.checkbox('active').bind_value(receive_Microbit_Messages_Object, 'active')


### ### jwc yyy tyj: line_checkbox = ui.checkbox('active').bind_value(receive_Microbit_Messages_Object, 'active')
### jwc 23-0504-0720 y ui.button('Update Chart', on_click=receive_Microbit_Messages_Fn)


ui.run()


#
# Archive
#

###jwc n will not work, no returned selected rows: def selectedRows_Fn5():
###jwc n will not work, no returned selected rows:         ###jwc n rows = await scoreboardServer_WebGrid.get_selected_rows()
###jwc n will not work, no returned selected rows:         rows = grid2.get_selected_rows()
###jwc n will not work, no returned selected rows: 
###jwc n will not work, no returned selected rows:         ###jwc ? rows.forEach(function( selectedRow, index){
###jwc n will not work, no returned selected rows:         ui.notify("Notify")
###jwc n will not work, no returned selected rows: 
###jwc n will not work, no returned selected rows:         ###jwc ? })
###jwc n will not work, no returned selected rows:         if rows == None:
###jwc n will not work, no returned selected rows:             ui.notify("No Data Selected")
###jwc n will not work, no returned selected rows:             return
###jwc n will not work, no returned selected rows:         else:
###jwc n will not work, no returned selected rows:             ui.notify("Yes Data Selected")
###jwc n will not work, no returned selected rows: 
###jwc n will not work, no returned selected rows:         scoreboardServer_WebGrid.update()
###jwc n will not work, no returned selected rows: ui.button('Update5', on_click=selectedRows_Fn5)


###jwc 23-0506-1700 y reduce to one scoreboardServer_WebGrid: grid2 = ui.aggrid({
###jwc 23-0506-1700 y reduce to one scoreboardServer_WebGrid:     'columnDefs': [
###jwc 23-0506-1700 y reduce to one scoreboardServer_WebGrid:         {'headerName': 'Row_Id', 'field': 'row_id'},
###jwc 23-0506-1700 y reduce to one scoreboardServer_WebGrid:         ###jwc y {'headerName': 'Bot_Id', 'field': 'bot_id','sortable':'true'},
###jwc 23-0506-1700 y reduce to one scoreboardServer_WebGrid:         {'headerName': 'Bot_Id', 'field': 'bot_id','sortable':'true', 'sort': 'asc'},
###jwc 23-0506-1700 y reduce to one scoreboardServer_WebGrid:         {'headerName': 'Mission_Status', 'field': 'mission_status'},
###jwc 23-0506-1700 y reduce to one scoreboardServer_WebGrid:         {'headerName': 'Team_Id', 'field': 'team_id'},
###jwc 23-0506-1700 y reduce to one scoreboardServer_WebGrid:         {'headerName': 'Light_LastDelta', 'field': 'light_lastdelta'},
###jwc 23-0506-1700 y reduce to one scoreboardServer_WebGrid:         {'headerName': 'Light_Total', 'field': 'light_total'},
###jwc 23-0506-1700 y reduce to one scoreboardServer_WebGrid:         {'headerName': 'Magnet_LastDelta', 'field': 'magnet_lastdelta'},
###jwc 23-0506-1700 y reduce to one scoreboardServer_WebGrid:         {'headerName': 'Magnet_Total', 'field': 'magnet_total'},
###jwc 23-0506-1700 y reduce to one scoreboardServer_WebGrid:     ],
###jwc 23-0506-1700 y reduce to one scoreboardServer_WebGrid:     'rowData' : rowData_ArrayList_OfDictionaryPairs_ForAllBots,
###jwc 23-0506-1700 y reduce to one scoreboardServer_WebGrid:     'rowSelection': 'multiple', 
###jwc 23-0506-1700 y reduce to one scoreboardServer_WebGrid:     'rowSelectionWithClick': 'True', 
###jwc 23-0506-1700 y reduce to one scoreboardServer_WebGrid:     ###jwc n not seem to work 'rowMultiSelectWithClick': 'True',
###jwc 23-0506-1700 y reduce to one scoreboardServer_WebGrid: 
###jwc 23-0506-1700 y reduce to one scoreboardServer_WebGrid:     'onGridReady': ui.notify("Grid Ready")
###jwc 23-0506-1700 y reduce to one scoreboardServer_WebGrid: 
###jwc 23-0506-1700 y reduce to one scoreboardServer_WebGrid: # Defaults to 'h-64'
###jwc 23-0506-1700 y reduce to one scoreboardServer_WebGrid: # 1 rem = 16px, 2 rem = 1 full font height     
###jwc 23-0506-1700 y reduce to one scoreboardServer_WebGrid: }).classes('h-[128rem]')

###jwc 23-0506-1700 y reduce to one scoreboardServer_WebGrid: def updateGrid2():
###jwc 23-0506-1700 y reduce to one scoreboardServer_WebGrid:     ###jwc n scoreboardServer_WebGrid.options[
###jwc 23-0506-1700 y reduce to one scoreboardServer_WebGrid:     ###jwc n     'rowData': [
###jwc 23-0506-1700 y reduce to one scoreboardServer_WebGrid:     ###jwc n     {'name': 'Alice', 'age': 28},
###jwc 23-0506-1700 y reduce to one scoreboardServer_WebGrid:     ###jwc n     {'name': 'Bob', 'age': 31},
###jwc 23-0506-1700 y reduce to one scoreboardServer_WebGrid:     ###jwc n     {'name': 'Carol', 'age': 52},
###jwc 23-0506-1700 y reduce to one scoreboardServer_WebGrid:     ###jwc n]] 
###jwc 23-0506-1700 y reduce to one scoreboardServer_WebGrid:     ###jwc y scoreboardServer_WebGrid.options['rowData'][0]['age'] += 1
###jwc 23-0506-1700 y reduce to one scoreboardServer_WebGrid:     ###jwc yy scoreboardServer_WebGrid.options['rowData'][0]['magnet_lastdelta'] += temp2
###jwc 23-0506-1700 y reduce to one scoreboardServer_WebGrid:     grid2.options['rowData'][0]['magnet_lastdelta'] += temp2
###jwc 23-0506-1700 y reduce to one scoreboardServer_WebGrid:     grid2.options['rowData'][0]['magnet_total'] += temp2
###jwc 23-0506-1700 y reduce to one scoreboardServer_WebGrid:     grid2.options['rowData'][0]['light_lastdelta'] += random_General.randint(1,100)
###jwc 23-0506-1700 y reduce to one scoreboardServer_WebGrid:     ###jwc n scoreboardServer_WebGrid.options['rowData']['Carol']['age'] = random_Numpy(9)
###jwc 23-0506-1700 y reduce to one scoreboardServer_WebGrid:     grid2.options['rowData'][0]['light_total'] += random_General.randint(1,100)
###jwc 23-0506-1700 y reduce to one scoreboardServer_WebGrid: 
###jwc 23-0506-1700 y reduce to one scoreboardServer_WebGrid:     grid2.update()

###jwc 23-0506-1700 y reduce to one scoreboardServer_WebGrid: ### ###jwc y was 5 now 1: update_Grid2 = ui.timer(5, updateGrid2, active=True)
###jwc 23-0506-1700 y reduce to one scoreboardServer_WebGrid: update_Grid2 = ui.timer(1, updateGrid2, active=True)
###jwc 23-0506-1700 y reduce to one scoreboardServer_WebGrid: 
###jwc 23-0506-1700 y reduce to one scoreboardServer_WebGrid:     ###jwc y scoreboardServer_WebGrid.options['rowData'][1]['age'] += 1
###jwc 23-0506-1700 y reduce to one scoreboardServer_WebGrid:     ###jwc y scoreboardServer_WebGrid.options['rowData'][2]['weight'] += 2


