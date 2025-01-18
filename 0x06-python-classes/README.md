# Python - Classes and Objects
  - What is `OOP`
  - “first-class everything”
  - What is a `class`
  - What is an `object` and an `instance`
  - What is the difference between a `class` and an `object` or `instance`
  - What is an attribute
  - What are and how to use `public`, `protected` and `private` attributes
  - What is `self`
  - What is a `method`
  - What is the special `__init__` method and how to use it
  - What is `Data Abstraction`, `Data Encapsulation`, and `Information Hiding`
  - What is a property
  - What is the difference between an `attribute` and a `property` in Python
  - What is the Pythonic way to write `getters` and `setters`
  - How to dynamically create arbitrary new attributes for existing instances of a `class`
  - How to bind `attributes` to `object` and `classes`
  - What is the `__dict__` of a `class` and/or `instance` of a class and what does it contain
  - How does Python find the `attributes` of an `object` or `class`
  - How to use the `getattr` function

## [0-square.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x06-python-classes/0-square.py)
   An empty class `Square` that defines a square

## [1-square.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x06-python-classes/1-square.py)
   A class `Square` that defines a square by: (base on [0-square.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x06-python-classes/0-square.py)
   - Private instance attribute: `size`
   - Instantiation with `size` (no type/value verification)

## [2-square.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x06-python-classes/2-square.py)
   A class `Square` that defines a square by: (based on [1-square.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x06-python-classes/1-square.py)
   - Private instance attribute: `size`
   - Instantiation with optional `size`: `def __init__(self, size=0):`
     - `size` must be an integer, otherwise a `TypeError` exception with the message `size must be an integer` is raised
     - If `size` is less than `0`, a `ValueError` exception with the message `size must be >= 0` is raised

## [3-square.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x06-python-classes/3-square.py)
   A class `Square` that defines a square by: (based on [2-square.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x06-python-classes/2-square.py)
   - Private instance attribute: `size`
   - Instantiation with optional `size`: `def __init__(self, size=0):`
     - `size` must be an integer, otherwise a `TypeError` exception with the message `size must be an integer` is raised
     - If `size` is less than `0`, a `ValueError` exception with the message `size must be >= 0` is raised
   - Public instance method: `def area(self):` that returns te current square area

## [4-square.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x06-python-classes/4-square.py)
   A class `Square` that defines a square by: (based on [3-square.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x06-python-classes/3-square.py)
   - Private instance attribute: `size`:
     - Property `def size(self):` to retrieve it
     - Property setter `def size(self, value):` to set it:
       - `size` must be an integer, otherwise a `TypeError` exception with the message `size must be an integer` is raised
       - If `size` is less than `0`, a `ValueError` exception with the message `size must be >= 0` is raised
   - Instantiation with optional `size`: `def __init__(self, size=0):`
   - Public instance method: `def area(self):` that returns te current square area

## [5-square.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x06-python-classes/5-square.py)
   A class `Square` that defines a square by: (based on [4-square.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x06-python-classes/4-square.py)
   - Private instance attribute: `size`:
     - Property	`def size(self):` to retrieve it
     - Property	setter `def size(self, value):`	to set it:
       - `size` must be an integer, otherwise a `TypeError` exception with the message `size must be an integer` is raised
       - If `size` is less than `0`, a `ValueError` exception with the message `size must be >= 0` is raised
   - Instantiation with optional `size`: `def __init__(self, size=0):`
   - Public instance method: `def area(self):` that returns te current square area
   - Public instance method: `def my_print(self):` that prints in `stdout` the square with the character `#`:
     - if `size` is equal to `0`, print an empty line

## [6-square.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x06-python-classes/6-square.py)
   A class `Square` that defines a square by: (based on [5-square.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x06-python-classes/5-square.py)
   - Private instance attribute: `size`:
     - property `def size(self):` to retrieve it
     - property setter `def size(self, value):` to set it:
       - `size` must be an integer, otherwise a `TypeError` exception with the message `size must be an integer` is raised
       - if `size` is less than `0`, a `ValueError` exception with the message `size must be >= 0` is raised
   - Private instance attribute: position:
     - property `def position(self):` to retrieve it
     - property setter `def position(self, value):` to set it:
       - position must be a `tuple` of `2 positive integers`, otherwise a `TypeError` exception with the message `position must be a tuple of 2 positive integers` is raised
   - Instantiation with optional `size` and `position`: `def __init__(self, size=0, position=(0, 0):`
   - Public instance method: `def area(self):` that returns te current square area
   - Public instance method: `def my_print(self):` that prints in `stdout` the square with the character `#`:
     - if `size` is equal to `0`, print an empty line
     - `position` will be printed by using `spaces` - except when when position[1] > 0

## [100-singly_linked_list.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x06-python-classes/100-singly_linked_list.py)
   A class `Node` that defines a node of a singly linked list by:
   - Private instance attribute: `data`:
     - property `def data(self):` to retrieve it
     - property setter `def data(self, value):` to set it:
     - `data` must be an integer, otherwise a `TypeError` exception with the message `data must be an integer` is raised
   - Private instance attribute: `next_node`:
     - property `def next_node(self):` to retrieve it
     - property setter `def next_node(self, value):` to set it:
     - `next_node` can be `None` or must be a Node, otherwise a `TypeError` exception with the message `next_node must be a Node object` is raised
   - Instantiation with `data` and `next_node`: `def __init__(self, data, next_node=None):`

   A class SinglyLinkedList that defines a singly linked list by:
   - Private instance attribute: `head` (no setter or getter)
   - Simple instantiation: `def __init__(self):`
   - Should be printable:
     - prints the entire list in `stdout`
     - one node number by line
   - Public instance method: `def sorted_insert(self, value):` that inserts a new Node into the correct sorted position in the list (increasing order)

## [101-square.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x06-python-classes/102-square.py)
   A class `Square` that defines a square by: (based on [6-square.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x06-python-classes/6-square.py)
   - Private instance attribute: `size`:
     - property `def size(self):` to retrieve it
     - property setter `def size(self, value):` to set it:
     - `size` must be an integer, otherwise a `TypeError` exception with the message `size must be an integer` is raised
     - if `size` is less than `0`, a `ValueError` exception with the message `size must be >= 0` is raised
   - Private instance attribute: `position`:
     - property `def position(self):` to retrieve it
     - property setter `def position(self, value):` to set it:
     - position must be a `tuple` of `2 positive integers`, otherwise a `TypeError` exception with the message `position must be a tuple of 2 positive integer` is raised
   - Instantiation with optional size and optional `position`: `def __init__(self, size=0, position=(0, 0)):`
   - Public instance method: `def area(self):` that returns the current square area
   - Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
     - if `size` is equal to `0`, print an empty line
     - `position` wiil be printed using space
   - Printing a `Square` instance will have the same behavior as calling `my_print()` method an instance

## [102-square.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x06-python-classes/102-square.py)
   A class `Square` that defines a square by: (based on [4-square.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x06-python-classes/4-square.py)
   - Private instance attribute: `size`:
     - property `def size(self)`: to retrieve it
     - property setter `def size(self, value)`: to set it:
     - `size` must be a number (float or integer), otherwise a `TypeError` exception with the message `size must be a number` is raised
     - if `size` is less than `0`, a `ValueError` exception with the message `size must be >= 0` is raised
     - Instantiation with `size`: `def __init__(self, size=0):`
   - Public instance method: `def area(self):` that returns the current square area
   - `Square` instance can answer to comparators: `==`, `!=`, `>`, `>=`, `<` and `<=` based on the square area

## [103-magic_class.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x06-python-classes/103-magic_class.py)
   A class `MagicClass` that does exactly the same as the following Python bytecode:
   ```
   Disassembly of __init__:
 10           0 LOAD_CONST               1 (0)
              3 LOAD_FAST                0 (self)
              6 STORE_ATTR               0 (_MagicClass__radius)

 11           9 LOAD_GLOBAL              1 (type)
             12 LOAD_FAST                1 (radius)
             15 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             18 LOAD_GLOBAL              2 (int)
             21 COMPARE_OP               9 (is not)
             24 POP_JUMP_IF_FALSE       60
             27 LOAD_GLOBAL              1 (type)
             30 LOAD_FAST                1 (radius)
             33 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             36 LOAD_GLOBAL              3 (float)
             39 COMPARE_OP               9 (is not)
             42 POP_JUMP_IF_FALSE       60

 12          45 LOAD_GLOBAL              4 (TypeError)
             48 LOAD_CONST               2 ('radius must be a number')
             51 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             54 RAISE_VARARGS            1
             57 JUMP_FORWARD             0 (to 60)

 13     >>   60 LOAD_FAST                1 (radius)
             63 LOAD_FAST                0 (self)
             66 STORE_ATTR               0 (_MagicClass__radius)
             69 LOAD_CONST               3 (None)
             72 RETURN_VALUE

Disassembly of area:
 17           0 LOAD_FAST                0 (self)
              3 LOAD_ATTR                0 (_MagicClass__radius)
              6 LOAD_CONST               1 (2)
              9 BINARY_POWER
             10 LOAD_GLOBAL              1 (math)
             13 LOAD_ATTR                2 (pi)
             16 BINARY_MULTIPLY
             17 RETURN_VALUE

Disassembly of circumference:
 21           0 LOAD_CONST               1 (2)
              3 LOAD_GLOBAL              0 (math)
              6 LOAD_ATTR                1 (pi)
              9 BINARY_MULTIPLY
             10 LOAD_FAST                0 (self)
             13 LOAD_ATTR                2 (_MagicClass__radius)
             16 BINARY_MULTIPLY
             17 RETURN_VALUE
    ```