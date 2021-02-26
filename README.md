[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_SHT40&metric=alert_status)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_SHT40)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_SHT40&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_SHT40)

[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_SHT40&metric=ncloc)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_SHT40)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_SHT40&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_SHT40)

[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_SHT40&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_SHT40)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_SHT40&metric=security_rating)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_SHT40)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_SHT40&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_SHT40)


![Upload Python Package](https://github.com/GreenPonik/GreenPonik_SHT40/workflows/Upload%20Python%20Package/badge.svg?event=release)
![Python package](https://github.com/GreenPonik/GreenPonik_SHT40/workflows/Python%20package/badge.svg?event=push)


## GreenPonik_SHT40.py Library for Raspberry pi
---------------------------------------------------------
This is the sample code for read light with SHT40 sensor.


## Table of Contents

- [Installation](#installation)
- [Methods](#methods)
- [Examples](#example)
- [Credits](#credits)


## Installation
```shell
> git clone https://github.com/GreenPonik/GreenPonik_SHT40.git
cd GreenPonik_SHT40
pip3 install -r requirements.txt

or 

> pip3 install greenponik-sht40
```
```Python

from GreenPonik_SHT40.SHT40 import SHT40

```

## Methods

```python
"""
Get light data
"""
def read_sht40():

```

## Example
```Python
import time
from GreenPonik_SHT40.SHT40 import SHT40

if __name__ == "__main__":
    try:
        sht = SHT40()
        while True:
            data = sht.read_sht40()
            print("temperature: %.2f / humidity: %.2f" % (data[0], data[1]))
            time.sleep(1)
    except Exception as e:
        print('An exception occurred: {}'.format(e))

```

## Credits
Code by Mickael Lehoux, from [GreenPonik](https://www.greenponik.com), 2021
