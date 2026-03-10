##if else statment


#if means aagar ye sahi hai condition ke hisab se toh print kar de bhai

#else means aagar if consition sahi nai hai else print kar de bhai


#elif means allow to check multiple statments


'''age=20

if age>18:
  print("you are allowed to vote")
else:
  print("you are not allowed to vote")'''

#another example
age=15

if age<13:
  print("you are a child")
elif age<18:
  print("you are a teenager")
else:
  print("you are an adult")

#Nested Conditional statment -> if,elif,else -> one or more

print("Nested Conditional statment")

##number even , odd , negative


num=int(input("Enter the number: "))

if num>=0:
  print("The number is positive")
  if num%2==0:
    print("The number is even")
  else:
    print("The number is odd")
else:
  print("The number is zero or negative")
  
#managing indendation part is most important

##Practical Examples

#Determine if a year is a leap year using nested Conditional statment

year=int(input("Enter the year: "))

if year%4==0:
  if year%100==0:
    if year%400==0:
      print(year,"is a leap year")
    else:
      print(year,"its not a leap year")
  else:
    print(year,"is a leap year")
else:
  print(year,"is not a leap year")


##Assignnment
# 01 - Simple calculator program 
''' 02 - Determine the ticket price based on age and wheather the person is a student. 
      Ticket pricing based on age and student status
  Take user inputs'''

