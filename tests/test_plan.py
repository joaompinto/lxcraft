from dataclasses import dataclass

import pytest

import lxcraft


class MyTestElement(lxcraft.PlanElement):
    def get_actions(self):
        pass

    def destroy(self):
        pass


@dataclass
class MyTestElementWithActions(lxcraft.PlanElement):
    raise_exeception: bool = False
    completed: bool = False
    always_run: bool = False

    def get_actions(self):
        if not self.completed or self.always_run:
            return [self.hello]

    def hello(self):
        if self.raise_exeception:
            raise Exception("TestElementWithActionsException")
        self.completed = True


def test_plan():
    with pytest.raises(Exception, match=r"is not based on PlanElement"):
        lxcraft.Plan("text")

    # Test the context manager
    with lxcraft.Plan(MyTestElement()) as plan:
        plan.execute()

    lxcraft.Plan(MyTestElementWithActions()).execute()

    with pytest.raises(Exception, match=r"TestElementWithActionsException"):
        lxcraft.Plan(MyTestElementWithActions(raise_exeception=True)).execute()
    with pytest.raises(Exception, match=r"Plan did not run successfully"):
        lxcraft.Plan(MyTestElementWithActions(always_run=True)).execute()
