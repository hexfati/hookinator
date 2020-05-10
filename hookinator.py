# Main ==================================================================

import win32com.client
import ctypes
import Tkinter, tkFileDialog
from eventHandlers import NktSpyMgrEvents
from auxFunctions import *
import logging
import sys
import logger


logo = "  _                 _    _             _             \n" \
       " | |               | |  (_)           | |            \n" \
       " | |__   ___   ___ | | ___ _ __   __ _| |_ ___  _ __ \n" \
       " | '_ \ / _ \ / _ \| |/ / | '_ \ / _` | __/ _ \| '__|\n" \
       " | | | | (_) | (_) |   <| | | | | (_| | || (_) | |   \n" \
       " |_| |_|\___/ \___/|_|\_\_|_| |_|\__,_|\__\___/|_|   \n\n" \


try:
       filepath = sys.argv[1]
except IndexError:
       root = Tkinter.Tk()
       root.withdraw()
       filepath = tkFileDialog.askopenfilename()


try:
       logger.init(filepath)
       logger.log(logging.INFO, logo)

       spyManager = win32com.client.DispatchWithEvents('DeviareCOM.NktSpyMgr', NktSpyMgrEvents)
       spyManager.Initialize()

       StartProcessAndHook(spyManager, filepath)
except:
       logger.log(logging.ERROR, "ERROR")
       exit(1)

MessageBox = ctypes.windll.user32.MessageBoxA
MessageBox(None, 'Press OK to end hookinator', 'hookinator', 0)


