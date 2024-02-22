import subprocess
import tqdm
import matplotlib.pyplot as plt
from cst import *
import pandas as pd


def batch_ntp(phoneA, phoneB="local", nrequests=100):
    """
    Do the Network Time Protocol between a phone and the computer (if phone B=="local") or between two phones.
    See https://fr.wikipedia.org/wiki/Network_Time_Protocol for more info on NTP

    ### Returns:
    -
    """
    timetable_A = pd.DataFrame()
    timetable_B = pd.DataFrame()

    for _ in tqdm.tqdm(range(nrequests)):

        timetable_A = pd.concat([timetable_A, ntp(phoneA)])
        if not phoneB == "local":
            timetable_B = pd.concat([timetable_B, ntp(phoneB)])

    return timetable_A if phoneB == "local" else (timetable_A, timetable_B)


def ntp(phone):
    # here ntp_sequence.sh return 4 numbers : T1, T'1, dT'2, T2
    response = subprocess.run(
        ["bash_scripts/ntp_sequence.sh", phone.ip], capture_output=True, text=True
    )
    t = [
        float(elem) for elem in response.stdout.split("\n")[:-1]
    ]  # last element is an empty string
    t[2] = t[2] + t[1]  # T'2 = T'1 + dT'2

    return pd.DataFrame([t], columns=["t1", "t2", "t3", "t4"])


if __name__ == "__main__":
    from phone import Phone

    ps = [Phone(ID) for ID in ID_LUT]

    tt1, tt2 = batch_ntp(ps[0], ps[1], nrequests=7500)

    tt1.to_csv("timesync/tt1.csv")
    tt2.to_csv("timesync/tt2.csv")
