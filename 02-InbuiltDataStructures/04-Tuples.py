### Tuples

# Tuples are ordered collection of items that are immutable. they are similar to lists, but their immutability makes them different

## Creating a Tuple

empty_tuple=()
print(empty_tuple) # ()
print(type(empty_tuple)) # <class 'tuple'>

numbers=tuple([1,2,3,4,5,6])
print(numbers)

mixed_tuple=(1, "Hello World",3.14,True)
print(mixed_tuple) # (1, 'Hello World', 3.14, True)

## Accessing Tuple Elements

print(numbers[0])
print(numbers[2])
print(numbers[-1])
print(numbers[::-1]) # (6, 5, 4, 3, 2, 1)

# Tuple Operations
concatenation_tuple=numbers + mixed_tuple
print(concatenation_tuple) # (1, 2, 3, 4, 5, 6, 1, 'Hello World', 3.14, True)

print (mixed_tuple * 3) # (1, 'Hello World', 3.14, True, 1, 'Hello World', 3.14, True, 1, 'Hello World', 3.14, True)

print(numbers*3) # (1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6)

## Immutable Nature of Tuples
## Tuples are immutable, meaningtheir elements cannot be changed once assigned.

lst=[1,2,3,4,5]
print(lst) # [1, 2, 3, 4, 5]

lst3="Jyoshita"
print(lst3)

lst[1]="Noorein"
print(lst) # [1, 'Noorein', 3, 4, 5]

## Tuple Methods

print(numbers.count(1)) # 1
print(numbers.index(3)) # 2

## Packing and unpacking tuple

# Packing
packed_tuple=1,"Hello",3.14
print(packed_tuple) # (1, 'Hello', 3.14)

# Unpacking
a,b,c=packed_tuple
print(a)
print(b)
print(c)

# Unpacking with *
numbers=(1,2,3,4,5,6)
first,*middle,last=numbers
print(first) # 1
print(middle) # [2, 3, 4, 5]
print(last) # 6

## Nested Tuple
##  Nested List
lst=[[1,2,3,4],[6,7,8,9],[1,"Hello",3.14,"c"],]
print(lst[0][2])
print(lst[2][0:3]) # [1, 'Hello', 3.14]

nested_tuple=((1,2,3),('a','b','c'),(True, False))

print(nested_tuple[1][2])

# iterating over nested tuples
for sub_tuple in nested_tuple:
  for item in sub_tuple:
    print(item,end="")
  print() 
'''
output:
123
abc
TrueFalse
'''

## Conclusion

# Tuples are versatile and useful in many real-world scenarios where an immutable and ordered collection of items is required. they are commonly used in data structure, function arguments and return values, and as dictionary keys. Understanding how to leverage tuples effectively can improve the efficiency and readability of python code