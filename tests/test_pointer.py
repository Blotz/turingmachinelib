from turingmachine.state import State, StateAction
from turingmachine.pointer import Pointer
from turingmachine.structs import MoveAction

def test_move_left():
    state = State("")
    pointer = Pointer(state) 

    staring_point = pointer.index
    pointer.move_left()
    next_point = pointer.index

    # Check to see if pointer updates correctly
    assert (staring_point - 1) == next_point

    for _ in range(pointer.index):
        pointer.move_left()
    
    # Move to edge of tape
    assert pointer.index == 0


    staring_point = pointer.index
    pointer.move_left()
    next_point = pointer.index

    # Does the pointer move right by the amount expected?
    assert next_point == (staring_point - 1) + pointer.INCREASE_AMOUNT

def test_move_right():
    state = State("")
    pointer = Pointer(state) 

    staring_point = pointer.index
    pointer.move_right()
    next_point = pointer.index

    # Check to see if pointer updates correctly
    assert (staring_point + 1) == next_point

    for _ in range(len(pointer.tape) - pointer.index - 1):
        pointer.move_right()
    
    # Move to edge of tape
    assert pointer.index == len(pointer.tape) - 1


    staring_point = pointer.index
    pointer.move_right()
    next_point = pointer.index

    # Does the pointer move right by the amount expected?
    assert next_point == (staring_point + 1)

def test_move():
    state = State("")
    pointer = Pointer(state)

    staring_point = pointer.index
    pointer.move(MoveAction.LEFT)
    next_point = pointer.index

    # Moves left
    assert staring_point - 1 == next_point

    staring_point = pointer.index
    pointer.move(MoveAction.RIGHT)
    next_point = pointer.index

    assert staring_point + 1 == next_point

    staring_point = pointer.index
    pointer.move(MoveAction.NONE)
    next_point = pointer.index

    assert staring_point == next_point

def test_write():
    state = State("")
    pointer = Pointer(state) 

    # initalised to zero
    assert pointer.tape[pointer.index] == 0

    pointer.write(None)

    # Check to see it hasnt changed
    assert pointer.tape[pointer.index] == 0

    pointer.write(1)

    assert pointer.tape[pointer.index] == 1

def test_compute():
    state = State("")
    pointer = Pointer(state) 

    sa = StateAction(1, MoveAction.LEFT, state)
    state.set_action(0, sa)


    start_index = pointer.index

    assert pointer.tape[pointer.index] == 0

    pointer.compute()
    next_index = pointer.index

    assert start_index - 1 == next_index
    assert pointer.tape[start_index] == 1

    pointer.compute()

    assert pointer.tape[next_index] == 1

