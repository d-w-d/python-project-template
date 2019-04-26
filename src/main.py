'''
Placeholder Doc String
'''

import typing

#
# Demo imports from module and package
#
from module_example import demo_variable_imported_from_module as x
from package_example import demo_variable_imported_from_package as y

print("\n>>>" + x               )
print("\n>>>" + y)

#
# Demo usage of python typing system
# Try changing types to confirm VSCode mypy is correctly integrated
#
example_float: float = 3.14
example_int: int = 1
example_str: str = "Wow!"

example_list: typing.List[typing.Union[float, int, str]] = [
    example_float,
    example_int,
    example_str
]

for i in example_list:
    print("\n-->"+str(i)+"  <-> "+str(type(i)))

# Demo class


class Pet:
    '''Docstring'''

    def __init__(self, name: str, animal: str):
        '''Docstring'''
        self.name = name
        self.animal = animal

    def who_am_i(self: "Pet") -> None:
        '''Docstring'''
        print("\n"+self.name+" is a "+self.animal+"\n\n")


pet1: Pet = Pet("Scooby", "Dog")
pet1.who_am_i()
