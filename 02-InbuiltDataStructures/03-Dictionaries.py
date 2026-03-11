### Dictionaries
'''
Introduction to Dictionaries
Creating Dictionaries
Accessing Dictionary Element
Modifying Dictionary Element
Dictionary Methods
Iterating Over Dictionaries
Nested Dictionaries
Dictionary Comprehensions
Practice Examples and Common Errors
'''

## Introduction To Dictionaries

''' Dictionaries are unordered collection of items. They store data in key-value pairs. Keys must be unique and immutable (e.g., strings, numbers, or tuples), While values can be of any type '''

## Creating Dictionaries
empty_dict={}
print(type(empty_dict)) # <class 'dict'>

student={"name": "Noorein", "age":21,"grade":16}
print(student) # {'name': 'Noorein', 'age': 21, 'grade': 16}
print(type(student)) # <class 'dict'>

# single key always use

## Accessing Dictionary elements
student={"name":"Noorein","age":21,"grade":"A"}
print(student)
print(student['grade'])
print(student['age'])

# Accesing using get() method

print(student.get("grade"))
print(student.get("last_name")) # None
print(student.get("last_name","Not Available")) # Not Available

## Modifying Dicitonary Elements
## Dictionary are mutable, so you can add, update or delete elements
print(student)

student["age"]=33 #--> Updated
print(student) # {'name': 'Noorein', 'age': 33, 'grade': 'A'} 
student["address"]="India"  # --> Added
print(student) #{'name': 'Noorein', 'age': 33, 'grade': 'A', 'address': 'India'}
del student['grade'] ## delete
print(student) # {'name': 'Noorein', 'age': 33, 'address': 'India'}

## Dictionary Methods
keys=student.keys()
print(keys) # dict_keys(['name', 'age', 'address'])
values=student.values()
print(values) # dict_values(['Noorein', 33, 'India'])
items=student.items()
print(items) # dict_items([('name', 'Noorein'), ('age', 33), ('address', 'India')]) --> list of tuples

## Shallow Copy 
student_copy=student
print(student) # {'name': 'Noorein', 'age': 33, 'address': 'India'}
print(student_copy) # {'name': 'Noorein', 'age': 33, 'address': 'India'}

student["name"]="Noorein Fatima"
print(student) # {'name': 'Noorein Fatima', 'age': 33, 'address': 'India'}
print(student_copy) # {'name': 'Noorein Fatima', 'age': 33, 'address': 'India'}

##shallow copy-->

student_copy1=student.copy()
print(student_copy1) # {'name': 'Noorein Fatima', 'age': 33, 'address': 'India'}
print(student) # {'name': 'Noorein Fatima', 'age': 33, 'address': 'India'}

student["name"]="Noorein2"
print(student_copy)
print(student)

##  Iterating Over Dictionaries
##  you can use loops to iterate over dictionaries, key,values, items
## Iterating Over keys
for keys in student.keys():
  print(keys) # name age address

## Iterate over values 
for value in student.values():
  print(value) # Noorein2 33 India
  
## Iterate over key value pairs
for key,value in student.items():
  print(f"{key}:{value}") # name:Noorein2 age:33 address:India
  
## Nested Dictionaries --> Dictionaries inside a Dictionaries
students={
  "student":{"name":"Noorein","age":21},
  "student2":{"name":"peter","age":25}
}
print(students) # {'student': {'name': 'Noorein', 'age': 21}, 'student2': {'name': 'peter', 'age': 25}}

## Access nested dictionaries elements
print(students["student2"]["name"]) # peter
print(students["student2"]["age"]) # 25

student.items()
## Iterating over nested dictionaries
for student_id,student_info in students.items():
  print(f"{student_id}:{student_info}")
  for key,value in student_info.items():
    print(f"{key}:{value}")
''' Output 
student:{'name': 'Noorein', 'age': 21}
name:Noorein
age:21
student2:{'name': 'peter', 'age': 25}
name:peter
age:25
'''
# Dictionary Comphrension

squres={x:x**2 for x in range(5)}
print(squres) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

evens={x:x**2 for x in range(10) if x%2==0}
print(evens) # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

## Practical Examples
# Use a dictionary to count he frequence of elements in list

numbers=[1,2,2,3,3,3,4,4,4,4]
frequecy={}

for number in numbers:
  if number in frequecy:
    frequecy[number]+=1 
  else:
    frequecy[number]=1
print(frequecy) # {1: 1, 2: 2, 3: 3, 4: 4}

## Merge 2 dictionaries into one

dict1={"a":1,"b":2}
dict2={"b":3,"c":4}
merged_dict={**dict1,**dict2}
print(merged_dict)