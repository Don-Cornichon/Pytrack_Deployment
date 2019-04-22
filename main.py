import machine
import math
import network
import os
import time
import utime
import gc
from machine import RTC
from machine import SD
from L76GNSS import L76GNSS
from pytrack import Pytrack
### Lora
import socket
from network import LoRa



### GPS
time.sleep(2)
gc.enable()
# setup rtc
rtc = machine.RTC()
rtc.ntp_sync("pool.ntp.org")
utime.sleep_ms(750)
print('\nRTC Set from NTP to UTC:', rtc.now())
utime.timezone(7200)
print('Adjusted from UTC to EST timezone', utime.localtime(), '\n')
py = Pytrack()
l76 = L76GNSS(py, timeout=30)
# sd = SD()
# os.mount(sd, '/sd')
# f = open('/sd/gps-record.txt', 'w')


### LORA
lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)
l = socket.socket(socket.AF_LORA, socket.SOCK_RAW)


while True:
    l.setblocking(True)
    coord = l76.coordinates()
    #f.write("{} - {}\n".format(coord, rtc.now()))
    # Package send containing a simple string
    #s.send("{}".format(coord))
    #print('Gheu')
    #l.send(bytes(coord))
    #c = hex(coord)
    #c = coord.decode('utf-8')
    if coord != (None, None):
        #print("{}".format(coord))
        co = ("{}".format(coord))
        l.send(co)
        print("GPS location sended")
    else:
        print('no GPS datas found')
    #print("{}".format(coord))
    time.sleep(3)
