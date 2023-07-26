# Resource

An LXCraft any resource represents an artifact, capability or feature that can be installed on a target system.

A resource is a Python object based on the `lxcraft.Resource` class which must implement all of the following methods:


| Method          | Purpose   | Returns    |
|-----------------|-----------|------------|
| `__init__`      | The constructor of the resource with the required/optional arguments. | |
| `create`        | Creat the resource in the target system. | |
| `destroy`       | Destroy the resource in the target system. | |
| `is_created`    | Return `True` if the resource is present in the target system. | `bool` |
| `is_consistent` | Return `True` if the resource is consitent to the expected state. | `bool` |
