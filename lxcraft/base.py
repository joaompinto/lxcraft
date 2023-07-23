class BaseAction:
    def on_change(self, action):
        self.action = action
        return self


def action_engine(action_dict: dict):
    action_list = []
    for key, value in action_dict.items():
        key_value = key()
        if key_value:
            action_list.append(value)
    return action_list
