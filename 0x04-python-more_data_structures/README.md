# Python - More Data Structures
  - What are sets and how to use them
  - What are the most common methods of set and how to use them
  - When to use sets versus lists
  - How to iterate into a set
  - What are dictionaries and how to use them
  - When to use dictionaries versus lists or sets
  - What is a key in a dictionary
  - How to iterate over a dictionary
  - What is a lambda function
  - What are the map, reduce and filter functions

## [0-square_matrix_simple.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/0-square_matrix_simple.py)
   A function that computes the square value of all integers of a matrix
   - Prototype: `def square_matrix_simple(matrix=[]):`
   - Return: A new matrix;
     - same size as `matrix`
     - each value should be squared of the value of the input
   - Initial matrix should not be modified

## [1-search_replace.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/1-search_replace.py)
   A function that replaces all occurrences of an element by another in a new list
   - Prototype: `def search_replace(my_list, search, replace):`
   - `my_list` is the initial list
   - `search is the element to be replaced in the list
   - `replace` is the new element

## [2-uniq_add.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/2-uniq_add.py)
   A function that adds all unique integers in a list
   - Prototype: `def uniq_add(my_list=[]):`

## [3-common_elements.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/3-common_elements.py)
   A function that returns a set of common elements in two sets
   - Prototype: `def common_elements(set_1, set_2):`

## [4-only_diff_elements.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/4-only_diff_elements.py)
   A function that returns a set of all elements present in only one set
   - Prototype: `def only_diff_elements(set_1, set_2):`

## [5-number_keys.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/5-number_keys.py)
   A function that returns the number of keys in a dictionary
   - Prototype: `def number_keys(a_dictionary):`

## [6-print_sorted_dictionary.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/6-print_sorted_dictionary.py)
   A function that prints a dictionary by ordered keys
   - Prototype: `def print_sorted_dictionary(a_dictionary):`

## [7-update_dictionary.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/7-update_dictionary.py)
   A function that replaces or adds key/value in a dictionary
   - Prototype: `def update_dictionary(a_dictionary, key, value):`
   - If a key exists in the dictionary, the value will be replaced
   - If a key doesn't exist in the dictionary, it will be created

## [8-simple_delete.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/8-simple_delete.py)
   A function that deletes a key in a dictionary
   - Prototype: `def simple_delete(a_dictionary, key=""):`
   - If `key` doesn't exist, the dictionary won't change

## [9-multiply_by_2.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/9-multiply_by_2.py)
   A function that returns a new dictionary with all the values multiplied by 2
   - Prototype: `def multiply_by_2(a_dictionary):`
   - Returns a new dictionary

## [10-best_score.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/10-best_score.py)
   A function that returns a key with the biggest integer value
   - Prototype: `def best_score(a_dictionary):`
   - Return `None` if no score is found

## [11-multiply_list_map.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/11-multiply_list_map.py)
   A function that returns a list with all values multiplied by a number without using any loops
   - Prototype: `def multiply_list_map(my_list=[], number=00:`
   - Returns a new list:
     - same length as `my_list`
     - each value should be multiplied by `number`
   - Initial list should not be modified

## [12-roman_to_int.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/12-roman_to_int.py)
   A function that converst a Roman numeral to an integer
   - Prototype: `def roman_to_int(roman_string):`
   - Returns an integer
   - If the `roman_string` is not a string or `None`, return `0`

## [100-weight_average.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/100-weight_average.py)
   A function that returns the weighted average of all integers in a tuple
   - Prototype: `def weight_aveage(my_list=[]):`
   - Returns `0` if list is empty

## [101-square_matrix_map.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/101-square_matrix_map.py)
   A function that computes th square value of all inteers of a matrix using `map`
   - Prototype: `def square_matrix_map(matrix=[]):`
   - Returns anew matrix:
     - same size as `matrix`
     - each value should be the square of the value of input
   - Initial matrix should not be modified

## [102-complex_delete.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/102-complex_delete.py)
   A function that deletes keys with a specific value in a dictionary
   - Prototype: `def complex_delete(a_dictionary, value):`
   - If the values doesn't exist, the dictionary won't change
   - All keys having the searched value have to be deleted

## [103-pyton.c](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/103-python.c)
   Create two C functions that print some basic info about Python lists and Python bytes objects.
   - Python lists:
     - Prototype: `void print_python_list(PyObject *p);`
   - Python bytes:
     - Prototype: `void print_python_bytes(PyObject *p);`
     - Prints a maximum of 10 bytes