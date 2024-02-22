#!/bin/bash

# 1: IP adress with opened port 5500, or phone identifier (from 'adb devices')

adb -s $1 shell am force-stop com.android.settings > /dev/null 2>&1
adb -s $1 shell am start -n com.android.settings/.TetherSettings > /dev/null 2>&1
adb -s $1 shell input keyevent 20 
adb -s $1 shell input keyevent 66
adb -s $1 shell am force-stop com.android.settings
