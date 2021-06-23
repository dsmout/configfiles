#!/bin/python3
import socket
import psutil
from subprocess import check_output as co
from alsaaudio import Mixer
from datetime import datetime
from time import sleep
def getIP():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip

def getMem():
    mem = psutil.virtual_memory()[3]
    mynum = 1000000
    val = mem / mynum
    val = round(val)
    msg = str(val) + " MB"
    return msg

def getVol():
    m = Mixer()
    vol = m.getvolume()
    msg = str(vol[0]) + "%"
    return msg

def getMute():
    m = Mixer()
    mute = m.getmute()[0]
    if mute == 0:
        return "Mute off"
    else:
        return "Mute on"

def getTime():
    d = datetime.now()
    out = d.strftime("%a %d %b %y %H:%M:%S")
    return out

def main():
    while True:
        print(getIP(), getMem(), getVol() , getMute(), getTime())
        sleep(5)

if __name__ == "__main__":
    main()
