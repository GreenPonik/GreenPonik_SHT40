#! /usr/bin/env python3

"""
####################################################################
####################################################################
####################### GreenPonik_BH1750 ##########################
####################### Read BH1750 sensor #########################
#################### with Python3 through i2c ######################
####################################################################
####################################################################
"""

import board
import busio


class GreenPonik_BH1750:
    # Constants taken from the datasheet
    DEVICE = 0x23       # Default device I2C address
    POWER_DOWN = 0x00   # No active state
    POWER_ON = 0x01     # Power on
    RESET = 0x07        # Reset data register value
    # Start measurement at 4 lx resolution. Time typically 16ms.
    CONTINUOUS_LOW_RES_MODE = 0x13
    # Start measurement at 1 lx resolution. Time typically 120ms
    CONTINUOUS_HIGH_RES_MODE_1 = 0x10
    # Start measurement at 0.5 lx resolution. Time typically 120ms
    CONTINUOUS_HIGH_RES_MODE_2 = 0x11
    # Start measurement at 1 lx resolution. Time typically 120ms
    # Device is automatically set to Power Down after measurement.
    ONE_TIME_HIGH_RES_MODE_1 = 0x20
    # Start measurement at 0.5 lx resolution. Time typically 120ms
    # Device is automatically set to Power Down after measurement.
    ONE_TIME_HIGH_RES_MODE_2 = 0x21
    # Start measurement at 1 lx resolution. Time typically 120ms
    # Device is automatically set to Power Down after measurement.
    ONE_TIME_LOW_RES_MODE = 0x23

    def _convert_to_number(self, data):
        # Simple function to convert 2 bytes of data
        # into a decimal number
        return ((data[1] + (256 * data[0])) / 1.2)

    def read_bh1750(self, addr=DEVICE):
        try:
            # bus = smbus.SMBus(0)    # Rev 1 Pi uses 0
            # bus = smbus.SMBus(1)    # Rev 2 Pi uses 1
            # data = bus.read_i2c_block_data(addr, self.ONE_TIME_HIGH_RES_MODE_2)
            # lux = self._convertToNumber(data)
            i2c = busio.I2C(board.SCL, board.SDA)
            buffer = bytearray(1)
            bh = i2c.readfrom_into(addr, buffer, self.ONE_TIME_HIGH_RES_MODE_2)
            print(bh)
            lux = bh

            print('light: %.3f lx' % lux)
            return lux
        except BaseException as e:
            print('cannot read bh1750')
            print('An exception occurred: {}'.format(e))
