# Python - Data Structures
  - What are lists and how to use them
  - What are the differences and similarities between strings and lists
  - What are the most common methods of lists and how to use them
  - How to use lists as stacks and queues
  - What are list comprehensions and how to use them
  - What are tuples and how to use them
  - When to use tuples versus lists
  - What is a sequence
  - What is tuple packing
  - What is sequence unpacking
  - What is the `del` statement and how to use it

## [0-print_list_integer.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x03-python-data_structures/0-print_list_integer.py)
   A function that prints all integers of a list
   - Prototype: `def print_list_integer(my_list=[]):`

## [1-element_at.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x03-python-data_structures/1-element_at.py)
   A function that retrieves an element from a list like in C
   - Prototype: `def element_at(my_list, idx):`
   - If `idx` is negative, the function should return `None`
   - If `idx` is out of range(> number of elements in `my_list`), the function should return `None`

## [2-replace_in_list.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x03-python-data_structures/2-replace_in_list.py)
   A function that replaces an element of a list at a specific position (like in C)
   - Prototype: `def replace_int_list(my_list, idx, element):`
   - If `idx` is negative, the function should not modify aything, and returns the original list
   - If	`idx` is out of	range(> number of elements in `my_list`), the function should not modify anything, and returns the original list

## [3-print_reversed_list_integer.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x03-python-data_structures/3-print_reversed_list_integer.py)
   A function that prints all integers of a list, in reverse order
   - Prototype: `def print_reversed_list_integer(my_list=[]):`

## [4-new_in_list.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x03-python-data_structures/4-new_in_list.py)
   A function that replaces an element in a list at a specific position without modifying the original list like in C
   - Prototype: `def new_in_list(my_list, idx, element):`
   - If `idx` is negative, the function should return a copy of the original `list`
   - If `idx` is out of range (> number of elements in `my_list`), the function should return a copy of the original list

## [5-no_c.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x03-python-data_structures/5-no_c.py)
   A function that removes all character `c` and `C` from a string
   - Prototype: `def no_c(my_string):`
   - Return: A new string without `c` and `C`

## [6-print_matrix_integer.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x03-python-data_structures/6-print_matrix_integer.py)
   A function that prints a matrix of integers
   - Prototype: `def print_matrix_integer(matrix=[]):`

## [7-add_tuple.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x03-python-data_structures/7-add_tuple.py)
   A function that add 2 tuples
   - Prototype: `def add_tuple(tuple_a=(), tuple_b=()):`
   - Returns tuple with 2 integers:
     - the first element should be the addition of the first element of each argument
     - the second element should be th addition of the second element of each argument
   - If a tuple is smaller than 2, the value `0` will be used for each missing integer
   - If a tuple is bigger that 2, only the first 2 elements will be used

## [8-multiple_returns.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x03-python-data_structures/8-multiple_returns.py)
   A function that returns a tuple with the length of a string and its first character
   - Prototype: `def multiple_returns(sentence):`
   - If the sentence is empty, the first character should be equal to `None`

## [9-max_integer.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x03-python-data_structures/9-max_integer.py)
   A function that finds the biggest integer of a list
   - Prototype: `def max_integer(my_list=[]):`
   - If the list is empty, return `None`

## [10-divisible_by_2.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x03-python-data_structures/10-divisible_by_2.py)
   A function that finds all multiple of 2 in a list
   - Prototype: `def divisible_by_2(my_list-[]):`
   - Return a new list with `True` or `False`, depending in whether the integer at the same position in the original list is a multiple of 2
   - The new list should have the same size as the original list

## [11-delete_at.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x03-python-data_structures/11-delete_at.py)
   A function that deletes the item at a specific position in a list
   - Prototype: `def delete_at(my=[], idx=0):`
   - If `idx` is negative or out of range, nothing changes(returns the same list)

## [12-switch.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x03-python-data_structures/12-switch.py)
   Complete the [source code](https://intranet.alxswe.com/rltoken/9kg8R2hfPSN5pClcVAeGlA) in order to switch value of `a` and `b`

## [13-is_palindrome.c](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x03-python-data_structures/13-is_palidrome.c)
   A function in C that checks if a singly linked list is a palindrome
   - Prototype: `int is_palidrome(listint_t **head);`
   - Return: `0` if it is not a palindrom, `1` if it is a palindrome
   - An ampty list is considered a palidrome

## [100-print_python_list_info.c](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x03-python-data_structures/100-print_python_list_info.c)
   - Create a C function that prints some basic info about Python lists.
   - Prototype: `void print_python_list_info(PyObject *p);`