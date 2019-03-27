# '''
# Doc string
# '''

import os
import typing

from module_example import xxx

print(xxx)

print("This line is way too long!!! -------------------------------------------------------------------------------------------------")

# my_directories: typing.List[str] = os.listdir()

# print(my_directories)


class MyClass:
    '''Token Docstring'''
    x = 5


p1: MyClass = MyClass()
print(p1.x)


x: int = 1


def test_xxx() -> None:
    z = 1
    assert 1 == 1
