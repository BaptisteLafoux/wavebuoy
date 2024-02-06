

import matplotlib.pyplot as plt

from phone import Phone
from cst import *


if __name__ == "__main__":
    phones = [Phone(id) for id in ID_LUT]
    [phone.unlock() for phone in phones]
    [phone.launch_phyphox() for phone in phones]
    [phone.run_experiment(5) for phone in phones]

    # with Pool(2) as p:
    #     p.map(Phone.run_experiment, phones)

    print(phones[0].is_connected)

    fig, ax = plt.subplots()
    ax.plot()
    plt.show()

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
