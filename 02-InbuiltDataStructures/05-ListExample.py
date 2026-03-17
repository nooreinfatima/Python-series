to_do_list=["Buy Groceries"," Clean the House", "Pay Bills"]

## Adding to task
to_do_list.append("Schedule meeting")
to_do_list.append("Go for a Run")

##removing
to_do_list.remove(" Clean the House")
print(to_do_list)

## checking if a task is in the list

if "Pay Bills" in to_do_list:
  print("Don't forget to pay the utility bills")

print("To Do List Remaining")

for task in to_do_list:
  print(f"-{task}")
  
  
## Example 2

grades=[85,92,78,90,88]

## Adding a new grades
grades.append(95)
print(grades)

#Calculating the average grades
average_grade = sum(grades) / len(grades)
print(f"Average Grade: {average_grade:.2f}")

# Finding the highest and lowest grades

highest_grade = max(grades)
lowest_grade = min(grades)

print(f"Highest Grade: {highest_grade}")
print(f"Lowest Grade: {lowest_grade}")