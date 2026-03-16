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
  
  
