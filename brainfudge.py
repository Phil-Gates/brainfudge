import re
import logging
import sys
import argparse
from typing import Tuple

logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.ERROR)


class _ArgumentParser(argparse.ArgumentParser):
    """Custom error message."""

    def error(self, message):
        """Custom error message."""
        self.print_help()
        sys.stderr.write(f"\n{message}\n")


Parser = _ArgumentParser(description="Easy Brainf*ck interpretation")


def _parse_args():
    """Nicer than doing it at start of code."""
    Parser.add_argument("-r", "--run", type=str, help="code to run")
    Parser.add_argument("-i", "--input", action="store_true", help="from input")
    Parser.add_argument("-f", "--file", type=str, help="filename to run")
    return Parser.parse_args()


class Interpreter:
    """Encapsulate all functions into one class."""

    def __init__(self, array_len: int = 30000) -> None:
        """
        Initialize variables.
        array_len: determine storage tape length
        """
        self.array_len = array_len
        self.array = [0] * array_len
        self.pointer = 0

    def run(self, code: str) -> None:
        """Run some code."""
        i = 0
        brack_count = 0
        brack_list = []
        ghost_mode = False
        first_time = True
        while i < len(code):
            # Parse
            if not ghost_mode:
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
            if code[i] == "[":
                if (self.array[self.pointer] != 0) and (not ghost_mode):
                    brack_list.append(i)
                    brack_count += 1
                elif ghost_mode:
                    brack_count += 1
                else:
                    brack_count += 1
                    ghost_mode = True
                    ghost_count = brack_count
            elif code[i] == "]":
                try:
                    if self.array[self.pointer] != 0:
                        if first_time:
                            brack_count -= 1
                            first_time = False
                        i = brack_list[brack_count]  # incremented later
                        if brack_count < 0:
                            raise IndexError()
                    elif ghost_mode:
                        if brack_count == ghost_count:
                            ghost_mode = False
                        brack_count -= 1
                    elif self.array[self.pointer] == 0:
                        first_time = True
                        brack_list.pop()
                except IndexError:
                    logger.exception(
                        f"mismatched brackets at char {i}",
                        exc_info=False,
                    )
                    return
            i += 1

    def run_input(self) -> None:
        """Run code from user input."""
        try:
            code = input("Code: ")
        except (KeyboardInterrupt, EOFError):
            return
        self.run(code)

    def run_file(self, file_name: str) -> None:
        """Run a file."""
        try:
            with open(file_name, "r") as file:
                code = file.read()
        except FileNotFoundError:
            logger.exception(f"file '{file_name}' not found", exc_info=False)
            return
        self.run(code)

    def reset(self) -> None:
        """Reset storage tape and pointer."""
        self.pointer = 0
        self.array = [0] * self.array_len


if __name__ == "__main__":
    args = _parse_args()
    if len(sys.argv) > 1:
        I = Interpreter()
        if args.run:
            I.run(args.run)
        elif args.input:
            I.run_input()
        elif args.file:
            I.run_file(args.file)
    else:
        Parser.error("no flags provided")
