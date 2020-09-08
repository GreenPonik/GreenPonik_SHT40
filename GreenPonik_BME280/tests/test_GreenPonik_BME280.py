# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import sys
import unittest
from unittest.mock import patch


class SmbusMock():
    pass


class FCNTLMock:
    def __init__(self):
        pass

    def ioctl():
        pass


sys.modules["fcntl"] = FCNTLMock()
sys.modules["smbus"] = SmbusMock()


class Test_GreenPonik_BME280(unittest.TestCase):
    @patch("GreenPonik_BME280.GreenPonik_BME280")
    def test_read_bme280(self, Mock):
        bme = Mock()
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
