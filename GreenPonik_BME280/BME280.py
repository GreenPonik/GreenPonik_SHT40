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

    def __init__(self, bus=DEFAULT_BUS, addr=DEFAULT_ADDR):
        self._bus = bus
        self._addr = addr
        self._debug = False

    def __enter__(self):
        """Context manager enter function."""
        # Just return this object so it can be used in a with statement, like
        # with WaterPumpDriver(bus=1, addr=100) as driver:
        #     # do stuff!
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit function, ensures resources are cleaned up."""
        return False  # Don't suppress exceptions.

    @property
    def bus(self):
        return self._bus

    @property
    def address(self):
        return self._addr

    @property
    def debug(self):
        return self._debug

    @debug.setter
    def debug(self, d):
        self._debug = d

    def read_bme280(self):
        """
        @brief Read bme280 raspberry pi i2c bus
        Get temperatue, humidity, pressure, altitude
        """
        self._humidity_compensation = 13
        self._temperature_compensation = 3
        try:
            with I2C(self._bus) as i2c:
                bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, self._addr)
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
                if self._debug:
                    print("Temperature: %.3f °c" % temperature)
                    print("Humidity: %.3f %%" % humidity)
                    print("Pressure: %.3f hPa" % bme280.pressure)
                    print("Altitude: %.3f meters" % bme280.altitude)
                return temperature, humidity, bme280.pressure, bme280.altitude
        except Exception as e:
            print("cannot read bme280, An exception occurred: {}".format(e))
