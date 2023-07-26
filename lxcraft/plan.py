import sys
from dataclasses import dataclass, field
from typing import Callable

from lxcraft.debug import debug

from .resource import Resource


@dataclass
class Plan:
    resources: Resource | list[Resource] = field(
        default_factory=list[Resource]
    )  # List of plan resources

    # Check if all the resources are based on Resource to avoid type errors
    def __post_init__(self):
        if not isinstance(self.resources, list):
            self.resources = [self.resources]
        assert self.resources, "Plan must have at least one resource"
        for resource in self.resources:
            assert isinstance(
                resource, Resource
            ), f"{resource} is not based on Resource"

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        for resource in self.resources:
            debug("destroy", "__exit__ Destroying", resource)
            resource.destroy()

    def try_and_point(self, action: Callable):
        debug("action", "Trying to execute", action)
        try:
            action()
        except Exception as e:
            print(
                "EXCEPTION related to ",
                action.__self__.source_repr(),
                file=sys.stderr,
            )
            raise e

    def execute(self):
        """Execute all the actions required to create the resources
        and bring them to a consistent state"""
        for resource in self.resources:
            if not resource.is_created():
                self.try_and_point(resource.create)
            if not resource.is_consistent():
                self.try_and_point(resource.destroy)
                self.try_and_point(resource.create)
