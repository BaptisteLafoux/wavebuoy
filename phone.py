from cst import *
import requests
import pprint; pp = pprint.PrettyPrinter(indent=2)

class Phone():

    def __init__(self, id) -> None:
        self.id = id
        self.ip = f'{IP_BASE}.{id}'
        self.url = f'http://{self.ip}:{PHYPHOX_PORT}'

    def clear(self):
        with requests.get(f'{self.url}/control?cmd=clear') as response:
            print(f'\t\t[#{self.id}] >>  Clearing phone buffers')
            return response.json()

    def start(self):
        with requests.get(f'{self.url}/control?cmd=start'):
            print(f'\t\t[#{self.id}] >>  Starting acquisition')

    def clear(self):
        with requests.get(f'{self.url}/control?cmd=clear'):
            print(f'\t\t[#{self.id}] >>  Clearing phone buffers')



    def send_custom(self, request, show_response=False):
        with requests.get(f'{self.url}/{request}') as response:
            print(f'\t\t[#{self.id}] >>  Sending: "{request}"')

            print('Got response: ')
            pp.pprint(response.json())

            return(response.json())
        
    def run_experiment(self):
        self.clear() 
        self.start()
