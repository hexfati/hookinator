# Event Handlers ======================================================================

import win32com.client
import re
from hooksDictionary import hooksAndFunctions
import hookFunctions

class NktSpyMgrEvents:
    def OnProcessStarted(self, nktProcessAsPyIDispatch):
        nktProcess = win32com.client.Dispatch(nktProcessAsPyIDispatch)
        if (nktProcess.Name == "notepad.exe"):
            print 'Notepad was started.'

    def OnProcessTerminated(self, nktProcessAsPyIDispatch):
        nktProcess = win32com.client.Dispatch(nktProcessAsPyIDispatch)
        if (nktProcess.Name == "notepad.exe"):
            print 'Notepad was terminated.'

    def OnFunctionCalled(self, nktHook, nktProcess, nktHookCallInfo):
        nktProcess = win32com.client.Dispatch(nktProcess)
        nktHookCallInfo = win32com.client.Dispatch(nktHookCallInfo)

        ### Retrieve the function to invoke from the dictionary
        hookFunctionName = hooksAndFunctions.get(nktHook.FunctionName)[0]
        if hookFunctionName is not None:
            getattr(hookFunctions, hookFunctionName)(nktHook, nktProcess, nktHookCallInfo)

    # Aux Functions =========================================================================

    def SkipCall(self, nktHookCallInfo, nktProcess):
        nktHookCallInfo.SkipCall()
        if (nktProcess.PlatformBits == 64):
            nktHookCallInfo.Result().LongLongVal = -1
        else:
            nktHookCallInfo.Result().LongVal = -1
        nktHookCallInfo.LastError = 5

    def GetFileNameParam(self, nktParamsEnum):
        nktParam = nktParamsEnum.First()
        return nktParam.Value


