import curses
from collections.abc import Callable
from typing import Union
from dataclasses import dataclass

from turingmachinelib.pointer import Pointer


@dataclass
class Window:
    window_coord: list[float]
    window_name: str
    #  (curses.window) -> None
    window_func: Callable[[curses.window], None]

    window: curses.window = None


class TuringMachine():
    def __init__(self, state) -> None:
        self.pointer = Pointer(state)

    def run(self) -> str:
        return curses.wrapper(self.run_curses)

    def old_run(self) -> str:
        try:
            while True:
                self.old_print_turing_machine()
                input()
                self.pointer.compute()

        except Exception as e:
            return self.pointer.output

    def run_curses(self, stdscr: curses.window):
        scene = self.init_windows(stdscr)
        stdscr.refresh()

        while True:
            # Stop outputting if terminal is too small
            height, width = stdscr.getmaxyx()
            if height < 20 or width < 30:
                stdscr.clear()
                self.print_too_small(stdscr)
                stdscr.refresh()
                key = stdscr.getch() # Wait for next key because its pointless to
                # continue if the terminal is too small
                continue

            try:
                self.print_turing_machine(scene)
            except curses.error:
                stdscr.clear()
                self.resize_windows(stdscr, scene)
                self.print_too_small(stdscr)
                stdscr.refresh()
                key = stdscr.getch()
                continue

            key = stdscr.getch()

            if key == curses.KEY_RESIZE:
                self.resize_windows(stdscr, scene)
                continue
            if key == ord('q'):
                break

            
            ############################################
            try:
                self.pointer.compute()
            except Exception as e:
                return self.pointer.output
            ############################################


    def print_turing_machine(self, scene: dict[str, Window]):
        for w in scene.values():
            w.window.clear()
            w.window.border()
            w.window.addstr(0, 1, w.window_name, curses.A_BOLD)
            w.window_func(w.window)
            w.window.refresh()

    def resize_windows(self, stdscr: curses.window, scene: dict[str, Window]):
        height, width = stdscr.getmaxyx()

        for w in scene.values():
            w.window.resize(
                int(height * w.window_coord[0]),
                int(width * w.window_coord[1]))
            w.window.mvwin(
                int(height * w.window_coord[2]),
                int(width * w.window_coord[3]))

        stdscr.clear()
        stdscr.refresh()
        
    def init_windows(self, stdscr: curses.window) -> dict[str, Window]:
        height, width = stdscr.getmaxyx()

        scene = dict()
        # y length, x length, y start, x start

        scene["next_states"] = Window(
            window_coord=[0.7, 0.3, 0.3, 0.7], 
            window_name="Next State", 
            window_func=self.print_next_states)
        scene["next_states"].window = curses.newwin(
            int(height * scene["next_states"].window_coord[0]),
            int(width * scene["next_states"].window_coord[1]),
            int(height * scene["next_states"].window_coord[2]),
            int(width * scene["next_states"].window_coord[3]))

        scene["tape"] = Window(
            window_coord=[0.3, 0.7, 0.0, 0.0], 
            window_name="Tape", 
            window_func=self.print_tape)
        scene["tape"].window = curses.newwin(
            int(height * scene["tape"].window_coord[0]),
            int(width * scene["tape"].window_coord[1]),
            int(height * scene["tape"].window_coord[2]),
            int(width * scene["tape"].window_coord[3]))
        
        scene["current_state"] = Window(
            window_coord=[0.3, 0.3, 0.0, 0.7], 
            window_name="Current State", 
            window_func=self.print_current_state)
        scene["current_state"].window = curses.newwin(
            int(height * scene["current_state"].window_coord[0]),
            int(width * scene["current_state"].window_coord[1]),
            int(height * scene["current_state"].window_coord[2]),
            int(width * scene["current_state"].window_coord[3]))
        
        scene["output"] = Window(
            window_coord=[0.7, 0.7, 0.3, 0.0], 
            window_name="Output", 
            window_func=self.print_output)
        scene["output"].window = curses.newwin(
            int(height * scene["output"].window_coord[0]),
            int(width * scene["output"].window_coord[1]),
            int(height * scene["output"].window_coord[2]),
            int(width * scene["output"].window_coord[3]))

        return scene


    def print_next_states(self, stdscr: curses.window):
        current_state = self.pointer.get_state()
        next_states = current_state.get_next_states()

        for i, (value, state) in enumerate(next_states):
            stdscr.addstr(i + 1, 1, f"{value} -> {state.get_ident()}")
    
    def print_output(self, stdscr: curses.window):
        output = self.pointer.get_output()
        stdscr.addstr(1, 1, output)
    
    def print_current_state(self, stdscr: curses.window):
        current_state = self.pointer.get_state()
        stdscr.addstr(1, 1, current_state.get_ident())
    
    def print_tape(self, stdscr: curses.window):
        _, width = stdscr.getmaxyx()
        width -= 2 # Remove border
        
        tape = self.pointer.get_tape()
        index = self.pointer.get_index()

        characters_per_cell = 4
        number_of_cells = width // characters_per_cell
        start_index = index - number_of_cells // 2

        for i in range(number_of_cells):
            if i > 0:
                stdscr.addstr(2, i*characters_per_cell, "|")  # Divider

            value = str(tape[start_index + i]).rjust(3)
            stdscr.addstr(2, 1 + i*characters_per_cell, value, curses.A_BOLD)  # Value

        stdscr.addstr(1, 1, "-"*width)  # Top bar
        stdscr.addstr(3, 1, "-"*width)  # Bottom bar
        stdscr.addstr(4, (number_of_cells // 2) * characters_per_cell + 3, "^")  # Pointer

    def print_too_small(self, stdscr: curses.window):
        height, width = stdscr.getmaxyx()
        message = "Terminal too small"
        try:
            stdscr.addstr(height//2, (width-len(message))//2, message)
        except curses.error:
            pass

    def old_print_turing_machine(self) -> None:
        """
        --- --- --- --- --- --- ---
           |123|123|123|123|123|
         --- --- --- --- --- --- --- 
                      ^ 
        """
        tape = self.pointer.get_tape()
        index = self.pointer.get_index()
        state = self.pointer.get_state()
        tm_output = self.pointer.get_output()

        padding = 2
        max_size = len(tape)
        
        left_index = index - padding
        right_index = index + padding
        left_buffer = 0
        right_buffer = 0

        if left_index < 0:
            left_buffer = - left_index
            left_index = 0
        if right_index > max_size:
            right_buffer = (right_index - max_size)
            right_index = max_size

        preview_tape = [0]*left_buffer + tape[left_index:right_index + 1] + [0]*right_buffer

        output = ""
        nl = "\n"
        bar = " ---" * 7
        box = "|%s"
        wspace = "    "
        arrow_up = "^"

        output += bar + nl + wspace
        for value in preview_tape:
            output += box % str(value).rjust(3)
        output += "|" + wspace + nl + bar + nl
        output += " " * 14 + arrow_up + nl

        output += "State: \"" + state.get_ident() + "\"" + nl
        output += "Output: \"" + tm_output + "\"" + nl

        print(output)