# Pythonic Configuration Manager for Linux Systems

[![PyPi](https://img.shields.io/pypi/v/lxcraft.svg?style=flat-square)](https://pypi.python.org/pypi/lxcraft)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/ambv/black)


```python
from lxcraft import Plan
from lxcraft.debian import APTPackages

Plan("ensure nginx is installed", [
    APTPackages(["nginx"], must_be_installed=True)
]).run()
```
