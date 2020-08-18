[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_TSL2561&metric=alert_status)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_TSL2561)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_TSL2561&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_TSL2561)

[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_TSL2561&metric=ncloc)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_TSL2561)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_TSL2561&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_TSL2561)

[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_TSL2561&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_TSL2561)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_TSL2561&metric=security_rating)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_TSL2561)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=GreenPonik_GreenPonik_TSL2561&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=GreenPonik_GreenPonik_TSL2561)


![Upload Python Package](https://github.com/GreenPonik/GreenPonik_TSL2561/workflows/Upload%20Python%20Package/badge.svg?event=release)
![Python package](https://github.com/GreenPonik/GreenPonik_TSL2561/workflows/Python%20package/badge.svg?event=push)


## GreenPonik_TSL2561.py Library for Raspberry pi
---------------------------------------------------------
This is the sample code for read light with TSL2561 sensor.


## Table of Contents

- [GreenPonik_TSL2561.py Library for Raspberry pi](#GreenPoniktsl2561py-library-for-raspberry-pi)
- [Table of Contents](#table-of-contents)
- [Installation](#installation)
- [Methods](#methods)
- [Examples](#examples)
- [Credits](#credits)


## Installation
```shell
> git clone https://github.com/GreenPonik/GreenPonik_TSL2561.git
cd GreenPonik_TSL2561
pip3 install -r requirements.txt

or 

> pip3 install greenponik-tsl2561
```
```Python

from GreenPonik_TSL2561 import GreenPonik_TSL2561

```

## Methods

```python
"""
Get light data
"""
def read_tsl2561():

```

## Example
```Python
import time
from GreenPonik_TSL2561 import GreenPonik_TSL2561

if __name__ == "__main__":
    tsl = GreenPonik_TSL2561()
    while True:
        data = tsl.read_tsl2561()
        print(data)
        time.sleep(1)
```

## Credits
Write by Mickael Lehoux, from [GreenPonik](https://www.greenponik.com), 2019
