import time
from GreenPonik_TSL2561 import GreenPonik_TSL2561

if __name__ == "__main__":
    tsl = GreenPonik_TSL2561()
    while True:
        data = tsl.read_tsl2561()
        print(data)
        time.sleep(1)
