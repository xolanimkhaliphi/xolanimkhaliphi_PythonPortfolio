"""Capstone template project for FCS Task 19 Compulsory task 1.
This template provides a skeleton code to start compulsory task 1 only.
Once you have successfully implemented compulsory task 1 it will be easier to
add a code for compulsory task 2 to complete this capstone"""

# =====importing libraries===========
'''This is the section where you will import libraries'''
import os


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


# Function to register a new user
def reg_user():
    # Requesting user to input new username, new password and confirmation password
    username = input("Please Enter a new username:\n")
    password = input("Please Enter a new Password:\n")
    confirm_password = input("Please Enter your confirmation Password:\n")

    # Checking if the username already exists in user.txt
    with open("user.txt", "r") as user_file:
        for line in user_file:
            if username in line:
                print("This username already exists, please try another username.")
                return

    # Checking if password is the same as confirm_password
    # if they are the same add the user and new password to the file
    if password == confirm_password:
        with open("user.txt", "a") as user_file:  # open fie and use append to add to file
            user_file.write(f'{username}, {password}\n')  # .write() to write the new passwords into the file
            print("You have been added successfully!")
    # if passwords do not match print the following message
    else:
        print("The passwords you have entered do not match, please try again.")


# Functions to add tasks
def add_task():
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


# Function to view all tasks
def view_all():
    # Remember for loops are most useful for iterating over a sequence( such as a list or a string)
    with open("tasks.txt", "r") as task_file:  # Open the task.txt file in read mode
        lines = task_file.readlines()  # Read all lines from the file
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


# A Function for users to view  tasks that have been assigned to them
def view_mine():
    username = input("Please Enter Username:")  # Request username from user
    found = False  # Keep track of whether the username was found
    tasks = []
    with open("tasks.txt", "r") as task_file:  # Open the task.txt file in read mode
        for i, line in enumerate(task_file):  # iterate through each line in the file
            parts = line.split(", ")  # Split the line on comma and space
            if parts[0] == username:  # Check if the username matches the first element in the line
                found = True  # The username was found
                tasks.append(parts)
        if not found:  # If the Username was not found, print an error message
            print(f"Error: No tasks found for user '{username}'")
        else:
            for i, task in enumerate(tasks):
                print(f"Task {i + 1}:")
                print(f'Task:               {task[1]}\n')
                print(f'Assigned to:        {task[0]}\n')
                print(f'Date assigned:      {task[3]}\n')
                print(f'Due Date:           {task[4]}\n')
                print(f'Task Completed?     {task[5]}\n')
                print(f'Task description:\n   {task[2]}\n')

                # Allow user to select a task or return to main menu
                task_num = int(input("Enter the task number to edit or -1 to return to main menu:"))
                if task_num == -1:
                    break
                task_to_edit = tasks[task_num - 1]
                # Allow user to edit/mark task as complete
                edit_choice = input("Enter 'e' to edit task or 'c' to mark as complete:")
                if edit_choice == 'e':
                    if task_to_edit[5] == 'Yes':
                        print("Error: Task already completed, cannot edit.")
                    else:
                        edit_field = input("Enter 'u' to edit username or 'd' to edit due date:")
                        if edit_field == 'u':
                            new_username = input("Enter new username:")
                            task_to_edit[0] = new_username
                        elif edit_field == 'd':
                            new_due_date = input("Enter new due date:")
                            task_to_edit[4] = new_due_date
                        with open("tasks.txt", "w") as task_file:
                            for t in tasks:
                                task_file.write(", ".join(t) + "\n")
                elif edit_choice == 'c':
                    task_to_edit[5] = "Yes"
                    with open("tasks.txt", "w") as task_file:
                        for t in tasks:
                            task_file.write(", ".join(t) + "\n")


# A Function to display statistics
def display_stats():
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
    # Check if task_overview.txt and user_overview.txt exist, if not, generate them
    if not os.path.exists("task_overview.txt") or not os.path.exists("user_overview.txt"):
        generate_reports()
    # os.path.exists is a method in the os.path module in Python. It returns True if the specified file path exists,
    # and False otherwise
    # Read task_overview.txt and display its contents on the screen
    with open("task_overview.txt", "r") as task_overview:
        print(task_overview.read())

    # Read user_overview.txt and display its contents on the screen
    with open("user_overview.txt", "r") as user_overview:
        print(user_overview.read())


# A function to generate reports

def generate_reports():
    task_count = 0
    completed_tasks = 0
    uncompleted_tasks = 0
    overdue_tasks = 0

    # Open tasks.txt file to read and count the number of tasks
    with open("tasks.txt", "r") as task_file:
        for line in task_file:
            task_count += 1
            task = line.strip().split(", ")
            if len(task) == 5:
                due_date = task[3]
                task_completion = task[4]

                # Get the current date using datetime module
                import datetime
                current_date = datetime.datetime.now().strftime("%Y-%m-%d")

                # Count the number of completed and uncompleted tasks
                if task_completion == "Yes":
                    completed_tasks += 1
                else:
                    uncompleted_tasks += 1
                    # Check if the task is overdue
                    if current_date > due_date:
                        overdue_tasks += 1

    # Calculate the percentage of uncompleted and overdue tasks
    if task_count == 0:
        uncompleted_percentage = 0
        overdue_percentage = 0
    else:
        uncompleted_percentage = uncompleted_tasks / task_count * 100
        overdue_percentage = overdue_tasks / task_count * 100

    # Generate task_overview.txt file
    with open("task_overview.txt", "w") as task_overview:
        task_overview.write("Task Overview:\n")
        task_overview.write(f'Total number of tasks: {task_count}\n')
        task_overview.write(f'Total number of completed tasks: {completed_tasks}\n')
        task_overview.write(f'Total number of uncompleted tasks: {uncompleted_tasks}\n')
        task_overview.write(f'Total number of tasks that are overdue: {overdue_tasks}\n')
        task_overview.write(f'Percentage of tasks that are incomplete: {uncompleted_percentage:.2f}%\n')
        task_overview.write(f'Percentage of tasks that are overdue: {overdue_percentage:.2f}%\n')

    # Generate the users dictionary
    with open("tasks.txt", "r") as task_file:
        users = {}
        for line in task_file:
            task = line.strip().split(", ")
            if len(task) == 5:
                user_name = task[0]
                task_completion = task[4]

                # Initialize the dictionary for a new user
                if user_name not in users:
                    users[user_name] = {"total_tasks": 0, "completed_tasks": 0}

                # Count the total number of tasks and completed tasks for each user
                users[user_name]["total_tasks"] += 1
                if task_completion == "Yes":
                    users[user_name]["completed_tasks"] += 1

    # Write the user overview to user_overview.txt
    with open("user_overview.txt", "w") as user_overview:
        user_overview.write("User Overview:\n")
        for user_name, data in users.items():
            total_tasks = data["total_tasks"]
            completed_tasks = data["completed_tasks"]

            # Calculate the percentage of completed tasks for each user
            if total_tasks == 0:
                completed_percentage = 0
            else:
                completed_percentage = completed_tasks / total_tasks * 100

            # Write the username, total tasks, completed tasks, and completed percentage to user_overview.txt
            user_overview.write(f"{user_name}:\n")
            user_overview.write(f"\tTotal tasks: {total_tasks}\n")
            user_overview.write(f"\tCompleted tasks: {completed_tasks}\n")
            user_overview.write(f"\tPercentage of completed tasks: {completed_percentage:.2f}%\n")


def main_menu():
    # Keep presenting the menu to the user until they choose to exit
    logged_in = False
    while True:
        if not logged_in:
            username = login()
            logged_in = True

        # presenting the menu to the user and
        # making sure that the user input is converted to lower case.
        if username == 'admin':  # Admin will be presented with this menu
            menu = input('''Select one of the following Options below:
        r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - view my task
        ds - Display statistics
        gr - generate reports
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
            reg_user()
        # to add a task
        if menu == 'a':
            add_task()
        # view all tasks
        elif menu == 'va':
            view_all()
        # to view the tasks that are assigned to them
        elif menu == 'vm':
            view_mine()
        # Display statistics
        elif menu == 'ds':  # Display statistics
            display_stats()
        # Generate reports
        elif menu == 'gr':
            generate_reports()
        # Exit menu
        elif menu == 'e':  # Exit
            print('Goodbye!!!')
            exit()

        else:
            print("You have made a wrong choice, Please Try again")


main_menu()
