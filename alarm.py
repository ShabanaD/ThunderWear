#alarm
import datetime
import mraa
import time

import json

#outfit chooser
from Outfit import *

#weather finder
from Weather import *

#email
import emailBot

w = Weather("toronto", "canada")
wDict = w.getDict()
print(wDict)

o = Outfit(wDict)
print(o.outfit)

buzz = mraa.Gpio(31)
button = mraa.Gpio(29)

buzz.dir(mraa.DIR_OUT)
button.dir(mraa.DIR_IN)

buzz.write(0)

def alarm(Atime):
    while datetime.timedelta(seconds=0) < Atime - datetime.datetime.now():
        time.sleep(1)
    
    emailBot.send(w.getEmailMsg(), o.outfit)
    buzz.write(1)



now = datetime.datetime.now()
alarm(now+datetime.timedelta(seconds=5))
while True:
    PressButton = int(button.read())
    if (PressButton == 1):
        buzz.write(0)
        break
