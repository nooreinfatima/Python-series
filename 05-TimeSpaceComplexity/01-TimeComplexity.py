""" 
What is Time Complexity?

Time Complexity is a measure of the amount of time an algorithm takes to complete as a function of the size of the input. It is often expressed using Big O notation, which describes the upper bound of the growth rate of an algorithm's running time.
The time complexity of an algorithm can be classified into different categories based on how the running time grows with the size of the input. Some common time complexities include:
1. O(1) - Constant Time: The running time of the algorithm does not depend on the size of the input. It takes a constant amount of time to complete.
2. O(log n) - Logarithmic Time: The running time of the algorithm grows logarithmically with the size of the input. This is often seen in algorithms that divide the input in half at each step, such as binary search.
3. O(n) - Linear Time: The running time of the algorithm grows linearly with the size of the input. This is often seen in algorithms that need to process each element of the input, such as linear search.
4. O(n log n) - Linearithmic Time: The running time of the algorithm grows as n log n with the size of the input. This is often seen in efficient sorting algorithms like merge sort and quicksort.
5. O(n^2) - Quadratic Time: The running time of the algorithm grows quadratically with the size of the input. This is often seen in algorithms that involve nested loops, such as bubble sort.
6. O(2^n) - Exponential Time: The running time of the algorithm grows exponentially with the size of the input. This is often seen in algorithms that generate all possible combinations of the input, such as the brute-force solution to the traveling salesman problem.
7. O(n!) - Factorial Time: The running time of the algorithm grows factorially with the size of the input. This is often seen in algorithms that generate all possible permutations of the input, such as the brute-force solution to the traveling salesman problem.
Understanding the time complexity of an algorithm is crucial for selecting the most efficient algorithm for a given problem
and for optimizing code to run faster. It helps developers make informed decisions about which algorithms to use and how to improve the performance of their code.
"""

n=5
for i in range(n):
    print(i)
print(range(n)) # Output:0 1 2 3 4 range(0, n)

