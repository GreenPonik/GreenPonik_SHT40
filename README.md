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
<snippet>
<content>

## Installation
```shell
git clone https://github.com/GreenPonik/GreenPonik_TSL2561.git
cd GreenPonik_TSL2561
pip3 install -r requirements.txt

```
```Python

from GreenPonik_TSL2561 import read_tsl2561

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
from GreenPonik_TSL2561 import read_tsl2561


if __name__ == "__main__":
    while True:
        read_tsl2561()
        time.sleep(1)
    pass
```

## Credits
Write by Mickael Lehoux, from [GreenPonik](https://www.greenponik.com), 2019
