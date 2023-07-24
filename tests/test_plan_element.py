from dataclasses import dataclass

import pytest

import lxcraft


@dataclass
class MyTestElement(lxcraft.PlanElement):
    def get_actions(self):
        pass

    def destroy(self):
        pass


@dataclass
class MyTestElementWithAction(lxcraft.PlanElement):
    pending_action: bool = True

    def get_actions(self):
        return self.action_engine({self.is_pending_action: self.do_something})

    def is_pending_action(self):
        return self.pending_action

    def do_something(self):
        self.pending_action = False

    def destroy(self):
        pass


def test_plan_element():
    # Base PlanElement and context manager
    with lxcraft.Plan(MyTestElement()) as plan:
        plan.execute()

    element = MyTestElementWithAction()
    with lxcraft.Plan(element) as plan:
        assert element.source_repr()

        plan.execute()
        plan.execute()

    with pytest.raises(Exception, match=r"already has a plan"):
        lxcraft.Plan(element)
