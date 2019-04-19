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
# A basic package header, B: 1 byte for the deviceId, B: 1 byte for the pkg size
_LORA_PKG_FORMAT = "BB%ds"
_LORA_PKG_ACK_FORMAT = "BBB"
DEVICE_ID = 0x01
# Open a Lora Socket, use tx_iq to avoid listening to our own messages
lora = LoRa(mode=LoRa.LORA, tx_iq=True, region=LoRa.EU868)
l = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
l.setblocking(False)

while (True):
    coord = l76.coordinates()
    #f.write("{} - {}\n".format(coord, rtc.now()))
    # Package send containing a simple string
    #s.send("{}".format(coord))
    l.send("coord")
    #print("{} - {}".format(coord, rtc.now()))
    time.sleep(5)
