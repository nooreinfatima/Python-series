# What is Space Complexity?
"""
Space Complexity is a measure of the amount of memory an algorithm uses as a function of the size of the input. It is often expressed using Big O notation, which describes the upper bound of the growth rate of an algorithm's memory usage.
The space complexity of an algorithm can be classified into different categories based on how the memory usage grows with the size of the input. Some common space complexities include:
1. O(1) - Constant Space: The amount of memory used by the algorithm does not depend on the size of the input. It uses a constant amount of memory regardless of the input size.
2. O(n) - Linear Space: The amount of memory used by the algorithm grows linearly with the size of the input. This is often seen in algorithms that use arrays or lists to store all elements of the input.
3. O(n^2) - Quadratic Space: The amount of memory used by the algorithm grows quadratically with the size of the input. This is often seen in algorithms that use 2D arrays or matrices to store all pairs of elements from the input.
Understanding the space complexity of an algorithm is crucial for selecting the most efficient algorithm for a given problem and for optimizing code to use less memory. It helps developers make informed decisions about which algorithms to use and how to improve the performance of their code by reducing memory usage.
"""

def find_max(arr):
    max_element=arr[0]
    for num in arr:
        if num > max_element:
            max_element=num
    return max_element
arr=[1,2,3,4,5]
print(find_max(arr)) # Output: 5


def find_min(arr):
    min_element=arr[0]
    for num in arr:
        if num < min_element:
            min_element=num
        return min_element
arr=[8,23,14,5,45,50]
print(find_min(arr)) # output : 8