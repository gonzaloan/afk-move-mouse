import os
import ctypes
import time

def afk_me():
    if os.name == 'nt':
        ES_CONTINUOUS = 0x80000000
        ES_SYSTEM_REQUIRED = 0x00000001
        ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | ES_SYSTEM_REQUIRED)
    elif os.name == 'posix':
        try:
            # Trying to use caffeinate in Mac
            os.system("caffeinate -disu &")
        except:
            try:
                # if not, we use linux
                os.system("xset s off")
                os.system("xset -dpms")
                os.system("xset s noblank")
            except:
                print("Could not prevent the system from going to sleep. I suck! :( ")
    else:
        print("shit happened, sorry, dude :( ")

while True:
    afk_me()
    time.sleep(60)