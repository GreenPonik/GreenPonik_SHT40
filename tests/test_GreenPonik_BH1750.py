# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import sys
import unittest
from unittest.mock import patch, MagicMock


class BoardMock:
    def __init__(self):
        self._scl = 18
        self._sda = 15

    def SCL(self):
        return self._scl

    def SDA(self):
        return self._sda


class BusioMock(MagicMock()):
    def I2C(self, sda, scl):
        return True


sys.modules["board"] = BoardMock()
sys.modules["busio"] = BusioMock()


class TestGreenPonik_BH1750(unittest.TestCase):
    @patch("GreenPonik_BH1750.GreenPonik_BH1750.read_bh1750")
    def test_read_bh1750(self, MockBH):
        bh = MockBH()
        expected = 124.3
        bh.read_bh1750.return_value = expected
        readed = bh.read_bh1750()
        self.assertIsNotNone(readed)
        self.assertTrue(type(readed).__name__ == "float")


if __name__ == "__main__":
    unittest.main()
