def has_pair(arr,target):
    left, right=0, len(arr)-1
    while left<right:
        current_sum=arr[left]+arr[right]
        if current_sum==target:
            return True
        elif current_sum<target:
            left+=1
        else:
            right-=1
    return False
arr=[1,2,3,4,5]
target=7
print(has_pair(arr,target)) # Output: True