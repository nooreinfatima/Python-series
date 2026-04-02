'''
Map function is used to apply a given function to each item of an iterable (like a list) and return a map object (which is an iterator). The map function takes two arguments: the first is the function to apply, and the second is the iterable. The map function applies the given function to each item of the iterable and returns a map object that can be converted into a list or other iterable types.
'''

def square(x):
    return x ** 2
print(square(10)) # Output: 100

numbers = [1, 2, 3, 4, 5,7,8]

# map takes two input operation one is a number and another one is a iterable
map(square,numbers) # Output: <map object at 0x7f8c8c8c8c8>
squared_numbers=list(map(square,numbers))
print(squared_numbers) # Output: [1, 4, 9, 16, 25, 49, 64]

numbers = [1, 2, 3, 4, 5,7,8]
list(map(lambda x:x*x,numbers)) # Output: [1, 4, 9, 16, 25, 49, 64]

# can we map multiple iterables

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
added_numbers=map(lambda x,y:x+y, numbers1, numbers2)
print(added_numbers) # Output: <map object at 0x7f8c8c8c8c8>

## map() to convert a list of strings to uppercase
# use map() to convert a list of strings to uppercase
str_numbers=['1','2','3','4','5']
int_numbers=list(map(int,str_numbers))
print(int_numbers) # Output: [1, 2, 3, 4,5]

words=['apple','banana','cherry']
upper_word=list(map(str.upper,words ))
print(upper_word) # Output: ['APPLE', 'BANANA', 'CHERRY']   

def get_name(person):
    return person['name']
people =[{'name': 'Noorein', 'age': 21},
         {'name': 'Alisha', 'age': 22},
         {'name': 'Neha', 'age': 25}]

print(list(map(get_name,people))) # Output: ['Noorein', 'Alisha', 'Neha']