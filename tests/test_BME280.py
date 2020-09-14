# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import sys
import unittest
from unittest.mock import patch


class SmbusMock():
    # simultate the smbus method just for tests
    pass


class FCNTLMock:
    def ioctl(self):
        # simultate the FCNTL.ioctl method just for tests
        pass


sys.modules["fcntl"] = FCNTLMock()
sys.modules["smbus"] = SmbusMock()


class TestBME280(unittest.TestCase):
    @patch("GreenPonik_BME280.BME280.BME280")
    def test_read_bme280(self, mock_bme280):
        bme = mock_bme280()
        expected = [21.8, 62.3, 1014.5, 426.37]
        bme.read_bme280.return_value = expected
        readed = bme.read_bme280()
        self.assertIsNotNone(readed)
        self.assertTrue(len(readed) == 4)
        self.assertTrue(type(readed).__name__ == "list")
        self.assertTrue(isinstance(readed[0], float))
        self.assertTrue(isinstance(readed[1], float))
        self.assertTrue(isinstance(readed[2], float))
        self.assertTrue(isinstance(readed[3], float))


if __name__ == "__main__":
    unittest.main()
