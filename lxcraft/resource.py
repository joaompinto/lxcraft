import inspect
from typing import Callable


class Resource:
    def __post_init__(self):
        callerframerecord = inspect.stack()[2]
        self.location = callerframerecord.filename
        self.lineno = callerframerecord.lineno

    def source_repr(self):
        return f"{self.location}:{self.lineno} # -> {self}"

    def on_change(self, callback: Callable):
        """Execute callback if the resource is changed"""
        self.on_change_callback = callback
        return self
