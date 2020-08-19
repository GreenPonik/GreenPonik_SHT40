[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_BH1750&metric=alert_status)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_BH1750)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_BH1750&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_BH1750)

[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_BH1750&metric=ncloc)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_BH1750)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_BH1750&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_BH1750)

[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_BH1750&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_BH1750)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_BH1750&metric=security_rating)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_BH1750)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_BH1750&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_BH1750)


![Upload Python Package](https://github.com/GreenPonik/GreenPonik_BH1750/workflows/Upload%20Python%20Package/badge.svg?event=release)
![Python package](https://github.com/GreenPonik/GreenPonik_BH1750/workflows/Python%20package/badge.svg?event=push)


## GreenPonik_BH1750.py Library for Raspberry pi
---------------------------------------------------------
This is the sample code for read light with BH1750 sensor.


## Table of Contents

- [GreenPonik_BH1750.py Library for Raspberry pi](#GreenPonikBH1750py-library-for-raspberry-pi)
- [Table of Contents](#table-of-contents)
- [Installation](#installation)
- [Methods](#methods)
- [Examples](#examples)
- [Credits](#credits)


## Installation
```shell
> git clone https://github.com/GreenPonik/GreenPonik_BH1750.git
cd GreenPonik_BH1750
pip3 install -r requirements.txt

or 

> pip3 install greenponik-bh1750
```
```Python

from GreenPonik_BH1750 import GreenPonik_BH1750

```

## Methods

```python
"""
Get light data
"""
def read_bh1750():

```

## Example
```Python
import time
from GreenPonik_BH1750 import GreenPonik_BH1750

if __name__ == "__main__":
    try:
        bh = GreenPonik_BH1750()
        while True:
            lux = bh.read_bh1750()
            print(lux)
            time.sleep(1)
    except Exception as e:
        print('An exception occurred: {}'.format(e))
```

## Credits
Write by Mickael Lehoux, from [GreenPonik](https://www.greenponik.com), 2019
