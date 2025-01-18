# Python - Exceptions
  - What’s the difference between errors and exceptions
  - What are exceptions and how to use them
  - When do we need to use exceptions
  - How to correctly handle an exception
  - What’s the purpose of catching exceptions
  - How to raise a builtin exception
  - When do we need to implement a clean-up action after an exception

## [0-safe_print_list.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x05-python-exceptions/0-safe_print_list.py)
   A function that prints the elements of a list
   - Prototype: `def safe_print_list(my_list=[], x=0):`
   - `my_list` can contain any data type
   - `x` represents the number of the elements to prints

## [1-safe_print_integer.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x05-python-exceptions/1-safe_print_integer.py)
   A function that prints an integer with `"{:d}".format()`
   - Prototype: `def safe_print_ineger(value):`
   - `value` can be any data type

## [2-safe_print_list_integers.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x05-python-exceptions/2-safe_print_list_integers.py)
   A function that prints the first `x` elements of a list and only integers
   - Prototype: `def safe_print_list_integers(my_list=[], x=0):`
   - `my_list` can contain any data type
   - `x` represents the number of elements to access in `my_list`

## [3-safe_print_division](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x05-python-exceptions/3-safe_print_division.py)
   A function that divides 2 integers and prints the result.
   - Prototype: `def safe_print_division(a, b):`
   - You can assume `a` and `b` are integers

## [4-list_division.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x05-python-exceptions/4-list_division.py)
   A function that divides two lists element by element
   - Prototype: `def list_division(my_list_1, my_list_2, list_length):`
   - `my_list_1` and `my_list_2` can contain any data type
   - Returns a new list (length = `list_length`) with all divisions
   - If 2 elements can't be divided, the division result should be equal to `0`
   - If an element is not an integer or a float: prints `wrong type`
   - If the division can't be done(`/0`): prints `division by 0`
   - If `my_list_1` or `my_list_2` is too short: prints `out of range`

## [5-raise_exception.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x05-python-exceptions/5-raise_exception.py)
   A function that raises and exception
   - Prototype: `def raise_exception():`

## [6-raise_exception_msg](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x05-python-exceptions/6-raise_exception_msg.py)
   A function that raises a name exception with a message
   - Prototype: `def raise_exception_msg(message=""):`

## [100-safe_print_integer_err.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x05-python-exceptions/100-safe_print_integer_err.py)
   A function that prints an integer
   - Prototype: `def safe_print_integer_err(value):`
   - `value` can be any data type
   - Returns `True` if `value` has been correctly printed
   - Otherwise returns `False` and prints to `stderr`: `Exception: <error>`

## [101-safe_function.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x05-python-exceptions/101-safe_function.py)
   A function that executes a function safely
   - Prototype: `def safe_function(fct, *args):`
   - You can assume `fct` will always be a pointer to a function
   - Returns the result of the function
   - Otherwise, returns `None` if something happens during the execution and prints: `Exception: <error>`

## [102-magic_calculation.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x05-python-exceptions/102-magic_calculation.py)
   A function that does exactly the same thing as the Python bytcode below
   - Prototype: `def magic_calculation(a, b):`
   ```
  3           0 LOAD_CONST               1 (0)
              3 STORE_FAST               2 (result)

  4           6 SETUP_LOOP              94 (to 103)
              9 LOAD_GLOBAL              0 (range)
             12 LOAD_CONST               2 (1)
             15 LOAD_CONST               3 (3)
             18 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             21 GET_ITER
        >>   22 FOR_ITER                77 (to 102)
             25 STORE_FAST               3 (i)

  5          28 SETUP_EXCEPT            49 (to 80)

  6          31 LOAD_FAST                3 (i)
             34 LOAD_FAST                0 (a)
             37 COMPARE_OP               4 (>)
             40 POP_JUMP_IF_FALSE       58

  7          43 LOAD_GLOBAL              1 (Exception)
             46 LOAD_CONST               4 ('Too far')
             49 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             52 RAISE_VARARGS            1
             55 JUMP_FORWARD            18 (to 76)

  9     >>   58 LOAD_FAST                2 (result)
             61 LOAD_FAST                0 (a)
             64 LOAD_FAST                1 (b)
             67 BINARY_POWER
             68 LOAD_FAST                3 (i)
             71 BINARY_TRUE_DIVIDE
             72 INPLACE_ADD
             73 STORE_FAST               2 (result)
        >>   76 POP_BLOCK
             77 JUMP_ABSOLUTE           22

 10     >>   80 POP_TOP
             81 POP_TOP
             82 POP_TOP

 11          83 LOAD_FAST                1 (b)
             86 LOAD_FAST                0 (a)
             89 BINARY_ADD
             90 STORE_FAST               2 (result)

 12          93 BREAK_LOOP
             94 POP_EXCEPT
             95 JUMP_ABSOLUTE           22
             98 END_FINALLY
             99 JUMP_ABSOLUTE           22
        >>  102 POP_BLOCK

 13     >>  103 LOAD_FAST                2 (result)
            106 RETURN_VALUE
   ```

## [103-python.c](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x05-python-exceptions/103-python.c)
   Three C funtions that print some basic infor about Python lists, Python bytes and Python float objects
   - Python lists:
     - Prototype: `void print_python_list(PyObject *p);`
     - If `p` is not a valid `PyListObject`: prints `[ERROR] Invalid List Object`

   - Python bytes:
     - Prototype: `void	print_python_bytes(PyObject *p);`
     - If `p` is not a valid `PyBytesObject`: prints `[ERROR] Invalid Bytes Object`
     - Prints a maximum of `10 bytes`

   - Python float:
     - Prototype: `void	print_python_float(PyObject *p);`
     - If `p` is not a valid `PyFloatObject`: prints `[ERROR] Invalid Float Object`

   ### Usage
       #### Create a Dynamic Library
       	    `gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c`
       	    - Python version: 3.4

       #### Import the dynamic library in your python file
       	    ```
	    #!/usr/bin/python3 -u
	    import ctypes

	    lib = ctypes.CDLL('./libPython.so')
	    lib.print_python_list.argtypes = [ctypes.py_object]
	    lib.print_python_bytes.argtypes = [ctypes.py_object]
	    lib.print_python_float.argtypes = [ctypes.py_object]

	    # For Bytes Object
	    s = b"Hello"
	    lib.print_python_bytes(s);

	    # For List Object
	    l = [b'Hello', b'World']
	    lib.print_python_list(l)

	    # For Float Object
	    f = 3.14
	    lib.print_python_float(f);
	    ```