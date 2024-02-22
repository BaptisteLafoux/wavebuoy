# Time synchonization examples 

In this folder, you will find an example of how to find time offset between two phones
- `tt1.csv` and `tt2.csv` are timetables obtained from `timesyn.py`, following an Network Time Protocol, they contain Series of : 
    - `t1` : Time of first `$EPOCHREALTIME` command on **computer** 
    - `t2` : Time of first `$EPOCHREALTIME` command on **phone**
    - `t3` : Time at which a response is sent from **phone** to **computer** 
    - `t4` : Time of last `$EPOCHREALTIME` command on **computer** 

    Each file corresponds to a phone 
> See [this Wikipedia article](https://fr.wikipedia.org/wiki/Network_Time_Protocol) for more details (section *NTP Client/Server*)

> See `bash_scripts/ntp_sequence.sh` to see how the NTP is actually implemented