import pytest

from turingmachinelib.state import State, StateAction
from turingmachinelib.structs import MoveAction


def test_process():
    state = State("")
    sa = StateAction(1, MoveAction.NONE, state)
    sa = StateAction(None, MoveAction.NONE, state)
    state.set_action(0, sa)
    state.set_action(1, sa)

    assert state.actions[0] == sa
    
    response = state.process(0)
    assert response == sa

    response = state.process(1)
    assert sa == response

    with pytest.raises(Exception) as e:
        state.process(2)

