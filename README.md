         _                 _    _             _            
        | |               | |  (_)           | |            
        | |__   ___   ___ | | ___ _ __   __ _| |_ ___  _ __ 
        | '_ \ / _ \ / _ \| |/ / | '_ \ / _` | __/ _ \| '__|
        | | | | (_) | (_) |   <| | | | | (_| | || (_) | |   
        |_| |_|\___/ \___/|_|\_\_|_| |_|\__,_|\__\___/|_| 


A Deviare-based tool to hook and manipulate WinAPI calls. It is useful to understand and hijack API calls perfomed by a program. You can use hookinator in Malware Analysis to avoid API-based evasion techniques and to allow the complete detonation of the malware.
The current hooked WinAPIs are defined into `hooksDictionary.py` file.

#### Note

*  Works only with Python27

#### Installation (Tested on Win7 32-64 bit) 

1. download deviare release:
	https://github.com/nektra/Deviare2/releases/download/v2.8.3/Deviare.2.8.3.zip

2. execute the command: `regsvr32 DeviareCOM.dll` or `regsvr32 DeviareCOM64.dll`

3. download hookinator-master

4. install hookinator dependencies using the requirements.txt file:
	pip install -r requirements.txt 

5. execute hookinator:
	python hookinator.py 

#### Usage

1. Select the file you want to launch and to monitor

2. View intercepted APIs in prompt
