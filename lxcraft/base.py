class BaseAction:
    def on_change(self, action):
        self.action = action
        return self
