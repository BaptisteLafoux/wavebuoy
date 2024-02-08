#!/bin/bash

<<<<<<< HEAD
# 1: IP adress with opened port 5500, or phone identifier (from 'adb devices')
=======
# 1: IP adress with opened port 5500
>>>>>>> e68115b14a84ab47abc8b02015a1cb59cd260f0c
# 2: time befort starting experiments (in seconds)
# 3: duration of experiments (in seconds)

adb -s $1 shell input tap 1020 205 # click on menu
adb -s $1 shell input tap 965 600 # click on Activate run with delay button
adb -s $1 shell input tap 130 1130
adb -s $1 shell input tap 830 860
adb -s $1 shell input keyevent --longpress $(printf 'KEYCODE_DEL %.0s' {1..250})
adb -s $1 shell input text $2 # fill in time before start
adb -s $1 shell input tap 860 700
adb -s $1 shell input keyevent --longpress $(printf 'KEYCODE_DEL %.0s' {1..250})
adb -s $1 shell input text $3 # fill in acquisiton time
adb -s $1 shell input tap 910 1500
