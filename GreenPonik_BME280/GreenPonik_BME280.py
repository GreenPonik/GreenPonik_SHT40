#! /usr/bin/env python3

"""
####################################################################
####################################################################
####################### GreenPonik_BME280 ##########################
####################### Read BME280 sensor #########################
#################### with Python3 through i2c ######################
####################################################################
####################################################################
"""

from adafruit_extended_bus import ExtendedI2C as I2C
# import board
# import busio
import adafruit_bme280
import time


class GreenPonik_BME280:

    DEFAULT_ADDR = 0x76
    DEFAULT_BUS = 1

    def __init__(self, bus=None):
        # self._scl_pin = scl_pin if None is not scl_pin else board.SCL
        # self._scl_pin = scl_pin if None is not scl_pin else board.SCL
        self._bus = bus if None is not bus else self.DEFAULT_BUS

    @property
    def bus(self):
        return self._bus

    # @property
    # def scl_pin(self):
    #     return self._scl_pin

    # @property
    # def sda_pin(self):
    #     return self._sda_pin

    def read_bme280(self, addr=DEFAULT_ADDR):
        self._humidity_compensation = 13
        self._temperature_compensation = 3
        try:
            # Create library object using our Bus I2C port
            # i2c = busio.I2C(self._scl_pin, self._sda_pin)
            i2c = I2C(self._bus)
            bme280 = adafruit_bme280.Adafruit_BME280_I2C(
                i2c,
                self.DEFAULT_ADDR
            )

            # OR create library object using our Bus SPI port
            # spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
            # bme_cs = digitalio.DigitalInOut(board.D10)
            # bme280 = adafruit_bme280.Adafruit_BME280_SPI(spi, bme_cs)

            # Change this to match the location's pressure (hPa) at sea level
            bme280.sea_level_pressure = 1013.25
            bme280.mode = adafruit_bme280.MODE_NORMAL
            bme280.standby_period = adafruit_bme280.STANDBY_TC_500
            bme280.iir_filter = adafruit_bme280.IIR_FILTER_X16
            bme280.overscan_pressure = adafruit_bme280.OVERSCAN_X16
            bme280.overscan_humidity = adafruit_bme280.OVERSCAN_X1
            bme280.overscan_temperature = adafruit_bme280.OVERSCAN_X2
            # The sensor will need a moment to gather initial readings
            time.sleep(1)
            temperature = bme280.temperature - self._temperature_compensation
            humidity = bme280.humidity + self._humidity_compensation
            print("Temperature: %.3f C" % temperature)
            print("Humidity: %.3f %%" % humidity)
            print("Pressure: %.3f hPa" % bme280.pressure)
            print("Altitude: %.3f meters" % bme280.altitude)
            i2c.deinit()
            return (temperature, humidity, bme280.pressure, bme280.altitude)
        except BaseException as e:
            print("cannot read bme280")
            print("An exception occurred: {}".format(e))
