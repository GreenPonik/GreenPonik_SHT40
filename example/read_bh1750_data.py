import time
from GreenPonik_BH1750 import GreenPonik_BH1750

if __name__ == "__main__":
    try:
        bh = GreenPonik_BH1750()
        while True:
            lux = bh.read_bh1750()
            print(lux)
            time.sleep(1)
    except Exception as e:
        print('An exception occurred: {}'.format(e))
