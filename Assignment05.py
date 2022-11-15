# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Jessica Chen, 11/12/2022, Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = None  # File handle
strFile = 'ToDoList.txt'  # Data storage file
strData = ''  # A row of text data from the file
lstRow = []  # List of data
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ''   # A menu of user options
strChoice = ''  # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open(strFile, 'r')
for row in objFile:
    lstRow = row.split(', ')  # Return a list
    dicRow = {'Task': lstRow[0], 'Priority': lstRow[1].strip()}  # Add list data to dictionary
    lstTable.append(dicRow)  # Create the table
objFile.close()


# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print('''
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    ''')
    strChoice = str(input('Which option would you like to perform? [1 to 5] - '))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print('Your current data is: ')
        for row in lstTable:
            print(row['Task'], row['Priority'], sep=', ')
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        print('Type in a task and its priority.')
        strTask = input('Enter a Task: ')
        strPriority = input('Enter its Priority : ')
        dicRow = {'Task': strTask, 'Priority': strPriority}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        print(lstTable)  # Display the list to user for reference
        strRemove = input('Enter the Task to be removed: ')
        for row in lstTable:
            if row['Task'] == strRemove:
                lstTable.remove(row)
        continue
    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open('ToDoList.txt', 'w')
        for row in lstTable:
            objFile.write(row['Task'] + ', ' + row['Priority'] + '\n')
        objFile.close()
        print('Data saved!')
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print('Bye!')
        break  # and Exit the program
