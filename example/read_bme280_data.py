import time
from GreenPonik_BME280.BME280 import BME280

if __name__ == "__main__":
    try:
        bme = BME280()
        while True:
            data = bme.read_bme280()
            print(data)
            time.sleep(1)
    except Exception as e:
        print('An exception occurred: {}'.format(e))
