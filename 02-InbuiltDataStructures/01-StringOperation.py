''' 
1. Introduction to lists
2. Creating Lists
3. Accessing List Elements
4. Modifying List Elements
5. List Methods
6. Slicing lists
7. Iterating Over Lists
8. List Comprehensions
9. Nested Lists
10.Practicall Examples and Common Errors

'''

# List are ordered, mutable collections of items they can contain items of different Data Types

'''lst=[]
print(type(lst))

names=["Noorein", "Fatima", 1,2,3,4,5]
print(names)

mixed_list=[1,"Hello",3.14,True]
print(mixed_list)

## Accessing Lists Elements

fruits=["apple","banana","cherry","kiwi","gauva"]
print(fruits[0])
print(fruits[2])
print(fruits[4])
print(fruits[-1])#last element
print(fruits[1:])#banana,cherry,kiwi,gauva
print(fruits[1:3]) #banana,cherry
print(fruits[-1:-3]) # []

# Modifying the lists elements
fruits[1]="Watermelon"
print(fruits)

fruits[1:]="Watermelon"
print(fruits)

# List Method

fruits.append("Orange") # Add an item to the end
print(fruits)

fruits.insert(1, "Watermelon")
print(fruits)

#fruits.remove("banana") # Removing the frist occurance of an item
#print(fruits)

## Remove and return the last 
popped_fruits=frist.pop()
print(popped_fruits) # here orange removed
print(fruits)

index=fruits.index("cherry")
print(index)

fruits.insert(2,"banana")
print(fruits.count("banana"))
print(fruits)
print(fruits.sort()) # Sort the list in ascending order

print(fruits)

print(fruits.reverse()) # Reverse the list

print(fruits.clear()) # Remove all items from the list

print(fruits)'''

# Slicing List
'''numbers=[1,2,3,4,5,6,7,8,9,10]
print(numbers[2:5])
print(numbers[:5])
print(numbers[5:])
print(numbers[::2])
print(numbers[::-1])

# Iterating With index
for index,number in enumerate(numbers):
  print(index,numbers)
  
# List Comprehension

lst=[]
for x in range(10):
  lst.append(x**2)
print(lst) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

[x**2 for x in range(10)] 
print(lst)''' # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

### List Comprehension -> Syntx ->> [expression for item in iterable]

## With conditional logic -> [expression for item in iterable if condition]

## Nested List Comprehension ->  [expression for item1 in iterable1 for item2 in iterable2]

'''sqaure=[num ** for num i range(10)]
print(sqaure)'''

lst=[]
for i in range(10):
  if i%2==0:
    lst.append(i)
print(lst) # [0, 2, 4, 6, 8]

even_numbers=[num for num in range(10) if num%2==0]
print(even_numbers) # [0, 2, 4, 6, 8]

# Nested List Comphrension

lst1=[1,2,3,4]
lst2=["a","b","c","d"]

pair=[[i,j] for i in lst1 for j in lst2]

print(pair) # [[1, 'a'], [1, 'b'], [1, 'c'], [1, 'd'], [2, 'a'], [2, 'b'], [2, 'c'], [2, 'd'], [3, 'a'], [3, 'b'], [3, 'c'], [3, 'd'], [4, 'a'], [4, 'b'], [4, 'c'], [4, 'd']]


## List Comprehension with function calls

words=["Hello","World", "Python", "List", "Comprehension"]
length=[len(word) for word in words]
print(length) # [5, 5, 6, 4, 13]


# conclusion -> 
# List Comprehensions are a powerful and concise way to create lists in python. they are syntactically compact and can replace more verbose looping constructs. Understanding the syntax of list comprehensions will help you write cleaner and more efficient python code