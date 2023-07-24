import sys
from dataclasses import dataclass, field
from typing import Callable

from .plan_element import PlanElement


@dataclass
class Plan:
    elements: PlanElement | list[PlanElement] = field(
        default_factory=list[PlanElement]
    )  # List of plan elements

    # Check if all the elements are based on PlanElement to avoid type errors
    def __post_init__(self):
        if not isinstance(self.elements, list):
            self.elements = [self.elements]
        assert self.elements, "Plan must have at least one element"
        for element in self.elements:
            assert isinstance(
                element, PlanElement
            ), f"{element} is not based on PlanElement"

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        for element in self.elements:
            element.destroy()

    def preview(self):
        total_action_list: list[Callable] = []

        for element in self.elements:
            action_list = element.get_actions()
            if not action_list:
                continue
            for action in action_list:
                total_action_list.append(action)
        return total_action_list

    def execute(self):
        """Execute all the actions required to materialize the elements"""
        action_list = self.preview()
        if not action_list:
            return

        for action in action_list:
            try:
                action()
            except Exception as e:
                print(
                    "EXCEPTION related to ",
                    action.__self__.source_repr(),
                    file=sys.stderr,
                )
                raise e

        # run the preview to make suse
        post_run_preview = self.preview()
        if post_run_preview:
            print("Pending actions after run:", file=sys.stderr)
            for action in post_run_preview:
                print(" - ", action, file=sys.stderr)
            raise Exception("Plan did not run successfully - check previous errors")

        return post_run_preview
