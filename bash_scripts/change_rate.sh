#!/bin/bash

phyphox_file="accelero_gyro_magneto_gps.phyphox"

adb -s $1 pull /storage/self/primary/Download/$phyphox_file
sed -i "" -E "s/rate=\"[0-9]+(\.[0-9]+)?\"/rate=\"$2\"/g" "$phyphox_file"
adb -s $1 push $phyphox_file /storage/self/primary/Download
# rm $phyphox_file

# adb -s $1 shell am force-stop de.rwth_aachen.phyphox
# adb -s $1 shell am start --user 0 -a android.intent.action.VIEW -d file:///storage/self/primary/Download/$phyphox_file -t audio/wav -p de.rwth_aachen.phyphox
# adb shell am start -d file:///storage/self/primary/Download/$phyphox_file -t image/jpg -p de.rwth_aachen.phyphox
# adb shell am start -d file:///storage/self/primary/Download/$phyphox_file -t image/jpg
adb -s $1 shell am start --user 0 -a android.intent.action.VIEW -d file:///storage/self/primary/Download/$phyphox_file -t image/jpg