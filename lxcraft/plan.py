import sys
from dataclasses import dataclass, field
from typing import Callable

from .plan_element import PlanElement


@dataclass
class Plan:
    elements: PlanElement | list[PlanElement] = field(
        default_factory=list[PlanElement]
    )  # List of plan elements

    def __post_init__(self):
        if isinstance(self.elements, PlanElement):
            self.elements = [self.elements]
        for element in self.elements:
            if not isinstance(element, PlanElement):
                raise Exception(f"{element} is not based on PlanElement")

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
                print(action, file=sys.stderr)
                raise e

        # run the preview to make suse
        post_run_preview = self.preview()
        if post_run_preview:
            print("Pending actions after run:", file=sys.stderr)
            for action in post_run_preview:
                print(" - ", action, file=sys.stderr)
            raise Exception("Plan did not run successfully - check previous errors")

        return post_run_preview
