from enum import Enum
from dataclasses import dataclass

import ctypes
from typing import Union

from turingmachine.state import State

class MoveAction(Enum):
    NONE = 0
    LEFT = 1
    RIGHT = 2

@dataclass
class StateAction():
    write_value: Union[ctypes.c_byte, None]
    move_action: MoveAction
    state: State