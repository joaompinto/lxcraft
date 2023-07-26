from dataclasses import dataclass

import pytest

import lxcraft


class MyTestresource(lxcraft.Resource):
    def create(self):
        pass

    def destroy(self):
        pass

    def is_created(self):
        pass

    def is_consistent(self):
        pass


@dataclass
class MyTestresourceWithActions(lxcraft.Resource):
    raise_exeception: bool = False
    was_created: bool = False

    def create(self):
        if self.raise_exeception:
            raise Exception("TestresourceWithActionsException")
        self.was_created = True

    def destroy(self):
        pass

    def is_created(self):
        return self.was_created

    def is_consistent(self):
        return True


def test_plan():
    # with pytest.raises(Exception, match=r"is not based on Resource"):
    #     lxcraft.Plan("text")

    # Test the context manager
    with lxcraft.Plan([MyTestresource()]) as plan:
        plan.execute()
        plan.destroy()

    with lxcraft.Plan([MyTestresourceWithActions()]) as plan:
        plan.execute()
        plan.destroy()

    lxcraft.Plan([MyTestresourceWithActions()]).execute()

    with pytest.raises(Exception, match=r"TestresourceWithActionsException"):
        lxcraft.Plan([MyTestresourceWithActions(raise_exeception=True)]).execute()
