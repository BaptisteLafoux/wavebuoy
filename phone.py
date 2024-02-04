from cst import *
import requests
import pprint; pp = pprint.PrettyPrinter(indent=2)
import time 

class Phone():

    def __init__(self, id) -> None:
        self.id = id
        self.ip = f'{IP_BASE}.{id}'
        self.url = f'http://{self.ip}:{PHYPHOX_PORT}'

    def get_start_time(self):
        time.sleep(0.5)
        self.start_time = self.send_custom('time?=full')[0]['systemTime']

    def clear(self):
        with requests.get(f'{self.url}/control?cmd=clear') as response:
            print(f'\t\t[#{self.id}] >>  Clearing phone buffers')
            return response.json()

    def start(self):
        with requests.get(f'{self.url}/control?cmd=start'):
            print(f'\t\t[#{self.id}] >>  Starting acquisition')

    def stop(self):
        with requests.get(f'{self.url}/control?cmd=stop'):
            print(f'\t\t[#{self.id}] >>  Stoppig acquisition')

    def send_custom(self, request: str, show_response: bool=False):
        """Sends a customized requests to a phone. 

        Args:
            - request (str): the text of the request 
            - show_response (bool, optional): Show in terminal the response obtain to the request. Defaults to False.
        """
        with requests.get(f'{self.url}/{request}') as response:
            if show_response:  
                print(f'\t\t[#{self.id}] >>  Sending: "{request}"')
                print('Got response: ')
                pp.pprint(response.json())

            return(response.json())
        
    def run_experiment(self, acq_time):

        # exp = Experiment()
        self.clear() 
        self.start()

        self.get_start_time()

        while time.time() - self.start_time < acq_time:
            pass

        self.stop()

        # while self.is_running: 
