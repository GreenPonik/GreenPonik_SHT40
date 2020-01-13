import time
from GreenPonik_TSL2561 import read_tsl2561


if __name__ == "__main__":
    while True:
        read_tsl2561()
        time.sleep(1)
    pass