#!/bin/bash

connected=bash_scripts/devices_connected
output_file=bash_scripts/output.csv

echo "ID, IP" > $output_file

tail -n +2 "$connected" | while FS=, read -r id _ 
do 
    echo "$id"
    ip_output=$(adb -s "$id" shell ip -f inet addr show)
    if [[ $ip_output = *192.168.* ]]
    then
        echo $($ip_output | grep -A '192.168.')
    else
        echo 'Wifi hostpot is off on phone '$id''
    fi
    
done 