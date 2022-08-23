from datetime import datetime
import platform
import subprocess
import pyautogui

n = datetime.now()
def cmdo(com):
    try:
        res=subprocess.check_output(com, shell=1)
    except:
        return '🖥❌'
        
    try:
        res=res.decode('utf8')
    except:
        try:
            res=res.decode('cp866')
        except:		return '🖥❌'
    return '🖥✅:\n'+res

proc = cmdo('powershell "Get-WmiObject -Class Win32_Processor | select Name"').split('\n')[4][:-2]
ram = int(cmdo('powershell "Get-WmiObject Win32_PhysicalMemory | Measure-Object -Property capacity -Sum"').split("\n")[5].split(': ')[1][:-1])//1073741824
vid = cmdo('powershell "Get-WmiObject Win32_VideoController | select Name"').split('\n')[4][:-1]
x,y=pyautogui.size()
banner = f"""
Name PC:   DESKTOP-V6HOJSM
System:      Windows 10
CPU:        11th Gen Intel(R) Core(TM) i5-11600K @ 3.90GH
GPU:        AMD Radeon RX 6500 XT
RAM:        16 GB
Screen:     1440x900
        """
print(banner)
print(datetime.now()-n)