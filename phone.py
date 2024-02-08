from cst import *
import requests
import pprint; pp = pprint.PrettyPrinter(indent=2)
import time 
import subprocess
import os 
from subprocess import DEVNULL, STDOUT
import pandas as pd 
import numpy as np 
from datetime import datetime as dt 
import re 

class Phone():
    def __init__(self, id) -> None:
        self.id = id
        self.ip = f'{IP_BASE}.{id}'
        self.url = f'http://{self.ip}:{PHYPHOX_PORT}'
        
        print(f'[#{self.id}] Initializing... Available on network: {self.is_available}')

    @property
    def is_available(self):
        """WRONG !! 

        Returns:
            _type_: _description_
        """
        try: 
            self.send_custom('config?', show_response=False, get_response=False)
            print('Connexion with phone working')
            return True
        except:
            print('Phone not connected')
            return False 
    
    @property
    def is_running(self):
        req = self.send_custom('get?')['status']
        is_running =  req['measuring']
        if is_running: 
            if req['timedRun']:
                print(f"Timed run -\t Remaining : {req['countDown']/1000:.2f} s")
            else:
                print('Running in non-stop mode...')
        else: 
            print('Acquisition stopped')
        return is_running
    
    @property
    def start_time(self):
        return self.send_custom('time?=full')[0]['systemTime']
    
    def launch_phyphox(self):
        subprocess.run(['adb', '-s', f'{self.ip}:{ADB_PORT}', 'shell', 'monkey', '-p', 'de.rwth_aachen.phyphox', '-c', 'android.intent.category.LAUNCHER', '1'], text=False, capture_output=False, stdout=DEVNULL, stderr=DEVNULL)
        
    def unlock(self):
        print('Unlocking phone')
        subprocess.run(['bash', f'{BASH_SCRIPTS_PATH}/unlock.sh', f'{self.ip}:{ADB_PORT}'])
        time.sleep(3)

    def activate_timedRun(self, t_before: int=1, t_run: int=100):
        """Runs a bash file to does action on the phoe to activate the Timed Run optio (Fixed Experiment duration)

        Args:
            - t_before (int, optional): Delay before the start of an experiment, in seconds. Defaults to 1.
            - t_run (int, optional): Experiment duration, in seconds. Defaults to 100.
        """
        print(f'Activating timed run with :\n\t- Delay before start:\t{t_before} s\n\t- Experiment duration:\t{t_run} s')
        resp = subprocess.run(['bash', f'{BASH_SCRIPTS_PATH}/activate_timedRun.sh', f'{self.ip}:{ADB_PORT}', f'{t_before}', f'{t_run}'])

    def connect(self): 
        print(f'>> [#{self.id}] Initializing connexion...')
        ret = subprocess.run(['adb', 'connect', f'{self.ip}:{ADB_PORT}'], text=False, capture_output=False, stdout=DEVNULL, stderr=DEVNULL)
        if ret!=0: print('Connexon successful ! ')
        
    def clear_buffers(self):
        with requests.get(f'{self.url}/control?cmd=clear'):
            print(f'\t\t[#{self.id}] >>  Clearing phone buffers')

    def start(self):
        with requests.get(f'{self.url}/control?cmd=start'):
            print(f'\t\t[#{self.id}] >>  Starting acquisition')

    def stop(self):
        with requests.get(f'{self.url}/control?cmd=stop'):
            print(f'\t\t[#{self.id}] >>  Stopping acquisition')

    def send_custom(self, request: str, show_response: bool=False, get_response: bool=True):
        """Sends a customized request to a phone. 

        Args:
            - request (str): the text of the request 
            - show_response (bool, optional): Show in terminal the response obtained to the request. Defaults to False.
        """
        with requests.get(f'{self.url}/{request}') as response:
            if show_response:  
                print(f'\t\t[#{self.id}] >>  Sending: "{request}"')
                print('Got response: ')
                pp.pprint(response.json())

            if get_response: return response.json()

    def dump(self, vars=['acc']):
        dims = ['X', 'Y', 'Z', '_time']
        str_date = time.strftime("%d-%m-%Y>%H:%M:%S", time.gmtime(self.start_time))
        os.makedirs(os.path.join(DUMP, str_date)) 

        for var in vars: 
            dimD_vars = [f'{var}{dim}' for dim in dims]
            cmd = '&&'.join([f'{dimD_var}=full' for dimD_var in dimD_vars])
            raw_container = self.send_custom(f'get?{cmd}')

            data_array = np.array([raw_container['buffer'][dimD_var]['buffer'] for dimD_var in dimD_vars]).T
        
            df = pd.DataFrame(data_array, columns=dimD_vars)

            df[f'{var}_time_abs'] = [dt.fromtimestamp(t + self.start_time) for t in df[f'{var}_time']]

            df.to_csv(os.path.join(DUMP, str_date, f'{str_date}_{var}.csv'))
    
        
    def run_experiment(self, t_run):

        self.unlock()
        self.activate_timedRun(t_run=t_run)
        
        print(f"###########################\n[#{self.id}] >> Starting experiment\n")
        # exp = Experiment()
        
        self.clear_buffers() 
        self.start()
        time.sleep(2)
        while self.is_running:
            pass
        
        self.dump(vars=['acc', 'mag'])
