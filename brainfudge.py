import re
import logging
from typing import Tuple

logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.ERROR)

class Interpreter:
    """A Brainf*ck interpreter."""

    def __init__(self, array_len: int = 30000) -> None:
        """Initialize variables."""
        self.array_len = array_len
        self.array = [0] * array_len
        self.pointer = 0

    def loop(self, code: str) -> Tuple:
        """Loop some code."""
        brack_count = 0
        loop_starts = [m.start() for m in re.finditer("\[", code)]
        loop_ends = [m.start() for m in re.finditer("]", code)]
        # Add one for code slicing.
        loop_start = loop_starts[0] + 1
        for i, cmd in enumerate(code):
            # Algorithm for checking bracket pairs.
            if cmd == "[":
                brack_count += 1
            elif cmd == "]":
                brack_count -= 1
                if brack_count == 0:
                    loop_end = i
                    break
        if (
            # Check for inequalities.
            len(loop_starts) != len(loop_ends)
            or loop_starts[-1] > loop_ends[-1]
            or loop_ends[0] < loop_starts[0]
            or brack_count != 0
        ):
            # Abort!
            logger.exception("unclosed loop")
            exit()
        while self.array[self.pointer] != 0:
            # Loop code within loop while cell is not 0
            self.run(code[loop_start:loop_end])
        # Return values for code slicing
        return loop_start, loop_end

    def run(self, code: str) -> None:
        """Interpret some code."""
        i = 0
        while i < len(code):
            # Parse
            if code[i] == ">":
                self.pointer = (self.pointer + 1) % self.array_len
            elif code[i] == "<":
                self.pointer = (self.pointer - 1) % self.array_len
            elif code[i] == "+":
                self.array[self.pointer] = (self.array[self.pointer] + 1) % 256
            elif code[i] == "-":
                self.array[self.pointer] = (self.array[self.pointer] - 1) % 256
            elif code[i] == ".":
                print(chr(self.array[self.pointer]), end="")
            elif code[i] == ",":
                self.array[self.pointer] = int(input(f"{self.pointer}>")) % 256
            elif code[i] == "[":
                looped = self.loop(code)
                loop_start = looped[0]
                loop_end = looped[1]
                # Remove loop from code
                code = code[: loop_start - 1] + code[loop_end + 1 :]
                # Go back a step so no code is missed
                i -= 1
            i += 1

    def run_input(self) -> None:
        """Run code from user input."""
        fudge = input()
        self.run(fudge)

    def run_file(self, file_name: str) -> None:
        """Run a file."""
        with open(file_name, "r") as file:
            code = file.read()
        self.run(code)
