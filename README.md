[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_BME280&metric=alert_status)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_BME280)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_BME280&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_BME280)

[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_BME280&metric=ncloc)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_BME280)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_BME280&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_BME280)

[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_BME280&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_BME280)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_BME280&metric=security_rating)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_BME280)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_BME280&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_BME280)


![Upload Python Package](https://github.com/GreenPonik/GreenPonik_BME280/workflows/Upload%20Python%20Package/badge.svg?event=release)
![Python package](https://github.com/GreenPonik/GreenPonik_BME280/workflows/Python%20package/badge.svg?event=push)


## GreenPonik_BME280.py Library for Raspberry pi
---------------------------------------------------------
This is the sample code for read light with BME280 sensor.


## Table of Contents

- [GreenPonik_BME280.py Library for Raspberry pi](#GreenPonikBME280py-library-for-raspberry-pi)
- [Table of Contents](#table-of-contents)
- [Installation](#installation)
- [Methods](#methods)
- [Examples](#examples)
- [Credits](#credits)


## Installation
```shell
> git clone https://github.com/GreenPonik/GreenPonik_BME280.git
cd GreenPonik_BME280
pip3 install -r requirements.txt

or 

> pip3 install greenponik-bme280
```
```Python

from GreenPonik_BME280 import GreenPonik_BME280

```

## Methods

```python
"""
Get light data
"""
def read_bme280():

```

## Example
```Python
import time
from GreenPonik_BME280 import GreenPonik_BME280

if __name__ == "__main__":
    try:
        bme = GreenPonik_BME280()
        while True:
            data = bme.read_bme280()
            print(data)
            time.sleep(1)
    except Exception as e:
        print('An exception occurred: {}'.format(e))

```

## Credits
Write by Mickael Lehoux, from [GreenPonik](https://www.greenponik.com), 2019
