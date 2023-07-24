from typing import Callable


class PlanElement:
    def on_change(self, action):
        self.action = action
        return self

    def get_actions(self) -> list[Callable]:
        """Return a list of actions to be executed"""
        return []

    @staticmethod
    def action_engine(action_dict: dict[Callable, Callable]) -> list[Callable]:
        action_list = []
        for key, value in action_dict.items():
            key_value = key()
            if key_value:
                action_list.append(value)
        return action_list

    # __iter__ and __next__ are required for the for loop
    def __iter__(self):
        return self

    def __next__(self):
        return StopIteration
