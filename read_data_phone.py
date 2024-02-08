from phone import Phone
from cst import *

if __name__ == "__main__":
    phones = [Phone(id) for id in ID_LUT]

    [phone.run_experiment(300) for phone in phones]
