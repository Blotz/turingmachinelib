
from ctypes import c_byte
from typing import Union


from turingmachine.structs import MoveAction
from turingmachine.state import State, StateAction

class Pointer:
    # Max size of tape is limited the size of memory.
    # also the array index has a soft limit at 4300 digits (str-to-int-conversion)
    index: int = 50
    tape: list[c_byte] = [0]*100
    alphabet: set[c_byte] = set(range(0,256))
    state: State

    INCREASE_AMOUNT: int = 50

    def __init__(self, state: State) -> None:
        self.state = state  # Set the Inital State

    def compute(self) -> None:
        """
        Compute the current state
        """
        action: StateAction = self.state.process(self.tape[self.index])

        # write
        self.write(action.write_value)

        # move
        self.move(action.move_action)

        # update state
        self.state = action.state

    def move(self, move_action: MoveAction) -> None:
        """
        Move the pointer in the direction of move action
        """
        if move_action == MoveAction.LEFT:
            # Move left
            self.move_left()
        elif move_action == MoveAction.RIGHT:
            # Move right
            self.move_right()
        elif move_action == MoveAction.NONE:
            # Dont move
            pass
        else:
            raise Exception("Unexpected error has occured. ")

    def move_left(self) -> None:
        """
        Move the pointer to the left. Expand memory if we reach the end of the array
        """
        self.index -= 1

        # Not at end of tape
        if self.index >= 0:
            return
        
        self.index += self.INCREASE_AMOUNT
        self.tape = [0]*self.INCREASE_AMOUNT + self.tape

    def move_right(self) -> None:
        """
        Move pointer to the right. Expand memory if we reach the end of the tape.
        """
        self.index += 1

        # Not at end of tape
        if self.index < len(self.tape):
            return
        
        self.tape = self.tape + [0]*self.INCREASE_AMOUNT

    def write(self, value: Union[c_byte, None]) -> None:
        # Do nothing if the value is set to none
        if value is None:
            return
        
        # Write the value to tape
        self.tape[self.index] = value

    def __str__(self) -> str:
        return chr(self.tape[self.index])