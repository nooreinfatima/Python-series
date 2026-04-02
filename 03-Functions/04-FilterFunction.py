'''
The Filter() function constructs an iterator from elements of an iterable for which a function return true. It is used to filter out items from list(or any other iterable) based on a condition. The filter function takes two arguments: the first is a function that returns a boolean value (True or False), and the second is an iterable. The filter function applies the given function to each item of the iterable and returns an iterator that contains only the items for which the function returns True.
'''

def even(num):
    if num%2==0:
        return True
    else:
        return False
print(even(24)) # Output: True
print(even(25)) # Output: False

lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12]

list(filter(even,lst)) # Output: [2, 4, 6, 8, 10,12]

# Filter with lambda function
numbers=[1,2,3,4,5,6,7,8,9]
greater_than_five=list(filter(lambda x:x>5, numbers))
print(greater_than_five) # Output: [6, 7, 8, 9]

# filter with a lambda function and multiple condition
numbers=[1,2,3,4,5,6,7,8,9]
even_and_greater_than_five=list(filter(lambda x:x%2==0 and x>5, numbers))
print(even_and_greater_than_five) # Output: [6, 8]

# Apply filter to check if the age is greater than 25 in a list of dictionaries
people = [
    {"name": "Noorein", "age": 30},
    {"name": "Mariya", "age": 20},
    {"name": "Naseem", "age": 35}
]
filtered_people = list(filter(lambda person: person["age"] > 25, people))
print(filtered_people) # Output: [{'name': 'Noorein', 'age': 30}, {'name': 'Naseem', 'age': 35}]

def age_greater_than_25(person):
    return person["age"] > 25
print(list(filter(age_greater_than_25, people)))# Output: [{'name': 'Noorein', 'age': 30}, {'name': 'Naseem', 'age': 35}]
