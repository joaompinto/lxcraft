import inspect
from typing import Callable


class PlanElement:
    def __post_init__(self):
        callerframerecord = inspect.stack()[2]  # 0
        self.location = callerframerecord.filename
        self.lineno = callerframerecord.lineno

    def source_repr(self):
        return f"{self.location}:{self.lineno} # -> {self}"

    @staticmethod
    def action_engine(action_dict: dict[Callable, Callable]) -> list[Callable]:
        action_list = []
        for key, value in action_dict.items():
            key_value = key()
            if key_value:
                action_list.append(value)
        return action_list

    def set_plan(self, plan):
        if "plan" in self.__dict__:
            raise Exception("PlanElement already has a plan")
        self.plan = plan
