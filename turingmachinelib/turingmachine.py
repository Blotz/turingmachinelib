from turingmachinelib.pointer import Pointer

class TuringMachine():
    def __init__(self, state) -> None:
        self.pointer = Pointer(state)

    def run(self) -> str:
        try:
            while True:
                self.pointer.print_tm()
                input()
                self.pointer.compute()

        except Exception as e:
            return self.pointer.output