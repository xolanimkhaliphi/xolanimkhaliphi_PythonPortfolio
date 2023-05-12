
# =====importing libraries===========
'''This is the section where you will import libraries'''


# ====Login Section====
def login():
    # open and read from user.txt file
    with open("user.txt", "r") as user_file:
        users = []  # create empty list to store the usernames and passwords
        # Initialize username and password to empty strings
        username = ""
        password = ""

        for line in user_file:  # iterate over each line in the file
            # Strip() method used to remove whitespaces from the line in the text file
            # Split the line by the "," character to separate the username and password
            values = line.strip().split(", ")
            if len(values) == 2:  # Checks if there are two values in the text file
                username, password = values

            # Store the username and password in the list
            users.append({'username': username, 'password': password})

    # Keep asking user for their login details until they provide a valid username and password
    while True:
        # Request username and password
        username = input("Please Enter your Username:\n")
        password = input("Please Enter your Password: \n")

        # Validate password and username if they are correct
        found = False  # flag to track if user is found
        for user in users:
            if user['username'] == username and user['password'] == password:
                print(f"Welcome, {username}!")  # If user details are correct, break the loop and welcome user
                found = True
                break

        if found:
            return username  # Return the username of the logged-in user
        # Else if the details are incorrect, request the details again
        else:
            print("Invalid user password or username, please try again.")


# Keep presenting the menu to the user until they choose to exit
logged_in = False  # at first the user has not logged in after log in change this into true
while True:
    # Get the logged-in user's username
    if not logged_in:
        username = login()  # Call the log in function to allow user to log in
    logged_in = True
    # presenting the menu to the user and
    # making sure that the user input is converted to lower case.
    if username == 'admin':  # Admin will be presented with this menu
        menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    s - Display statistics
    e - Exit
    : ''').lower()

    else:
        menu = input('''Select one of the following Options below:
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

    # to register a user only admin has the permission to register a user
    if menu == 'r' and username == 'admin':
        # Requesting user to input new username, new password and confirmation password
        username = input("Please Enter a new username:\n")
        password = input("Please Enter a new Password:\n")
        confirm_password = input("Please Enter your confirmation Password:\n")

        # Checking if password is the same as confirm_password
        # if they are the same add the user and new password to the file
        if password == confirm_password:
            with open("user.txt", "a") as user_file:  # open fie and use append to add to file
                user_file.write(f'{username}, {password}\n')  # .write() to write the new passwords into the file
                print("You Have been added successfully!")
        # if passwords do not match print the following message
        else:
            print("The passwords you have entered do not match , Please try again.")

    # to add a task
    if menu == 'a':
        # Requesting user to input following
        print("Please Enter the Following details:\n")
        user_name = input("A username of the person whom the task is assigned to:\n")
        task_title = input("A Title of the task:\n")
        description = input("A description of the task:\n")
        due_date = input("the due date of the task (YYYY-MM-DD):\n")
        while True:
            task_completion = input("Is the task Completed? (Yes or No): ")
            if task_completion not in ["Yes", "No"]:
                print("Invalid input. Please enter either 'Yes' or 'No'.")
            else:
                break

        # Get current date using import datetime
        import datetime

        current_date = datetime.datetime.now().strftime("%Y-%m-%d")

        # Open task.txt and add the data to the file
        with open("tasks.txt", "a") as task_file:
            task_file.write(
                f'{user_name}, {task_title}, {description}, {due_date}, {task_completion}, {current_date}\n')

    # view all tasks
    elif menu == 'va':
        # Remember for loops are most useful for iterating over a sequence( such as a list or a string)
        with open("tasks.txt", "r") as task_file:  # Open the task.txt file in read mode
            lines = task_file.readlines()  # Read all lines from the file
            # print(task_file)
            # print(lines)
            for line in lines:  # iterate through each line in the file
                parts = line.split(", ")  # Split the line on comma and space
                # Print in the same formant as in the pdf Remember now each item before/after a comma is parts, we
                # must index to find the right point position for the right content
                print(f'Task:               {parts[1]}\n')
                print(f'Assigned to:        {parts[0]}\n')
                print(f'Date assigned:      {parts[3]}\n')
                print(f'Due Date:           {parts[4]}\n')
                print(f'Task Completed?     {parts[5]}\n')
                print(f'Task description:\n   {parts[2]}\n')

    # to view the tasks that are assigned to them
    elif menu == 'vm':
        username = input("Please Enter Username:")  # Request username from user
        found = False  # Keep track of whether the username was found
        with open("tasks.txt", "r") as task_file:  # Open the task.txt file in read mode
            for line in task_file:  # iterate through each line in the file
                parts = line.split(", ")  # Split the line on comma and space
                if parts[0] == username:  # Check if the username matches the first element in the line
                    found = True  # The username was found
                    # Print the task details
                    print(f'Task:               {parts[1]}\n')
                    print(f'Assigned to:        {parts[0]}\n')
                    print(f'Date assigned:      {parts[3]}\n')
                    print(f'Due Date:           {parts[4]}\n')
                    print(f'Task Completed?     {parts[5]}\n')
                    print(f'Task description:\n   {parts[2]}\n')
        if not found:  # If the username was not found, print an error message
            print(f"Error: No tasks found for user '{username}'")

    elif menu == 's':  # Display statistics
        # Count the number of tasks by reading the tasks.txt file and counting the number of lines
        task_count = 0
        with open('tasks.txt', 'r') as task_file:
            for line in task_file:  # Read txt file line by line
                task_count += 1  # increases by 1 for each line and returns the total number of lines in the file

        # Count the number of users by reading the user.txt file and counting the number of lines
        user_count = 0
        with open('user.txt', 'r') as user_file:
            for line in user_file:
                user_count += 1
        # Print the total number of tasks and users in a user-friendly manner
        print(f'Total number of tasks: {task_count}')
        print(f'Total number of users: {user_count}')

    elif menu == 'e':  # Exit
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
