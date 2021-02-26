#! /usr/bin/env python3

"""
####################################################################
####################################################################
####################### GreenPonik_SHT40 ##########################
####################### Read SHT40 sensor #########################
#################### with Python3 through i2c ######################
####################################################################
####################################################################
"""

from adafruit_extended_bus import ExtendedI2C as I2C
import adafruit_sht4x
import time


class SHT40:
    # TODO add compatibility to use it with the with statement
    DEFAULT_ADDR = 0x44
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

    def read_sht40(self):
        """
        @brief Read sht40 raspberry pi i2c bus
        Get temperatue, humidity
        """
        try:
            with I2C(self._bus) as i2c:
                sht = adafruit_sht4x.SHT4x(i2c)
                sht.mode = adafruit_sht4x.Mode.NOHEAT_HIGHPRECISION
                time.sleep(1)
                temperature, humidity = sht.measurements
                if self._debug:
                    print("Temperature: %.3f °c" % temperature)
                    print("Humidity: %.3f %%" % humidity)
                return temperature, humidity
        except Exception as e:
            print("cannot read sht40, An exception occurred: {}".format(e))
