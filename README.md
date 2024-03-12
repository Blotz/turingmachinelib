# Project structure

```
low level
Set -> Alphabet
double ended array -> Tape
list -> finite table of sets ?? maybe.

class state:
    str name
    dict value:(WriteAction, MoveAction, State)
    
    def compute(pointer):
        read value.
        -> write
        -> move pointer
        -> return new state
    
    def move(MoveAction):
        if ... 

    def write(WriteAction):
        if None: return
        tape[index] = value


    def move_left:
    def move_right:

datastruct StateAction:
    WriteAction
    MoveAction
    State

enum WriteAction:
    value || none

enum MoveAction:
    left || right || none

class pointer:
    int index 
    array tape
    set alpha
    State s

    loop
        s = compute(self)


init each state
confirm each state has unique id

for state in table
    read the action defined
    look up the return state by its ID
    set value in dict to be (date struct)

init pointer with inital state

for s in pointer.process():
    print(s)
```