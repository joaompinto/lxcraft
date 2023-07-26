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


def test_plan_resource():
    resource = MyTestresourceWithAction()
    with lxcraft.Plan(resource) as plan:
        assert resource.source_repr()

        plan.execute()
        plan.execute()
