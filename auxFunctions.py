# Auxiliar Functions =====================================================================

import psutil
import constants
import logging
from hashlib import md5
import logger

from hooksDictionary import hooksAndFunctions
import subprocess

def GetPIDByProcessName(aProcessName):
    for proc in psutil.process_iter():
        if proc.name == aProcessName:
            return proc.pid


def OpenProcessAndGetPID(spyManager, filepath):

    logging.info("Starting...")
    process, continueEvent = spyManager.CreateProcess(filepath, True)

    return process, continueEvent


def HookFunctionForProcess(spyManager, functionModuleAndName, pid, callFlag):
    logger.log(logging.DEBUG, "Hooking function " + functionModuleAndName)
    if callFlag == "pre":
        callFlag = constants.flgOnlyPreCall
    if callFlag == "post":
        callFlag = constants.flgOnlyPostCall

    callFlag = (callFlag | constants.flgAutoHookChildProcess)
    hook = spyManager.CreateHook(functionModuleAndName, callFlag)
    hook.Attach(pid, True)
    hook.Hook(True)
    logger.log(logging.DEBUG, "OK")
    return hook


def StartProcessAndHook(spyManager, filepath):
    process, continueEvent = OpenProcessAndGetPID(spyManager, filepath)

    for hook in hooksAndFunctions:
        HookFunctionForProcess(spyManager, hook, process.Id, hooksAndFunctions.get(hook)[1])

    logger.log(logging.DEBUG, "------------------------------------------------------")

    spyManager.ResumeProcess(process, continueEvent)

def calculateMD5(filepath):
    f = open(filepath, "rb")
    data = f.read()
    f.close()
    hash = md5(data).hexdigest()
    return hash
