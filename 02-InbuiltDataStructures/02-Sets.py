# Sets
# Sets are a built-in data types in python used to store collection of unique items. they are unordered, meaning that the elements do not follow a specific order, and they do not allow duplicate elements.sets are userful for membership tests, eliminating duplicate entries, and performing mathematical set operations like union, intersection, difference and symmetric difference.


## Create a set
my_set={1,2,3,4,5}
print(my_set)
print(type(my_set)) # {1, 2, 3, 4, 5} <class 'set'>

my_empty_set=set([1,2,6,3,4,5,6])
print(my_empty_set) #{1, 2, 3, 4, 5, 6}
print(type(my_empty_set))


# Basics Sets Operation
# Adding and Removing Elements

my_set.add(7)
print(my_set)
my_set.add(7)
print(my_set)

## Remove the elements from a set

my_set.remove(3)
print(my_set) #{1, 2, 4, 5, 7}

## Pop Method
removed_element=my_set.pop()
print(removed_element)
print(my_set)

## Clear all the element
my_set.clear()
print(my_set) #set()

## Set Membership test
my_set={1,2,3,4,5}
print(3 in my_set) # True
print(10 in my_set) # False

## Mathematical Operation
set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}

## Union
union_set=set1.union(set2)
print(union_set) # {1, 2, 3, 4, 5, 6, 7, 8, 9}

## Intersection
intersection_set=set1.intersection(set2)
print(intersection_set) # {4, 5, 6}

set1.intersection_update(set2)
print(set2)

set3={1,2,3,4,5,6}
set4={4,5,6,7,8,9}

## Difference
print(set3.difference(set4)) # {1, 2, 3}

print(set4.difference(set3)) # {8, 9, 7}

## Symmetric Difference

print(set3.symmetric_difference(set4)) # {1, 2, 3, 7, 8, 9}

### Sets Methods important onee----

set1={1,2,3,4,5}
set2={3,4,5}

print(set1.issubset(set2)) # False

print(set1.issuperset(set2)) # True -> it should be either one of the element same as another set

## Counting list of words to set to get unique words

text="In this tutorial we are discussing about sets"
words=text.split()

## convert list of words to get unique words

unique_words=set(words)
print(unique_words) # {'this', 'sets', 'we', 'discussing', 'tutorial', 'In', 'about', 'are'}
print(len(unique_words)) # 8

