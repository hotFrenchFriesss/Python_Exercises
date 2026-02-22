# This is a public method and variables
class Cat:
    def __init__(self, name, age): # Constructor
        self.name = name # Public variable | attribute
        self.age = age # Public variable | attribute
        
    def meow(self): # Public Method
        print(f"{self.name} is meowing!")
        
# -------------------------------------------------------------------

# This is a protected method and variables
class Dog:
    def __init__(self, name, age): # Constructor
        self._name = name # Protected variable using one underscore | attribute
        self._age = age # Protected variable using one underscore | attribute
        
    def bark(self): # Protected Method
        print(f"{self._name} is barking!")

# -------------------------------------------------------------------

# This is a private method and variables
class Human:
    def __init__(self, name, age): # Constructor
        self.__name = name # Private variable using two underscore | attribute
        self.__age = age # Private variable using two underscore | attribute
        
    def get_info(self): # Private Method
        print(f'My name is ' + my_human.__name, f'and I am {my_human.__age} years old!\n')
    def focus(self): # Private Method
        print(f'{my_human.__name} is focused!')

# -------------------------------------------------------------------

# Create an object 
my_cat = Cat('Kreme', 3)
my_dog = Dog('Tyler', 6)
my_human = Human('Axel', 19)

# -------------------------------------------------------------------

print(f'\n- This is a public class in use\n\n====================================================\n')

# Print cat name (Kreme) and age (3)
print(f'My cat\'s name is ' + my_cat.name, f'and he is {my_cat.age} years old!\n')

# Print cat meowing
my_cat.meow()
print(f'\n====================================================\n')

# --------------------------------------------------------------------

print(f'- This is a protected class in use\n\n====================================================\n')

# Print dog name (Tyler) and age (6)
print(f'My dog\'s name is ' + my_dog._name, f'and he is {my_dog._age} years old!\n')

# Print dog barking
my_dog.bark()
print(f'\n====================================================\n')

# -------------------------------------------------------------------

print(f'- This is a private class in use\n\n====================================================\n')

# Print human name (Axel) and age (19)
my_human.get_info()

# Print human focusing
my_human.focus()

print(f'\n====================================================\n')




