# Python - Hello, World
  - Why Python programming is awesome
  - Who created Python
  - Who is Guido van Rossum
  - Where does the name ‘Python’ come from
  - What is the Zen of Python
  - How to use the Python interpreter
  - How to print text and variables using print
  - How to use strings
  - What are `indexing` and `slicing` in Python
  - What is the official Python coding style and how to check your code
  with `pycodestyle`

# Files
## [0-run](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x00-python-hello_world/0-run)
   A Shell script that runs a Python script

## [1-run_inline](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x00-python-hello_world/1-run_inline)
   A Shell script that runs Python code.
   The Python code will be saved in the environment variable `$PYCODE`

## [2-print.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x00-python-hello_world/2-print.py)
   A Python script that prints exactly `\"Programming is like building a\
   multilingual puzzle`, followed by a new line.

## [3-print_number.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x00-python-hello_world/3-print_number.py)
   A Python script that prints variable `number`, followed `Battery Street`,
   followed by a new line.

## [4-print_float.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x00-python-hello_world/4-print_float.py)
   A Python script that prints the float variable `number`
   with a precision of 2 digits

## [5-print_string.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x00-python-hello_world/5-print_string.py)
   A Python script that prints the string  variable `str` 3 times,
   followed by its first 9 characters

## [6-concat.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x00-python-hello_world/6-concat.py)
   A Python script that prints `Welcome to Holberton School!`
   using string variables `str1` and `str2`
   - Loops or conditional statements are not allowed

## [7-edges.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x00-python-hello_world/7-edges.py)
   Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/7-edges.py)
   - Loops or conditionals are not allowed
   - `word_first_3` should contain the first 3 letters of the variable `word`
   - `word_last_2` should contain the last 2 letters of the variable `word`
   - `middle_word` should contain the value of the variable `word`
   without the first and last letters

## [8-concat_edges.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x00-python-hello_world/8-concat_edges.py)
   Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/8-concat_edges.py)\
   to print `object-oriented programming with Python`, followed by a new line
   - Loops or conditional statements not allowed
   - Not allowed to create new variables
   - Not allowed to use string literals

## [9-easter_egg.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x00-python-hello_world/9-easter_egg.py)
   A python script that prints "The Zen of Python", by TimPeters,
   followed by a new line

## [10-check_cycle.c](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x00-python-hello_world/10-check_cycle.c)
   A function in `C` that checks if a singly linked list has a cycle in it
   - Prototype: `int check_cycle(listint_t *list);`
   - Returns `0` if ther is no cycle, `1` if there is a cycle

## [100-write.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x00-python-hello_world/100-write.py)
   A Python script that prints exactly `and that piece of art is useful -\
   Dora Korpar, 2015-10-19` using the `write` function form the `sys` module
   - The script should print to `stderr`
   - The script should exit with status code `1`

## [101-compile](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x00-python-hello_world/101-compile)
   A script that compiles a Python script file.
   The Python file name  will be store in the environment variable `$PYFILE`

## [102-magic_calculation.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x00-python-hello_world/102-magic_calculation.py)
   A Python function `def magic_calculation(a, b)`: that does exactly the same\
   as the following Python bytecode:
   ````
   3  0 LOAD_CONST	1 (98)
      3 LOAD_FAST	0 (a)
      6 LOAD_FAST	1 (b)
      9 BINARY_POWER
      10 BINARY_ADD
      11 RETURN_VALUE
   ```