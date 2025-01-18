# Python - Everything is object
  - What is an object
  - What is the difference between a class and an object or instance
  - What is the difference between immutable object and mutable object
  - What is a reference
  - What is an assignment
  - What is an alias
  - How to know if two variables are identical
  - How to know if two variables are linked to the same object
  - How to display the variable identifier (which is the memory address in the CPython implementation)
  - What is mutable and immutable
  - What are the built-in mutable types
  - What are the built-in immutable types
  - How does Python pass variables to functions

## [0-answer.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/0-answer.txt)
   What function would you use to get the type of an object?

## [1-answer.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/1-answer.txt)
   How do you get the variable identifier (which is the memory address in the CPython implementation)?

## [2-answer.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/2-answer.txt)
   In the following code, do `a` and `b` point to the same object?
   ```
   >>> a = 89
   >>> b = 100
   ```

## [3-answer.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/3-answer.txt)
   In the following code, do `a` and `b` point to the same object?
   ```
   >>> a = 89
   >>> b = 89
   ```

## [4-answer.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/4-answer.txt)
   In the following code, do `a` and `b` point to the same object?
   ```
   >>> a = 89
   >>> b = a
   ```

## [5-answer.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/5-answer.txt)
   In the following code, do `a` and `b` point to the same object?
   ```
   >>> a = 89
   >>> b = a + 1
   ```

## [6-answer.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/6-answer.txt)
   What do these 3 lines print?
   ```
   >>> s1 = "Best School"
   >>> s2 = s1
   >>> print(s1 == s2)
   ```

## [7-answer.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/7-answer.txt)
   What	do these 3 lines print?
   ```
   >>> s1 = "Best School"
   >>> s2 = s1
   >>> print(s1 is s2)
   ```

## [8-answer.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/8-answer.txt)
   What do these 3 lines print?
   ```
   >>> s1 = "Best School"
   >>> s2 = "Best School"
   >>> print(s1 == s2)
   ```

## [9-answer.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/9-answer.txt)
   What do these 3 lines print?
   ```
   >>> s1 = "Best School"
   >>> s2 = "Best School"
   >>> print(s1 is s2)
   ```

## [10-answer.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/10-answer.txt)
   What do these 3 lines print?
   ```
   >>> l1 = [1, 2, 3]
   >>> l2 = [1, 2, 3]
   >>> print(l1 == l2)
   ```

## [11-answer.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/11-answer.txt)
   What do these 3 lines print?
   ```
   >>> l1 = [1, 2, 3]
   >>> l2 = [1, 2, 3]
   >>> print(l1 is l2)
   ```

## [12-answer.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/12-answer.txt)
   What do these 3 lines print?
   ```
   >>> l1 = [1, 2, 3]
   >>> l2 = l1
   >>> print(l1 == l2)
   ```

## [13-answer.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/mas
ter/0x09-python-everything_is_object/13-answer.txt)
   What do these 3 lines print?
   ```
   >>> l1 = [1, 2, 3]
   >>> l2 = l1
   >>> print(l1 is l2)
   ```

## [14-answer.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/14-answer.txt)
   What do this script print?
   ```
   >>> l1 = [1, 2, 3]
   >>> l2 = l1
   >>> l1.append(4)
   >>> print(l2)
   ```

## [15-answer.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/15-answer.txt)
   What do this script print?
   ```
   >>> l1 = [1, 2, 3]
   >>> l2 = [1, 2, 3]
   >>> print(l2)
   ```

## [16-answer.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/16-answer.txt)
   What do this script print?
   ```
   def increment(n):
       n += 1

   a = 1
   increment(a)
   print(a)

   ```

## [17-answer.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/17-answer.txt)
   What do this script print?
   ```
   def increment(n):
       n.append(4)

   l = [1, 2, 3]
   increment(l)
   print(l)

   ```

## [18-answer.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/18-answer.txt)
   What do this script print?
   ```
   def assign_value(n, v):
       n = v

   l = [1, 2, 3]
   l2 = [4, 5, 6]
   assign_value(l1, l2)
   print(l1)

   ```

## [19-copy_list.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/19-copy_list.py)
   A function that returns a copy of a list
   - Prototype: `def copy_list(l)`
   - `l` can contain any type of objects

## [20-answer.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/20-answer.txt)
   ```
   a = ()
   ```
   Is `a` a tuple?

## [21-answer.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/21-answer.txt)
   ```
   a = (1, 2)
   ```
   Is `a` a tuple?

## [22-answer.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/22-answer.txt)
   ```
   a = (1)
   ```
   Is `a` a tuple?

## [23-answer.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/23-answer.txt)
   ```
   a = (1, )
   ```
   Is `a` a tuple?

## [24-answer.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/24-answer.txt)
   What does this script print?
   ```
   a = (1)
   b = (1)
   print(a is b)
   ```

## [25-answer.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/25-answer.txt)
   What	does this script print?
   ```
   a = (1, 2)
   b = (1, 2)
   print(a is b)
   ```

## [26-answer.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/26-answer.txt)
   What	does this script print?
   ```
   a = ()
   b = ()
   print(a is b)
   ```

## [27-answer.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/27-answer.txt)
   ```
   >>> id(a)
   139926795932424
   >>> a
   [1, 2, 3, 4]
   >>> a = a + [5]
   >>> id(a)
   ```
   Will the last line of this script print `139926795932424`?


## [28-answer.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/28-answer.txt)
   ```
   >>> a
   [1, 2, 3]
   >>> id(a)
   139926795932424
   >>> a += [4]
   >>> id(a)
   ```
   Will	the last line of this script print `139926795932424`?

## [100-magic_string.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/100-magic_string.py)
   A function magic_string() that returns a string “BestSchool” `n` times the number of the iteration
   - Prototype: `def magic_string():`

## [101-locked_class.py](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/101-locked_class.py)
   A class `LockedClass` with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called `first_name`

## [103-line1.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/103-line1.txt) [103-line2.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/103-line2.txt)
   ```
   a = 1
   b = 1
   ```
   Assuming we are using a CPython implementation of Python3 with default options/configuration:
   - How many `int objects` are created by the execution of the first line of the script? ([103-line1.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/103-line1.txt))
   - How many `int objects` are created by the execution of the second line of the script? ([103-line2.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/103-line2.txt))

## [104-line1.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/103-line1.txt) [104-line2.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/103-line2.txt) [104-line3.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/104-line3.txt) [104-line4.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/103-line4.txt) [104-line5.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/104-line5.txt)
   ```
   a = 1
   b = 1
   ```
   Assuming we are using a CPython implementation of Python3 with default options/configuration:
   - How many `int objects` are created by the execution of the first line of the script? ([104-line1.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/104-line1.txt))
   - How many `int objects` are created by the execution of the second line of the script? ([104-line2.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/104-line2.txt))
   - After the execution of line 3, is the int object pointed by a deleted? ([104-line3.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/104-line3.txt))
   - After the execution of line 4, is the int object pointed by b deleted? ([104-line4.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/104-line4.txt))
   - How many int objects are created by the execution of the last line of the script? ([104-line5.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/104-line5.txt))

## [105-line1.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/105-line1.txt)
   ```
   print("I")
   print("Love")
   print("Python")
   ```
   Assuming we are using a CPython implementation of Python3 with default options/configuration:
   Before the execution of line 2 (print("Love")), how many int objects have been created and are still in memory? ([105-line1.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/105-line1.txt))

## [106-line1.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/106-line1.txt) [106-line2.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/106-line2.ext) [106-line3.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/106-line3.txt) [106-line4.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/106-line4.txt) [106-line5.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/106-line5.txt)
   ```
   a = "SCHL"
   b = "SCHL"
   del a
   del b
   c = "SCHL"
   ```
   Assuming we are using a CPython implementation of Python3 with default options/configuration:
   - How many `string objects` are created by the execution of the first line of the script? ([106-line1.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/106-line1.txt))
   - How many `string objects` are created by the execution of the second line of the script? ([106-line2.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/106-line2.txt))
   - After the execution of line 3, is the `string object` pointed by a deleted? ([106-line3.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/106-line3.txt))
   - After the execution of line 4, is the `string object` pointed by b deleted? ([106-line4.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/106-line4.txt))
   - How many `string objects` are created by the execution of the last line of the script? ([106-line5.txt](https://github.com/awinabaab/alx-higher_level_programming/blob/master/0x09-python-everything_is_object/106-line5.txt))
