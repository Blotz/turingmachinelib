from ctypes import c_byte

from turingmachine.structs import StateAction

class State:
    ident: str 
    actions: dict[c_byte, StateAction] = dict()

    def __init__(self, identity) -> None:
        self.ient = identity
    
    def get_ident(self) -> str:
        return self.ident
    
    def set_action(self, value: c_byte, action: StateAction) -> None:
        self.actions[value] = action 
    
    def process(self, value: c_byte):
        if value in self.actions:
            return self.actions[value] 
        
        raise Exception("State does not have action assigned to value %d", value)
