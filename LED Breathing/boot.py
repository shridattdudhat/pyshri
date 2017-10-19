from machine import Pin
import time
from machine import PWM
import math

# create an I/O pin in output mode
p = Pin('P9', Pin.OUT)
pwm = PWM(0, frequency=5000)

myfloat = 0
fade = 0.01

while True:

    myfloat=myfloat+fade
    pwm_p = pwm.channel(0, pin='P9', duty_cycle=myfloat)
    time.sleep(0.01)

    if (myfloat<=0 or myfloat>=1):
        fade=-fade