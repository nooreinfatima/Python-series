'''
For Loop 
While Loop
'''

## For loop

for i in range(5): 
  print(i) # 0 1 2 3 4 
  
print("next example")
for i in range(1,6):
  print(i) # 1 2 3 4 5 
  
print("next example")

for i in range(1,10,1): # 1-starting, 10-before 10 it will stop, 2- two numbers will incement
  print(i) # 1 2 3 4 5 6 7 8 9


print("next example")

for i in range(1,10,2):
  print(i) #1 3 5 7 9
  
print("next example")

for i in range(10,1,-1):
  print(i) # 10 9 8 7 6 5 4 3 2 
  
  
print("next example")

str="Noorein Fatima"
for i in str:
  print(i)
  
  
  
## While Loop

#  The while loop continues to execute as long as the condition is true

count=0

while count<5:
  print(count)
  count=count+1 # 0 1 2 3 4 

print("next example")

count=0

while count%2==0:
  print(count)
  count=count+1
  

## Loop control statment

# Break
## The break statment exits the loop permanturely

print("break example")

for i in range(10):
  if i==5:
    break
  print(i)
  
# Continue
## The continue statment skips the current iteration and continues with the next 


print("continue example")

for i in range(10):
  if i%2==0:
    continue
  print(i)
  
## pass
# The pass statement is a null operationit does nothing

for i in range(5):
  if i==3:
    print("The number is",i)
    pass
  print(i) # 0 1 2 3 4
  
## Nested Loopss
## a loop inside a loop

for i in range(3):
  for j in range(2):
    print(f"i:{i} and j:{j}")
#output 
''' 
i:0 and j:0
i:0 and j:1
i:1 and j:0
i:1 and j:1
i:2 and j:0
i:2 and j:1 
'''

#Examples - calculaute the sum of first N natural numbers using a while and for loop 

n=10
sum=0
count=1

while count<=n:
  sum=sum+count
  count=count+1
print("Sum of first 10 Natural Numbers, sum", sum) #Sum of first 10 Natural Numbers, sum 55

n=10
sum=0

for i in range(11):
  sum=sum+1
print(sum)

#prime Numbers between 1 and 100

for num in range(1,101):
  if num>1:
    for i in range(2,num):
      if num%i==0:
        break
      else:
        print(num)