import time
from GreenPonik_SHT40.SHT40 import SHT40

if __name__ == "__main__":
    try:
        sht = SHT40()
        while True:
            data = sht.read_sht40()
            print("temperature: %.2f / humidity: %.2f" % (data[0], data[1]))
            time.sleep(1)
    except Exception as e:
        print('An exception occurred: {}'.format(e))
