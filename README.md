# Brainfudge #
Run Brainf\*ck code with python!

## Classes ##
* `_ArgumentParser(argparse.ArgumentParser)`: sole reason for existence if for custom error message
    * `error(self, message)`: print help and sys.stderr
* `Interpreter(array_len)`: encapsulate all functions into class
    * `__init__(self, array_len: int=30000) -> None`: initialize variables
        * `array_len`: length of memory tape
    * `loop(self, code: str) -> Tuple`: loop some code
        * `code`: code to loop; will auto-cut down into the square brackets
    * `run(self, code: str) -> None`: run some code
        * `code`: code to run
    * `run_input(self) -> None`: run code from user input
    * `run_file(self, file_name: str) -> None`: run a file
        * `file_name`: file to run
    * `reset(self) -> None`: reset pointer and storage tape

## Functions ##
* `_parse_args()`: nicer than declaring flags at start of code

## Examples for Python terminal ##
For `run`:
```
>>> import brainfudge
>>> I = brainfudge.Interpreter()
>>> code = "[->+<]"
>>> I.run(code)
```
For `run_input`:
```
>>> import brainfudge
>>> I = brainfudge.Interpreter()
>>> I.run_input()
Code: [->+<]
```
For `run_file`:
```
>>> import brainfudge
>>> I = brainfudge.Interpreter()
>>> file_name = "example.bf"
>>> I.run_file(file_name)
Hello, World!
```
For `reset`:
```
>>> import brainfudge
>>> I = brainfudge.Interpreter()
>>> file_name = "exmple.bf"
>>> I.run_file(file_name)
Hello, World!>>> I.reset()
>>> I.run("[->+<]")
```
## For regular terminal ##
For `-r` (`--run`):
```
username@machine:~/brainfudge$ python3 brainfudge.py -r "[->+<]"
```
For `-i` (`--input`):
```
username@machine:~/brainfudge$ python3 brainfudge.py -i
Code: [->+<]
```
For `-f` (`--file`):
```
username@machine:~/brainfudge$ python3 brainfudge.py -f "example.bf"
Hello, World!
```
