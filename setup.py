from setuptools import setup, find_packages
import pathlib
import os

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')


def load_version():
    version_file = os.path.join(os.path.dirname(
        __file__), "src/GreenPonik_OneWire_DS18B20", "version.py")
    version = {}
    with open(version_file) as fd:
        exec(fd.read(), version)
    return version["__version__"]


setup(
    name="greenponik-tsl2561",
    version=load_version(),
    author="GreenPonik SAS",
    author_email="contact@greenponik.com",
    description="Read TSL2561 through Python3 on raspberry pi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GreenPonik/GreenPonik_TSL2561",
    license="MIT",
    install_requires=["adafruit-circuitpython-tsl2561"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={'': 'src'},  # Optional
    packages=find_packages(where='src'),  # Required
    python_requires='>=3.6',
    project_urls={  # Optional
        'Source': 'https://github.com/GreenPonik/GreenPonik_TSL2561/',
        'Bug Reports': 'https://github.com/GreenPonik/GreenPonik_TSL2561/issues',
    },
    keywords="GreenPonik hydroponics tsl2561 light reader python hardware diy iot raspberry pi",
    py_modules=["GreenPonik_TSL2561"],
)