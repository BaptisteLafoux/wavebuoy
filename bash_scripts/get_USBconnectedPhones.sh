#!/bin/bash

output_file=bash_scripts/output.csv

echo "ID, IP" > $output_file
#nphones=$(adb devices | wc -l) 

adb devices | grep -v '192.168' | wc -l

adb devices | tail -n +2 | while read -r id _ 
do 
    ip_output=$(adb -s "$id" shell ip -f inet addr show)
    if [[ $ip_output = *192.168.* ]]
    then
        adb -s "$id" shell ip -f inet addr show 
        # $($ip_output | grep -A '192.168.')
    else
        echo 'Wifi hostpot is off on phone '$id''
    fi
    
done 