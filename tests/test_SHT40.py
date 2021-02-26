# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import sys
import unittest
from unittest.mock import patch


class SmbusMock:
    # simultate the smbus method just for tests
    pass


class FCNTLMock:
    def ioctl(self):
        # simultate the FCNTL.ioctl method just for tests
        pass


sys.modules["fcntl"] = FCNTLMock()
sys.modules["smbus"] = SmbusMock()


class TestSHT40(unittest.TestCase):
    @patch("GreenPonik_SHT40.SHT40.SHT40")
    def test_read_sht40(self, mock_sht40):
        sht = mock_sht40()
        expected = [21.8, 62.3]
        sht.read_sht40.return_value = expected
        readed = sht.read_sht40()
        self.assertIsNotNone(readed)
        self.assertTrue(len(readed) == 2)
        self.assertTrue(type(readed).__name__ == "list")
        self.assertTrue(isinstance(readed[0], float))
        self.assertTrue(isinstance(readed[1], float))


if __name__ == "__main__":
    unittest.main()
