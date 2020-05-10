### contains the body of the hook-functions which are been defined in hooksDictionary.py ###

import re
import logging
import constants
import random
import logger

def CreateFileAHookFunction(nktHook, nktProcess, nktHookCallInfo):
    param = nktHookCallInfo.Params()
    value = param.First().Value

    if re.search('vbox', value, re.IGNORECASE) or re.search('vm', value, re.IGNORECASE):
        logger.log(logging.WARNING, nktHook.FunctionName + " on " + value)
        nktHookCallInfo.Result().LongVal = -1


def IsDebuggerPresentHookFunction(nktHook, nktProcess, nktHookCallInfo):
    nktHookCallInfo.SkipCall()
    logger.log(logging.WARNING, nktHook.FunctionName)
    nktHookCallInfo.Result().LongVal = 0

def GetSystemInfoHookFunction(nktHook, nktProcess, nktHookCallInfo):
    param = nktHookCallInfo.Params().First().Evaluate()
    logger.log(logging.WARNING, nktHook.FunctionName)
    param.Field(5).Value = 2

def GetProcessAffinityMaskHookFunction(nktHook, nktProcess, nktHookCallInfo):
    param = nktHookCallInfo.Params().GetAt(2).Evaluate()
    logger.log(logging.WARNING, nktHook.FunctionName)
    param.ULongVal = 3

def GetFileAttributesHookFunction(nktHook, nktProcess, nktHookCallInfo):
    param = nktHookCallInfo.Params()
    value = param.First().Value

    if re.search('vbox', value, re.IGNORECASE) or re.search('vm', value, re.IGNORECASE):
        logger.log(logging.WARNING, nktHook.FunctionName + " on " + value)
        nktHookCallInfo.Result().LongVal = -1

def CheckRemoteDebuggerPresentHookFunction(nktHook, nktProcess, nktHookCallInfo):
    param = nktHookCallInfo.Params().GetAt(1).Evaluate()
    logger.log(logging.WARNING, nktHook.FunctionName)
    param.Value = 0


##### NON VA #### probabilmente la modifica dei parametri su ntdll non funziona
def NtQueryInformationProcessHookFunction(nktHook, nktProcess, nktHookCallInfo):
    informationClass = nktHookCallInfo.Params().GetAt(1).Evaluate()

    #ProcessBasicInformation OR ProcessDebugPort OR tempValue
    if informationClass.Value == 0 or informationClass.Value == 7 or informationClass.Value == 36:

        processInformation = nktHookCallInfo.Params().GetAt(2).Evaluate()
        if informationClass.Value == 7:
            logger.log(logging.WARNING, nktHook.FunctionName + " (ProcessDebugPort)" )
            #ProcessDebugPort
            #print processInformation.LongVal
            nktHookCallInfo.Params().GetAt(2).LongVal = 2

        if informationClass.Value == 0:
            logger.log(logging.WARNING, nktHook.FunctionName + " (ProcessBasicInformation)")
            address = processInformation.Address
            #print address
            import ctypes
            g = (ctypes.c_char * 24).from_address(int(str(address), 16))
            #print g
    #TODO
    #print informationClass.UShortVal

    #
    #     logging.warning("Invoked: " + nktHook.FunctionName)


##### NON VA ####
def GetDiskFreeSpaceExHookFunction(nktHook, nktProcess, nktHookCallInfo):
    nktHookCallInfo.SkipCall()
    logger.log(logging.WARNING, nktHook.FunctionName)
    nktHookCallInfo.Params().GetAt(2).Value = 0

def GlobalMemoryStatusExHookFunction(nktHook, nktProcess, nktHookCallInfo):
    logger.log(logging.WARNING, nktHook.FunctionName)
    memorystatusex = nktHookCallInfo.Params().GetAt(0).Evaluate()
    memorystatusex.Field(2).ULongLongVal = 4000000000   #4GB

def SetupDiGetClassDevsHookFunction(nktHook, nktProcess, nktHookCallInfo):
    nktHookCallInfo.SkipCall()
    logger.log(logging.WARNING, nktHook.FunctionName)
    nktHookCallInfo.Result().LongVal = -1

#### NON VA ####
def DeviceIoControlHookFunction(nktHook, nktProcess, nktHookCallInfo):
    logger.log(logging.WARNING, nktHook.FunctionName)
    size = nktHookCallInfo.Params().GetAt(4).FullEvaluate()
    #print size.Address
    #print size.Memory().ReadMem(size.Address, size.Address, 8)


#### NON VA ####
def NtQuerySystemInformationHookFunction(nktHook, nktProcess, nktHookCallInfo):
    informationClass = nktHookCallInfo.Params().GetAt(0).Evaluate()

    # SystemKernelDebuggerInformation
    if informationClass.Value == 35:
        logger.log(logging.WARNING, nktHook.FunctionName + " (SystemKernelDebuggerInformation)")
        systeminfo = nktHookCallInfo.Params().GetAt(1)
        systeminfo.LongVal = 1

def GetCursorPosHookFunction(nktHook, nktProcess, nktHookCallInfo):
    logger.log(logging.WARNING, nktHook.FunctionName)
    lppoint = nktHookCallInfo.Params().GetAt(0).Evaluate()
    lppoint.Field(0).LongVal = random.randint(0,1920)
    lppoint.Field(1).LongVal = random.randint(0,1080)

def RegQueryValueExHookFunction(nktHook, nktProcess, nktHookCallInfo):
    lpvaluename = nktHookCallInfo.Params().GetAt(1)
    valuename = lpvaluename.ReadString()

    #HARDWARE\\DEVICEMAP\\Scsi\\Scsi Port 0\\Scsi Bus 0\\Target Id 0\\Logical Unit Id 0 -> Identifier
    if valuename == "Identifier":
        logger.log(logging.WARNING, nktHook.FunctionName + " on HARDWARE\\DEVICEMAP\\Scsi\\Scsi Port 0\\Scsi Bus 0\\Target Id 0\\Logical Unit Id 0 -> Identifier" )
        lpdata = nktHookCallInfo.Params().GetAt(4)
        lpdata.WriteString("SAMSUNG", 0)

    #HARDWARE\\Description\\System -> SystemBiosVersion
    elif valuename == "SystemBiosVersion":
        logger.log(logging.WARNING, nktHook.FunctionName + " on HARDWARE\\Description\\System -> SystemBiosVersion")
        lpdata = nktHookCallInfo.Params().GetAt(4)
        lpdata.WriteString("SAMSUNG", 0)

    #HARDWARE\\Description\\System -> VideoBiosVersion
    elif valuename == "VideoBiosVersion":
        logger.log(logging.WARNING, nktHook.FunctionName + " on HARDWARE\\Description\\System -> VideoBiosVersion")
        lpdata = nktHookCallInfo.Params().GetAt(4)
        lpdata.WriteString("NVIDIA", 0)

    #HARDWARE\\Description\\System -> SystemBiosDate
    elif valuename == "SystemBiosDate":
        logger.log(logging.WARNING, nktHook.FunctionName + " on HARDWARE\\Description\\System -> SystemBiosDate")
        lpdata = nktHookCallInfo.Params().GetAt(4)
        lpdata.WriteString("22/09/2018", 0)

    #SYSTEM\\ControlSet001\\Control\\SystemInformation -> SystemManufacturer
    elif valuename == "SystemManufacturer":
        logger.log(logging.WARNING, nktHook.FunctionName + " on SYSTEM\\ControlSet001\\Control\\SystemInformation -> SystemManufacturer")
        lpdata = nktHookCallInfo.Params().GetAt(4)
        lpdata.WriteString("SAMSUNG", 0)

    #SYSTEM\\ControlSet001\\Control\\SystemInformation -> SystemProductName
    elif valuename == "SystemProductName":
        logger.log(logging.WARNING, nktHook.FunctionName + " on SYSTEM\\ControlSet001\\Control\\SystemInformation -> SystemProductName")
        lpdata = nktHookCallInfo.Params().GetAt(4)
        lpdata.WriteString("SAMSUNG", 0)

def RegOpenKeyExHookFunction(nktHook, nktProcess, nktHookCallInfo):
    '''
    HARDWARE\\ACPI\\DSDT\\VBOX__
    HARDWARE\\ACPI\\FADT\\VBOX__
    HARDWARE\\ACPI\\RSDT\\VBOX__
    SOFTWARE\\Oracle\\VirtualBox Guest Additions
    SYSTEM\\ControlSet001\\Services\\VBoxGuest
    SYSTEM\\ControlSet001\\Services\\VBoxMouse
    SYSTEM\\ControlSet001\\Services\\VBoxService
    SYSTEM\\ControlSet001\\Services\\VBoxSF
    SYSTEM\\ControlSet001\\Services\\VBoxVideo
    SOFTWARE\\VMware, Inc.\\VMware Tools
    '''

    lpsubkey = nktHookCallInfo.Params().GetAt(1)
    key = lpsubkey.ReadString()

    if re.search('vbox', key, re.IGNORECASE) \
            or re.search('virtualbox', key, re.IGNORECASE)\
            or re.search('vmware', key, re.IGNORECASE):
        logger.log(logging.WARNING, nktHook.FunctionName + " on " + key)
        nktHookCallInfo.Result().LongVal = -1

def GetAdaptersInfoHookFunction(nktHook, nktProcess, nktHookCallInfo):
    logger.log(logging.WARNING, nktHook.FunctionName)
    size = nktHookCallInfo.Params().GetAt(1).Evaluate()
    size.LongVal = 0

    #
    # print size.LongVal
    # #loop
    # to explore Linked List
    # ipstruct = nktHookCallInfo.Params().GetAt(0).Evaluate()
    # for num in range(0, size.LongVal - 1):
    #     addresslength = ipstruct.Field(4)
    #     if addresslength.LongVal == 6:
    #         address = ipstruct.Field(5)
    #         address.WriteByteValAt(0, 5)
    #         address_str = hex(address.ByteValAt(0)) + hex(address.ByteValAt(1)) + hex(address.ByteValAt(2))
    #         print str(address_str)
    #     ipstruct = ipstruct.Field(0).Evaluate()
    
def CreateToolhelp32Snapshot(nktHook, nktProcess, nktHookCallInfo):
    logger.log(logging.WARNING, nktHook.FunctionName)
    
def Process32FirstW(nktHook, nktProcess, nktHookCallInfo):
    logger.log(logging.WARNING, nktHook.FunctionName)

def Process32NextW(nktHook, nktProcess, nktHookCallInfo):
    logger.log(logging.WARNING, nktHook.FunctionName)
    lppe = nktHookCallInfo.Params().GetAt(1).Evaluate().Fields().GetAt(9)
    logger.log(logging.WARNING, lppe)
