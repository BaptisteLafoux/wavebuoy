#!/bin/bash

# 1: IP adress with opened port 5500 
# 2: time befort starting experiments (in seconds)
# 3: duration of experiments (in seconds)

adb -s $1 shell input keyevent KEYCODE_WAKEUP # wakes up phone
adb -s $1 shell input swipe 200 900 200 300 # swipe up to unlock 
adb -s $1 shell input text 01012000 # type code 
