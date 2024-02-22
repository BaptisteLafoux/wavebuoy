#!/bin/sh

# 1. get current time on computer 
# 2. send a request for current time on phone 
# 2bis. time the request 2.
# 3. get current time on computer 

# returns 4 times :
    # - t1 (on computer)
    # - t2 (on phone)
    # - dt3 (time taken to execute \$EPOCHREALTIME command on phone)
    # - t4 (on computer)
    
# "$1" is either the serial number or the IP:port of a phone 


{ gdate +%s.%N && adb -s $1 shell /system/bin/time -p echo \$EPOCHREALTIME && gdate +%s.%N; } 2>&1 | \
awk 'NR==1 || NR==2 || NR==6 || /real/ {if ($1 == "real") {getline; print $2} else {print $1}}'



