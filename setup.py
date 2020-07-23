from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name="greenponik-tsl2561",
    version="0.0.1",
    author="GreenPonik SAS",
    author_email="mickael.lehoux@greenponik.com",
    description="Read TSL2561 through Python3 on raspberry pi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GreenPonik/GreenPonik_TSL2561",
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
    py_modules=["GreenPonik_TSL2561"],
)
