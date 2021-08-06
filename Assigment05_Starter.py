# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# <Morgan Farmer>,<August 6th,2021>,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {'Task': 'Dishes', 'Priority': 'Pay Rent'}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = ['Tasks, Priority']   #A list that acts as a 'table' of rows
strMenu = "Menu of Choices"   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
objFile = open('ToDoList.txt','w')

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
        objFile = open('ToDoList.txt', 'r')
        print('Previewing Current Items...')
        dicRow = {'Task': 'Dishes', 'Priority': 'Pay Rent'}
        print(dicRow)
        objFile.close()
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        objFile = open('ToDoList.txt', 'w')
        dicRow = {'Task': 'Dishes', 'Priority': 'Pay Rent'}
        objFile.write(dicRow['Task'] + ',' + dicRow['Priority'] + '\n')
        lstRow = ['Task','Priority']
        print('Enter new task or priority', '\n')
        objFile.write(input())
        print('New data saved!')
        objFile.close()
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        strFile = 'ToDoList.txt'
        objFile = open(strFile, 'w')
        lstRow = ['Dishes','Pay rent']
        del lstRow[1]
        objFile.close()
        print('Items Removed')
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        strFile = 'ToDoList.txt'
        objFile = open(strFile, 'w')
        lstRow = ['Dishes']
        objFile.write(lstRow[0])
        objFile.close()
        print('Tasks Saved')
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        print('Program has ended!')
        break  # and Exit the program
