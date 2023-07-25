# LXCraft

A Declarative Configuration Build Tool for Linux Systems

[![PyPi](https://img.shields.io/pypi/v/lxcraft.svg?style=flat-square)](https://pypi.python.org/pypi/lxcraft)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/ambv/black)

A simple declarative configuration build tool for Linux systems.

- 🐍 Pure Python declarative code
    - No need to learn a new DSL/programming language
    - Leverage IDE features like inline documentation, code completion, linting, etc.
- 📏 Ephemeral target system
    - No need to worry about maintaing the system state
- Simpler than Chef, Puppet, Ansible, Terraform, SaltStack, etc. due to the above


## How to use
```python
from lxcraft import Plan
from lxcraft.debian import AptPackages

Plan([
    AptPackages(["nginx"])
]).execute()
```

## How to develop

In order to develop you must use Linux or WSL with docker.

```sh
develop/docker-bash     # Enter the development docker instance
just                    # Run the tests
```
