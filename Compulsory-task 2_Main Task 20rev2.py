# This program allows users whose names and passwords have been saved in the users txt files to:
# add task, view all task and view tasks of the logged-in individuals with the exception of the admin,
# who is allowed to register new users and read the tasks and users stat

print("\n WELCOME TO THE TASK MANAGER PAGE: \n")

usernames = " "    # usernames are stored in here
passwords = " "    # passwords are stored in here
Login = False      # this boolean is meant to counter the true state of the login state
file = open("user.txt","r")
lines = file.read()    # file.read assist in ensuring lines are read in their state in the file

print("\n TO LOG_IN PLEASE ENTER USERNAME AND PASSWORD")
# the initial state of the login is false and the user credentials will be requested
# login_details formated to resemble how they are read in the file 
while Login == False:       
    user_name = input(" Please enter user name: ")
    password = input(" Please enter password: ")
    login_details = user_name+", "+password
    print(login_details)
# if the login_details are not in the right combination in the file line, an error message is returned
    if login_details not in lines:
        print("Incorrect login_details, please enter a correct details")
        Login = False
# when the desired counter state of the login is attained the code runs       
    else:
        print(f"Welcome {user_name}!") 
        Login = True
        
while Login == True:         
# when admin user is logged in an additional option of  st is added and can only be viewed by the admin  
    if user_name =="admin":
        
        choice = input("Select, r, a, va, vm, st or e: ")
    else:
# when any other user is logged-in an option of st is not provided        
        print("SUCCESFULLY LOGGED-IN: \n: Please select one of the following options: \n: r-register user: \n: a-add task: \n: va-view all task: \n: vm = view my task: \n: e-exit")
        choice = input("Select, r, a, va, vm, or e: ")
        
# this option only allows the admin to register new users        
    if choice == "r":
        if user_name == "admin":
            confirmation = False
            while confirmation == False:
                new_user = input("Please enter new user_name: \n")
                password = input("Please enter new user password: \n")
                password_confirmantion = input("Please confirm your user password: \n")
            
                if password != password_confirmantion:
                    print("Password dont match, please try again")
                    confirmation = False
 # only when the username and passwords are confirmed can the user write the text file            
                else:   
                    print("Username and password confirmed")
                    file = open("user.txt","a")
                    file.write(f"\n{new_user}, {password}")
                    confirmation = True
                    file.close()
        else:
            print("You dont have rights to register new user")
    
    if choice == "a":
        excecutor_user_name = input("Enter the user_name of the person this task is assigned to: \n")
        task_title = input("Enter the task title: \n")
        task_description = input("Enter the task description: \n")
        task_due_date = input("Enter the task due_date: \n")
        task_creation_date = input("Enter the task creation date: \n")
        task_completion_status ="No"        
        file = open("tasks.txt","a")
        file.write(f"\n{excecutor_user_name},{task_title},{task_description},{task_creation_date},{task_due_date},{task_completion_status}")
    file.close()
    
    if choice == "va":
        file = open("tasks.txt","r")
        lines = file.readlines()
        for line in lines:
            view_task = line.strip().split(",")  
            print("Task        :"+view_task[1])
            print("Assigned to :"+view_task[0])
            print("Date assigned:"+view_task[3])
            print("Due date     :"+view_task[4])
            print("Task complete?:"+view_task[5])
            print("Task description:"+view_task[2])
            
    if choice == "vm":
        file = open("tasks.txt","r")
        lines = file.readlines()
        for line in lines:
            view_task = line.strip().split(",")
            if user_name == view_task[0]:
                print("Task        :"+view_task[1])
                print("Assigned to :"+view_task[0])
                print("Date assigned:"+view_task[3])
                print("Due date     :"+view_task[4])
                print("Task complete?:"+view_task[5])
                print("Task description:"+view_task[2])
                
    if choice == "st":
        user_name == "admin"
        user_num = 0
        task_num = 0
        
# determination of number of the users
        file =open("user.txt","r")
        lines = file.readlines()
        for line in lines:
            user_num+=1
        
# determination of the number of task
        file = open("tasks.txt","r")
        lines = file.readlines()
        for line in lines:
            task_num+=1
        
        print("Users and Task Statistics:\n"+"Number of task = " +str(task_num)+"\n"+"Number of users = "+str(user_num))
              
    if choice == "e":
        exit()
           
    
        
