# Brainfudge
Run brainf\*ck code with python!

## Classes ##
>`Interpreter(array_len)`
>> `__init__`: initalize variables
>>>`array_len`: length of memory tape for interpreter
>> `run`: run code directly
>> `run_input`: ask for input then execute
>> `run_file`: run a file

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
