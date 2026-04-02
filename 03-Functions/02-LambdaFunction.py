'''
Lambda functions are anonymous functions that can be defined in a single line. They are often used for short, simple functions that are not reused elsewhere in the code. The syntax for a lambda function is defined using the lambda keywword.they can have any number of argument but only one expression. They are commonly used for short operations or as arguments to higher-order functions.
'''
# Synatx
#lambda arguments: expression

def addition(a,b):
    return a + b

print(addition(5, 3) )# Output: 8

addition=lambda a,b:a+b
print(type(addition)) # Output: <class 'function'>

def even(num):
    if num%2==0:
        return True
    

print(even(24)) # Output: True

even1=lambda num:num%2==0
print(even1(24)) # Output: True

def addition(x, y,z):
    return x + y +z
print(addition(5, 3,2))  # Output: 10

addition1=lambda x,y,z:x+y+z
print(addition1(5, 3,2))  # Output: 10

# map()
numbers = [1, 2, 3, 4, 5]
def square(number):
    return number ** 2

print(square(2)) # Output: 4

lambda_square=lambda number:number**2
print(lambda_square(2)) # Output: 4

map(lambda x:x**2,numbers) # Output: <map object at 0x7f8c8c8c8c8>
squared_numbers=list(map(lambda x:x**2,numbers))
print(squared_numbers) # Output: [1, 4, 9, 16, 25]