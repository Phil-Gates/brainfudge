# Brainfudge
Run brainf\*ck code with python!

## Classes ##
* `Interpreter(array_len)`: interpret some code.
    * `__init__(self, array_len: int=30000) -> None`: initialize variables
        * `array_len`: length of memory tape
    * `loop(self, code: str) -> Tuple`: loop some code
    * `run(self, code: str) -> None`: run some code
    * `run_input(self) -> None`: run code from user input
    * `run_file(self, file_name: str) -> None`: run a file


## Examples ##
For `run`:
```
>>> import brainfudge
>>> I = brainfudge.Interpreter()
>>> code = "[->+<]"
>>> I.run(code))
```
For `run_input`:
```
>>> import brainfudge
>>> I = brainfudge.Interpreter()
>>> I.run_input()
[->+<]
```
For `run_file`:
```
>>> import brainfudge
>>> I = brainfudge.Interpreter()
>>> I.run_file("example.bf")
```
