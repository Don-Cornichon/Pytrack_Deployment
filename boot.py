### Wifi connection
import machine
from network import WLAN
####Sigfox configuration
from network import Sigfox
import socket
### GPS Location
from machine import UART
import machine
import os

### SIGFOX ###
#RCZ1=Europe
sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ1)
s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)
s.setblocking(True)
s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False)
#s.send("Wake_up")


### Wifi connection
wlan = WLAN(mode=WLAN.STA)
nets = wlan.scan()
for net in nets:
    if net.ssid == 'Alcouffe_Home':
        print('Network found!')
        wlan.connect(net.ssid, auth=(net.sec, '1989198493160'), timeout=5000)
        while not wlan.isconnected():
            machine.idle() # save power while waiting
        print('WLAN connection succeeded!')
        break

### GPS Location
uart = UART(0, baudrate=115200)
os.dupterm(uart)

machine.main('main.py')
