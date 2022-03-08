import datetime

task1 = (True, "CPSC 4970 Hw", "2022-03-013 23:59")
task2 = (False, "Laundry", "2022-03-06 12:15")
task3 = (True, "Send email to Rick", "2022-03-09 8:00")
todo = [task1, task2, task3]



print("Main menu: ")
print("1) List ALL todo items ")
print("2) List all incomplete todo items ")
print("3) List incomplete todo items due today ")
print("4) Add a todo item ")
print("5) Complete a todo item ")
print("6) Quit ")
selection = input("Enter your choice> ")


if int(selection) == 1: print(todo)

# if int(selection) == 2:

# if int(selection) == 3:

# if int(selection) == 4:

# if int(selection) == 5:

# if int(selection) == 6:
