from dataclasses import dataclass

import lxcraft


@dataclass
class MyTestresourceWithAction(lxcraft.Resource):
    pending_action: bool = True

    def create(self):
        self.pending_action = False

    def destroy(self):
        pass

    def is_created(self):
        return not self.pending_action

    def is_consistent(self):
        return True


def test_resource():
    def change_callback():
        pass

    resource = MyTestresourceWithAction().on_change(change_callback)
    assert resource.source_repr()
    with lxcraft.Plan([resource]) as plan:
        plan.execute()
        plan.execute()
