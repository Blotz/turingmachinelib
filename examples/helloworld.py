from turingmachinelib.turingmachine import TuringMachine
from turingmachinelib.state import State
from turingmachinelib.state import StateAction
from turingmachinelib.structs import MoveAction

init_state = State("INIT")
print_hello1 = State("print_hello1")
print_hello2 = State("print_hello2")
print_hello3 = State("print_hello3")
print_hello4 = State("print_hello4")
print_hello5 = State("print_hello5")
print_hello6 = State("print_hello6")
print_hello7 = State("print_hello7")
print_hello8 = State("print_hello8")
print_hello9 = State("print_hello9")
print_hello10 = State("print_hello10")
halt = State("HALT")

init_state.set_action(None, StateAction(104, MoveAction.PRINT, print_hello1))
print_hello1.set_action(None, StateAction(101, MoveAction.PRINT, print_hello2))
print_hello2.set_action(None, StateAction(108, MoveAction.PRINT, print_hello3))
print_hello3.set_action(None, StateAction(108, MoveAction.PRINT, print_hello4))
print_hello4.set_action(None, StateAction(111, MoveAction.PRINT, print_hello5))
print_hello5.set_action(None, StateAction(32, MoveAction.PRINT, print_hello6))
print_hello6.set_action(None, StateAction(119, MoveAction.PRINT, print_hello7))
print_hello7.set_action(None, StateAction(111, MoveAction.PRINT, print_hello8))
print_hello8.set_action(None, StateAction(114, MoveAction.PRINT, print_hello9))
print_hello9.set_action(None, StateAction(108, MoveAction.PRINT, print_hello10))
print_hello10.set_action(None, StateAction(100, MoveAction.PRINT, halt))

tm = TuringMachine(init_state)
tm.run()
# tm.old_run()
