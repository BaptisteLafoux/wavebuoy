import pprint

import requests

from cst import ADB_PORT, BASH_SCRIPTS_PATH, IP_BASE, PHYPHOX_PORT

pp = pprint.PrettyPrinter(indent=2)
import subprocess
import time
from subprocess import DEVNULL


class Phone:
    def __init__(self, id) -> None:
        self.id = id

        self.ip = f"{IP_BASE}.{id}"
        self.url = f"http://{self.ip}:{PHYPHOX_PORT}"

        print(f"[#{self.id}] Initializing... Connected: {self.is_connected}")

    @property
    def is_connected(self):
        ret = subprocess.run(
            ["ping", self.ip, "-n", "1"],
            text=False,
            capture_output=False,
            stdout=DEVNULL,
            stderr=DEVNULL,
        )
        return ret != 0

    def launch_phyphox(self):
        subprocess.run(
            [
                "adb",
                "-s",
                f"{self.ip}:{ADB_PORT}",
                "shell",
                "monkey",
                "-p",
                "de.rwth_aachen.phyphox",
                "-c",
                "android.intent.category.LAUNCHER",
                "1",
            ],
            text=False,
            capture_output=False,
            stdout=DEVNULL,
            stderr=DEVNULL,
        )

    def get_start_time(self):
        self.start_time = self.send_custom("time?=full")[0]["systemTime"]

    def unlock(self):
        print("Unlocking phone")
        subprocess.run(["bash", f"{BASH_SCRIPTS_PATH}/unlock.sh", f"{self.ip}:{ADB_PORT}"])
        time.sleep(3)

    def activate_timedRun(self, t_before: int = 1, t_run: int = 100):
        print(
            f"Activating timed run with :\n\t- Delay before start:\t{t_before} s\n\t- Experiment duration:\t{t_run} s"
        )
        subprocess.run(
            [
                "bash",
                f"{BASH_SCRIPTS_PATH}/activate_timedRun.sh",
                f"{self.ip}:{ADB_PORT}",
                f"{t_before}",
                f"{t_run}",
            ]
        )
        time.sleep(10)

    def connect(self):
        print(f">> [#{self.id}] Initializing connexion...")
        ret = subprocess.run(
            ["adb", "connect", f"{self.ip}:{ADB_PORT}"],
            text=False,
            capture_output=False,
            stdout=DEVNULL,
            stderr=DEVNULL,
        )
        if ret != 0:
            print("Connexon successful ! ")

    def clear_buffers(self):
        with requests.get(f"{self.url}/control?cmd=clear") as response:
            print(f"\t\t[#{self.id}] >>  Clearing phone buffers")
            return response.json()

    def start(self):
        with requests.get(f"{self.url}/control?cmd=start"):
            print(f"\t\t[#{self.id}] >>  Starting acquisition")

    def stop(self):
        with requests.get(f"{self.url}/control?cmd=stop"):
            print(f"\t\t[#{self.id}] >>  Stopping acquisition")

    def send_custom(self, request: str, show_response: bool = False):
        """Sends a customized request to a phone.

        Args:
            - request (str): the text of the request
            - show_response (bool, optional): Show in terminal the response obtain to the request. Defaults to False.
        """
        with requests.get(f"{self.url}/{request}") as response:
            if show_response:
                print(f'\t\t[#{self.id}] >>  Sending: "{request}"')
                print("Got response: ")
                pp.pprint(response.json())

            return response.json()

    def run_experiment(self, acq_time):
        print(f"###########################\n[#{self.id}] >> Starting experiment\n")
        # exp = Experiment()

        time.sleep(1)
        self.clear_buffers()
        self.start()

        time.sleep(1)

        self.stop()

        # while self.is_running:
