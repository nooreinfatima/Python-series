## Introduction to Functions

# A Function is a block of code it performs a Specific task. Functions help in organizing code, and improving readability


# Syntax
def function_name(parameters):
  '''Docstring'''
  # Function body
  return expression


# Why functions
num=24
if num%2==0:
  print("the number is even")
else:
  print("the number is odd")

# function writing
def even_or_odd(num):
  """This function finds even or odd"""
  if num%2==0:
    print("the number is even")
  else:
    print("the number is odd")
    
## Call this Function
even_or_odd(24)

# Function with multiple parameters
def add(a,b):
  return a+b
result=add(2,4)
print(result)


# Default parameters
def greet(name):
  print(f"Hello {name} Welcome to the paradise")

greet("Noorein") # Hello Noorein Welcome to the paradise

def greet(name="Fatima"):
  print(f"Hello {name} Welcome to the paradise")

greet()

# Variable Length Arguments
# Positional and keywords arguments

def print_numbers(*args):
  for number in args:
    print(number)

print_numbers(1,2,3,4,5,6,7,8,9,"Noorein")

## Keywords Arguments

def print_details(**kwargs):
  for key,value in kwargs.items():
    print(f"{key}:{value}")

print_details(name="Noorein",age="21",country="India")

def print_details(*args,**kwargs):
  for val in args:
    print(f"Positional argument:{val}")
  for key,value in kwargs.items():
    print(f"{key}:{value}")

print_details(1,2,3,4,5,"Noorein",name="Noorein",age="21",country="India")

# Return Statments
def multiple(a,b):
  return a*b
multiple(2,8)

# Return multiple parameters
def multiple(a,b):
  return a*b,a
multiple(2,8)

