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
import adafruit_bme280
import time


class BME280:

    DEFAULT_ADDR = 0x76
    DEFAULT_BUS = 1

    def __init__(self, bus=None):
        self._bus = bus if None is not bus else self.DEFAULT_BUS

    @property
    def bus(self):
        return self._bus

    def read_bme280(self, addr=DEFAULT_ADDR):
        """
        @brief Read bme280 raspberry pi i2c bus
        Get temperatue, humidity, pressure, altitude
        """
        self._humidity_compensation = 13
        self._temperature_compensation = 3
        try:
            with I2C(self._bus) as i2c:
                bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, self.DEFAULT_ADDR)

                # Change this to match the location's
                # pressure (hPa) at sea level
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
                print("Temperature: %.3f °c" % temperature)
                print("Humidity: %.3f %%" % humidity)
                print("Pressure: %.3f hPa" % bme280.pressure)
                print("Altitude: %.3f meters" % bme280.altitude)
                return temperature, humidity, bme280.pressure, bme280.altitude
        except BaseException as e:
            print("cannot read bme280")
            print("An exception occurred: {}".format(e))
