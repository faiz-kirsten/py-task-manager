# =====importing libraries===========
from datetime import date
import datetime


def reg_user():
    # ====Registering users section====
    # The if statement below checks if the item with the index value of 0 in 'user_split'
    # is 'admin'.
    # If it is admin the user is prompted to register a new user
    # and this is written to 'users.txt'.
    # If the user logged in is not an admin
    # the program displays the content in the else statement.
    if user_split[0] == 'admin':
        list_users_split = []

        for i in list_users:
            list_users_split.append(i.split(" ")[0])
        new_username = input("Enter a new username: ").lower()
        # The while loop below checks whether the username entered by the user is in 'list_users_split'
        # If it is, the user is continuously requested to enter a username that does not exist
        while new_username in list_users_split:
            new_username = input("Username already exists. Enter a new username: ").lower()

        new_password = input("Enter a new password: ")
        password_confirmation = input("Confirm password: ")
        while new_password != password_confirmation:
            new_password = input("Passwords dont match. Enter a new password: ")
            password_confirmation = input("Confirm new password: ")

        with open('user.txt', 'a') as f:
            f.write("\n")
            f.write(f"{new_username}, {new_password}")
        print("New user successfully registered!")
    else:
        print(f"Only admins can register new users.")


def add_task():
    # ====Adding a task section====
    # The user is prompted with the questions below which are stored in
    # variables which are stored in 'task_info' which is written to 'tasks.txt'.
    user_task_assigned = input("Who is the task assigned to: ").lower()
    task_title = input("What is title of the task: ")
    task_description = input("Enter the tasks description: ")

    # The user is requested to enter the task due date in a specific format which is split by '-'.
    # The 'task_due_date' is formatted into a date using the 'datetime' library.
    task_due_date = input("Enter the task due date in this format YYYY-MM-DD: ").split("-")
    x = datetime.date(int(task_due_date[0]), int(task_due_date[1]), int(task_due_date[2]))
    # The strftime method is used to convert the datetime to a string.
    # It is also used to format the date according to the way we want to display it
    task_due_date = x.strftime("%d %b %Y")
    # 'today' returns the current date using the 'date' class in the 'datetime' module
    today = date.today()
    task_date_assigned = today.strftime("%d %b %Y")

    task_completed = 'No'

    task_info = f"{user_task_assigned}, {task_title}, {task_description}, {task_date_assigned}, " \
                f"{task_due_date}, {task_completed}"

    with open('tasks.txt', 'a') as f:
        f.write("\n")
        f.write(task_info)
    print("New task successfully added!")


def view_all():
    # ====View all tasks section====
    # The with statement below reads from 'tasks.txt'
    # It removes '\n' from the end of each line and the contents in each
    # line are split wherever there is a comma followed by a space which is
    # added into 'list_tasks' using the append function
    # which creates a nested list('list_tasks').
    list_tasks = []

    with open('tasks.txt', 'r') as f:
        for line in f:
            list_tasks.append(line.strip("\n").split(", "))

    # The for loop below iterates through each item in 'list_tasks'.
    # List indexing is used to acquire the necessary information, and it
    # does this for each item in 'list_tasks' and displays the information
    # in a neat format
    for task in list_tasks:
        print(f"Task: \t\t{task[1]}\nAssigned to: \t{task[0]}\nDate assigned: \t{task[3]}\nDue date: \t{task[4]}"
              f"\nTask Complete?\t{task[5]}\nTask description: \n{task[2]}\n")


def view_mine():
    # # ====View logged in users tasks section====
    # The with statement below reads from 'tasks.txt'
    # It removes '\n' from the end of each line and the contents in each
    # line are split wherever there is a comma followed by a space which is
    # added into 'list_tasks' using the append function
    # which creates a nested list('list_tasks').

    list_tasks = []

    with open('tasks.txt', 'r') as f:
        for line in f:
            list_tasks.append(line.strip("\n").split(", "))
    # The for loop below iterates through each item in 'list_tasks'.
    # The if statement inside the for loop checks whether the users
    # name is the same as the user in the 'tasks.txt'.
    # List indexing is used to acquire the necessary information, and it
    # does this for each item in 'list_tasks' and displays the information
    # in a neat format.
    # 'counter' is defined and incremented by 1 within the if statement to count the amount of
    # tasks assigned to the user.
    # Each 'task' number which is 'counter' is added to 'dict_task_num' as the key and the corresponding
    # 'task' as a value for each key.
    counter = 0
    dict_task_num = {}

    for task in list_tasks:
        if user_split[0] == task[0]:
            counter += 1
            dict_task_num[counter] = task
            print(f"Task number:\t{counter}\nTask:\t\t{task[1]}\nAssigned to:\t{task[0]}\n"
                  f"Date assigned:\t{task[3]}\nDue date:\t{task[4]}\nTask Complete?\t{task[5]}\n"
                  f"Task description:\n{task[2]}\n")

    list_users_user = []

    # The for loop below iterates through 'list_users' and appends the item at index value 0 for
    # each iteration to 'list_users_user'
    for i in list_users:
        list_users_user.append(i.split(" ")[0])

    # The if statement below checks whether the length of 'dict_task_num' is 0 and if it is 0,
    # the user is notified that they do not have any tasks.
    if len(dict_task_num) != 0:
        dict_task_num_list = []

        # The for loop below iterates through 'dict_task_num' and appends all keys to 'dict_task_num_list'
        for i in dict_task_num:
            dict_task_num_list.append(i)

        user_select = int(input('Select a specific task by entering a task number'
                                ' or input ‘-1’ to return to the main menu: '))
        # The while loop below continuously requests that the user enters a number if the number
        # they entered is not inside 'dict_task_num_list'
        while user_select not in dict_task_num_list and user_select != -1:
            user_select = int(input('Invalid task number! Select a specific task by entering a task number'
                                    ' or input ‘-1’ to return to the main menu: '))

        if user_select != -1:
            # The if statement below checks whether the task selected is completed or not.
            # If the task selected in 'dict_task_num' with index value -1 is 'No' then the if statement is executed.
            if dict_task_num[user_select][-1] == "No":

                user_select_options1 = int(input("1. Mark the task as complete\n2. Edit the task\n"))
                # The while loop below continuously requests that the user enters a number if the number
                # they entered is not 1 or 2.
                while user_select_options1 != 1 and user_select_options1 != 2:
                    user_select_options1 = int(input("Invalid option! Select one of the options below:\n"
                                                     "1. Mark the task as complete\n2. Edit the task\n"))
                if user_select_options1 == 1:
                    # The for loop below iterates through 'list_tasks' and checks if the specific task selected,
                    # which is 'dict_task_num[user_select]', is equal to 'i'.
                    # If it is equal to 'i', the item with index value -1 in 'dict_task_num[user_select]
                    # is replaced with 'Yes'.
                    for i in list_tasks:
                        if dict_task_num[user_select] == i:
                            dict_task_num[user_select][-1] = "Yes"

                    print("Task marked as complete!")
                else:
                    user_select_options2 = int(input("1. Username\n2. Due Date\n"))
                    # The while loop below continuously requests that the user enters a number if the number
                    # they entered is not 1 or 2.
                    while user_select_options2 != 1 and user_select_options2 != 2:
                        user_select_options2 = int(input("Invalid option! Select one of the options below:\n"
                                                         "1. Username\n2. Due Date\n"))

                    if user_select_options2 == 1:
                        username_change = input("Enter the username: ").lower()
                        # The while statement below continuously requests that the user enter a username
                        # that is stored in 'list_users_user'.
                        while username_change not in list_users_user:
                            username_change = input("Username does not exist. Enter a valid username: ").lower()
                        # The for loop below iterates through 'list_tasks' and checks if the specific task selected,
                        # which is 'dict_task_num[user_select]', is equal to 'i'.
                        # If it is equal to 'i', the item with index value 0 in 'dict_task_num[user_select]
                        # is replaced with 'username_change'.
                        for i in list_tasks:
                            if dict_task_num[user_select] == i:
                                dict_task_num[user_select][0] = username_change

                        print(f"Task assigned to {username_change}!")
                    else:
                        # The 'new_due_date' is formatted into a date using the 'datetime' library.
                        new_due_date = input("Enter a new task due date in this format YYYY-MM-DD: ").split("-")
                        format_date = datetime.date(int(new_due_date[0]), int(new_due_date[1]),
                                                    int(new_due_date[2]))
                        # The strftime method is used to convert the datetime to a string.
                        # It is also used to format the date according to the way we want to display it
                        task_due_date = format_date.strftime("%d %b %Y")

                        # The for loop below iterates through 'list_tasks' and checks if the specific task selected,
                        # which is 'dict_task_num[user_select]', is equal to 'i'.
                        # If it is equal to 'i', the item with index value 4 in 'dict_task_num[user_select]'
                        # is replaced with 'task_due_date'.
                        for i in list_tasks:
                            if dict_task_num[user_select] == i:
                                dict_task_num[user_select][4] = task_due_date

                        print("New due date assigned to task!")
                # The with statements below overwrite 'tasks.txt'
                # The first with statement below writes to 'tasks.txt'
                # The first iteration in 'list_tasks' is written to 'tasks.txt'
                with open('tasks.txt', 'w') as f:
                    f.write(f"{list_tasks[0][0]}, {list_tasks[0][1]}, {list_tasks[0][2]}, "
                            f"{list_tasks[0][3]}, {list_tasks[0][4]}, {list_tasks[0][5]}")
                # The with statement below appends to 'tasks.txt'
                # The iterations starting from index value 1 in 'list_tasks' are appended to 'tasks.txt'
                with open('tasks.txt', 'a') as f:
                    for task in list_tasks[1:]:
                        f.write("\n")
                        f.write(f"{task[0]}, {task[1]}, {task[2]}, {task[3]}, {task[4]}, {task[5]}")
            else:
                print("Task completed! Unable to edit a completed task. ")
    else:
        print("You have not been assigned any tasks!")


def generate_reports():
    # The with statement below reads from 'tasks.txt'
    # 'total_tasks' stores the length of lines in 'tasks.txt' using the len and readlines functions
    with open('tasks.txt', 'r') as f:
        total_tasks = len(f.readlines())

    list_tasks = []

    # The with statement below reads from 'tasks.txt'
    # It removes '\n' from the end of each line and the contents in each
    # line are split wherever there is a comma followed by a space which is
    # added into 'list_tasks' using the append function
    # which creates a nested list('list_tasks').
    with open('tasks.txt', 'r') as f:
        for line in f:
            list_tasks.append(line.strip("\n").split(", "))

    # 'month_dict' is defined which stores the months names as keys and corresponding numbers as values
    month_dict = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9,
                  'Oct': 10, 'Nov': 11, 'Dec': 12}
    current_date = date.today()

    # User Overview
    list_users_split = []

    # The for loop below iterates through 'list_users' and appends the item at index value 0 for
    # each iteration to 'list_users_user'
    for i in list_users:
        list_users_split.append(i.split(" ")[0])

    dict_users = {}
    dict_tasks = {}
    dict_tasks_overdue = {}

    # The for loop below iterates through 'list_users_split' and appends each iteration as keys to 'dict_users',
    # 'dict_tasks' and 'dict_tasks_overdue' and an empty list is assigned as values to each key
    for i in list_users_split:
        dict_users[i] = []
        dict_tasks[i] = []
        dict_tasks_overdue[i] = []

    # The nested for loop below iterates through 'dict_users' and 'list_tasks'.
    # If the iteration with index value 0 in 'list_tasks' is equal to the iteration in 'dict_users',
    # the iteration in 'list_tasks' which is 'task' is appended to each key in 'dict_users' as values.
    for i in dict_users:
        for x in list_tasks:
            if x[0] == i:
                dict_users[i] += [x]

    # The for loop below iterates through 'dict_users' and checks if the length of the value
    # stored in each key is not 0.
    for i in dict_users:
        if len(dict_users[i]) != 0:
            # The for loop below iterates through the values of each key.
            for x in dict_users[i]:
                # The if statement below checks whether the iteration with index value -1 in
                # each value is 'Yes' or 'No'.
                # If it is 'Yes' it appends '1' to the list stored in the value of each key in 'dict_tasks'
                # If it is 'No' it appends '0' to the list stored in the value of each key in 'dict_tasks'
                if x[-1] == "Yes":
                    dict_tasks[i] += [1]
                else:
                    dict_tasks[i] += [0]

                # 'due_date_split1' splits the item at index value -2 in 'x' where there is a space
                due_date_split1 = x[-2].split(" ")

                # 'due_date_split1 is formatted into a date using the datetime module
                due_date_format1 = datetime.date(int(due_date_split1[2]), month_dict[due_date_split1[1]],
                                                 int(due_date_split1[0]))

                # The if statement below checks whether the iteration with index value -1 in
                # each value is a 'No' and if the 'due_date_format1' is before the 'current_date'.
                # If it is it appends '1' to the list stored in the value of each key in 'dict_tasks_overdue'.
                # If it is not it appends '0' to the list stored in the value of each key in 'dict_tasks_overdue'
                if x[-1] == "No" and due_date_format1 < current_date:
                    dict_tasks_overdue[i] += [1]
                else:
                    dict_tasks_overdue[i] += [0]

    # The with statement below creates and writes to 'user_overview.txt'
    with open('user_overview.txt', 'w') as f:
        # The for loop below iterates through 'dict_tasks' and checks whether the value which is a list is empty or not.
        # The sum, len and round functions are used to determine the necessary calculations.
        for i in dict_tasks:
            if len(dict_tasks[i]) != 0:
                f.write(f"{i} - Total assigned tasks: {len(dict_tasks[i])}, "
                        f"Total percent of all tasks: {round((len(dict_tasks[i]) / total_tasks) * 100, 1)}%, "
                        f"Percent complete: {round((sum(dict_tasks[i]) / len(dict_tasks[i])) * 100, 1)}%, "
                        f"Percent incomplete: "
                        f"{100 - (round((sum(dict_tasks[i]) / len(dict_tasks[i])) * 100, 1))}%, "
                        f"Percent incomplete & overdue: "
                        f"{round((sum(dict_tasks_overdue[i]) / len(dict_tasks_overdue[i])) * 100, 1)}%\n")
            else:
                f.write(f"{i} - No tasks assigned to user\n")

    # Tasks Overview
    list_tasks_complete = []
    list_tasks_overdue = []

    # The for loop below iterates through 'dict_tasks' and appends each value in 'dict_tasks'  to
    # 'list_tasks_complete' without appending them as separate items because of the use of the extend function
    for i in dict_tasks:
        list_tasks_complete.extend(dict_tasks[i])

    # The for loop below iterates through 'dict_tasks' and appends each value in 'dict_tasks_overdue'  to
    # 'list_tasks_overdue' without appending them as separate items because of the use of the extend function
    for i in dict_tasks_overdue:
        list_tasks_overdue.extend(dict_tasks_overdue[i])

    percent_incomplete = round(((len(list_tasks_complete) - sum(list_tasks_complete)) / len(list_tasks_complete)) * 100, 1)

    # The with statement below creates and writes to 'task_overview.txt'
    # The sum, len and round functions are used to determine the necessary calculations.
    with open('task_overview.txt', 'w') as f:
        f.write(f"Total number of tasks: {len(list_tasks_complete)}\n"
                f"Total completed tasks: {sum(list_tasks_complete)}\n"
                f"Total incomplete tasks: {len(list_tasks_complete) - sum(list_tasks_complete)}\n"
                f"Total overdue & incomplete tasks: {sum(list_tasks_overdue)}\n"
                f"Percentage of incomplete tasks: {percent_incomplete}%\n"
                f"Percentage of overdue & Incomplete tasks: {round((sum(list_tasks_overdue) / len(list_tasks_overdue)) * 100, 1)}%")

    return "User & Task reports successfully generated!"


def display_statistics():
    # The generate_reports function is called below
    generate_reports()

    # The user is requested to choose one of the options
    task_user_report = int(input("1. View task report\n2. View user report\n"))
    # The while loop below continuously requests that the user enters a number if the number
    # they entered is not 1 or 2.
    while task_user_report != 1 and task_user_report != 2:
        task_user_report = int(input("Invalid option! Select one of the options below:\n"
                                     "1. View task report\n2. View user report\n"))
    # Based on the users choice, the contents stored in 'user_overview.txt' or 'task_overview.txt' are read
    # from and displayed
    if task_user_report == 1:
        with open('task_overview.txt', 'r') as f:
            for line in f:
                print(line.strip("\n"))
    else:
        with open('user_overview.txt', 'r') as f:
            for line in f:
                print(line.strip("\n"))


# ====Login Section====
list_users = []

# The with statement below reads from 'user.txt'
# and the for loop formats and appends each user to 'list_users'.
with open('user.txt', 'r') as f:
    for line in f:
        list_users.append(line.strip('\n').replace(',', ''))

# The user is prompted to input their username and password.
user_name = input("Enter your username: ").lower()
user_password = input("Enter your password: ")
user_name_password = f'{user_name} {user_password}'

# If the 'user_name_password' are not in 'list_users', the user is prompted to enter them again.
while user_name_password not in list_users:
    user_name = input("Incorrect username or password. Enter your username: ").lower()
    user_password = input("Enter your password: ")
    user_name_password = f'{user_name} {user_password}'

# The 'user_name_password' is split by a space and stored in 'user_split'
user_split = user_name_password.split(" ")

menu = 0

while menu != "e":
    # The user is presented with a different 'menu' based on their username
    # and 'menu' is converted to lower case.
    # 'admin' users are presented with a different menu compared other users.
    # If the user entered an option that is not in the 'menu_options'
    # the user is requested to enter a valid option.
    if user_split[0] == "admin":
        menu = input('''Select one of the following Options below:
r - registering a user
a - adding a task
va - view all tasks
vm - view my task
gr - generate reports
ds - display statistics
e - exit
''').lower()
        menu_options = ['r', 'a', 'va', 'vm', 'e', 'ds', 'gr']
        while menu not in menu_options:
            menu = input('''Invalid option. Select one of the following Options below:
r - registering a user
a - adding a task
va - view all tasks
vm - view my task
gr - generate reports
ds - display statistics
e - Exit
''').lower()

    else:
        menu = input('''Select one of the following Options below:
r - registering a user
a - adding a task
va - view all tasks
vm - view my task
e - exit
''').lower()

        menu_options = ['r', 'a', 'va', 'vm', 'e']

        while menu not in menu_options:
            menu = input('''Invalid option. Select one of the following Options below:
r - registering a user
a - adding a task
va - view all tasks
vm - view my task
e - exit
''').lower()

    if menu == 'r':
        reg_user()
    elif menu == 'a':
        add_task()
    elif menu == 'va':
        view_all()
    elif menu == 'vm':
        view_mine()
    elif menu == 'ds':
        display_statistics()
    elif menu == 'gr':
        print(generate_reports())

print('Goodbye!!!')
exit()

# References:
# https://www.geeksforgeeks.org/get-current-date-using-python/
# https://www.geeksforgeeks.org/formatting-dates-in-python/
# https://www.programiz.com/python-programming/datetime/current-datetime
# https://www.geeksforgeeks.org/reading-writing-text-files-python/
# https://stackoverflow.com/questions/466345/convert-string-jun-1-2005-133pm-into-datetime
# https://www.geeksforgeeks.org/comparing-dates-python/
# https://www.geeksforgeeks.org/appending-to-list-in-python-dictionary/#:~:text=Method%201%3A%20Using%20%2B%3D%20sign,a%20list%20into%20the%20dictionary.
# https://www.geeksforgeeks.org/python-increment-value-in-dictionary/
# https://stackoverflow.com/questions/6148619/start-index-for-iterating-python-list
