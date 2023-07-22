from dataclasses import dataclass, field


@dataclass
class Plan:
    description: str = ""  # Description of the plan
    elements: list = field(default_factory=list)  # List of plan elements

    def preview(self):
        action_list: list = []
        for element in self.elements:
            action = element.get_action()
            if action is not None:
                action_list.append(action)
        return action_list

    def run(self, action_list=None):
        """Run the plan"""
        if action_list is None:
            action_list = self.preview()

        if not action_list:
            return []

        for action in action_list:
            action()

        return action_list
