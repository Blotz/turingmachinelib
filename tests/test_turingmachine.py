from turingmachinelib.turingmachine import TuringMachine
from turingmachinelib.state import State
from turingmachinelib.state import StateAction
from turingmachinelib.structs import MoveAction

def test_print():
    # Simple TM for moving left and setting tape values to 1
    state = State("")
    tm = TuringMachine(state) 
    sa = StateAction(1, MoveAction.LEFT, state)
    state.set_action(0, sa)

    tm.old_print_turing_machine()