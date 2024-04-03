import pytest

from turingmachinelib.state import State, StateAction
from turingmachinelib.structs import MoveAction


def test_process():
    state = State("")
    sa = StateAction(1, MoveAction.NONE, state)
    state.set_action(0, sa)

    assert state.actions[0] == sa
    
    response = state.process(0)
    assert response == sa

    with pytest.raises(Exception) as e:
        state.process(1)

    


