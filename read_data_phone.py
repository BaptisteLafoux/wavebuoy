import requests


import matplotlib.pyplot as plt 
from multiprocessing import Pool

from phone import Phone 
from cst import * 

import time 
if __name__=='__main__': 
    phones = [Phone(id) for id in ID_LUT]
    
    [phone.launch_phyphox() for phone in phones]
    # [phone.run_experiment(5) for phone in phones]

    plt.pause(1) 
    times = phones[1].send_custom('time?=full')
    print(times) 

    print(phones[0].is_connected)

    # phones[0].send_custom('control?cmd=start')

    
    # phone.send_custom('/control?cmd=set&status=timedRun&value=False')
    # [phone.send_custom('start?') for phone in phones]
    # [phone.clear() for phone in phones]
    # [phone.start() for phone in phones]

    # times = [phone.send_custom('time?=full') for phone in phones]

    # times[0]
    
    # var = 'accX'

    # url = f'{phone.url}/get?cmd=set&status=timedRun&value=False'#/get?{var}=5|acc_time'
    # f = requests.get(url)
    # pp.pprint(f.json())

    # data = f.json()['buffer'][var]['buffer']

    # fig, ax =plt.subplots() 

    # ax.plot(data, 'o')
    # plt.show()