# Find Duplicate Elements in an Array

def duplicate(arr):
    seen = set()
    duplicates = set()
    
    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    
    return list(duplicates)
arr = [1, 2, 3, 4, 5, 2, 3]
print(duplicate(arr)) # Output: [2, 3]


def duplicate(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return arr[i]
arr = [1, 2, 3, 4, 5, 2, 3]
print(duplicate(arr)) # Output: 2