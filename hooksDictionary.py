hooksAndFunctions = {
    "kernel32.dll!CreateFileA" :
        ["CreateFileAHookFunction", "post"],
    "kernel32.dll!IsDebuggerPresent" :
        ["IsDebuggerPresentHookFunction", "pre"],
    "kernel32.dll!GetSystemInfo":
        ["GetSystemInfoHookFunction", "post"],
    "kernel32.dll!GetProcessAffinityMask":
        ["GetProcessAffinityMaskHookFunction", "post"],
    "kernel32.dll!GetFileAttributesW":
        ["GetFileAttributesHookFunction", "post"],
    "kernel32.dll!GetFileAttributesA":
        ["GetFileAttributesHookFunction", "post"],
    "kernel32.dll!CheckRemoteDebuggerPresent":
        ["CheckRemoteDebuggerPresentHookFunction", "post"],
    "ntdll.dll!NtQueryInformationProcess":
        ["NtQueryInformationProcessHookFunction", "post"],
    "kernel32.dll!GetDiskFreeSpaceExA":
        ["GetDiskFreeSpaceExHookFunction", "pre"],
    "kernel32.dll!GetDiskFreeSpaceExW":
        ["GetDiskFreeSpaceExHookFunction", "pre"],
    "kernel32.dll!GlobalMemoryStatusEx":
        ["GlobalMemoryStatusExHookFunction", "post"],
    "setupapi.dll!SetupDiGetClassDevsW":
        ["SetupDiGetClassDevsHookFunction", "pre"],
    "setupapi.dll!SetupDiGetClassDevsA":
        ["SetupDiGetClassDevsHookFunction", "pre"],
    "kernel32.dll!DeviceIoControl":
        ["DeviceIoControlHookFunction", "post"],
    "ntdll.dll!NtQuerySystemInformation":
        ["NtQuerySystemInformationHookFunction", "post"],
    "user32.dll!GetCursorPos":
        ["GetCursorPosHookFunction", "post"],
    "advapi32.dll!RegQueryValueExA":
        ["RegQueryValueExHookFunction", "post"],
    "advapi32.dll!RegQueryValueExW":
        ["RegQueryValueExHookFunction", "post"],
    "advapi32.dll!RegOpenKeyExA":
        ["RegOpenKeyExHookFunction", "post"],
    "advapi32.dll!RegOpenKeyExW":
        ["RegOpenKeyExHookFunction", "post"],
    "iphlpapi.dll!GetAdaptersInfo":
        ["GetAdaptersInfoHookFunction", "post"],
    "kernel32.dll!CreateToolhelp32Snapshot":
        ["CreateToolhelp32Snapshot", "post"],
    "kernel32.dll!Process32FirstW":
        ["Process32FirstW", "post"],
    "kernel32.dll!Process32NextW":
        ["Process32NextW", "post"]
}
