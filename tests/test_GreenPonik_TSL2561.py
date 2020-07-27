# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from GreenPonik_TSL2561 import read_tsl2561


class TestGreenPonik_2561(unittest.TestCase):

    def test_read_tsl2561(self):
        self.assertListEqual(read_tsl2561())


if __name__ == '__main__':
    unittest.main()
