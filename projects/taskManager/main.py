import os  # To clear console

def takeStringInput(message):  # handles string input so user don't enter empty string
    while True:               # runs until valid/non-empty string provided
        inp1 = input(message)
        if inp1 : return inp1
        else : print('\tempty input !!')
        
        input()
        os.system('clear')

def takeIntInput(message, st, ed):  # handles Integer input so user don't enter any string or invalid input st and ed defines range of int st as start ans ed as end
    while True:               # runs until valid int is provided
        inp1 = input(message)
        try:
            inp1 = int(inp1)  # checks if input is a valid int
        except :
            print('\tInvalid Input')

        else : 
            if st <= inp1 <= ed : return inp1 # if input lies in range
            print('\tInvalid Input')
        
        input()
        os.system('clear')


class Task:  # class task to built or create task
    def __init__(self, title, description, completed = False):  # constructor initalizing title, description, completed(status)
        self.title = title             # string.title()
        self.description = description # string
        self.completed = completed   # bool
    
    def display(self):    # display info of our task
        print(f'Title: {self.title}, Description: {self.description}, Completed: {self.completed}\n\n')



# no need to create instance of the class TaskManager
class Taskmanager:  # class task manager manages all tasks and operations on the tasks(delete, add, view, update etc)
    record = {}     # record or task list which will contain all tasks
    
    @classmethod
    def add_task(cls):  # to add a task(new task specifically) to our record
        title = takeStringInput('ENTER TASK TITLE: ') # takes titile for the task
        if title.title() in cls.record:
            print('task already exists')  # if task is already present control goes to main menu
            input()
            os.system('clear')  # to clear console
            return None # if task already exists end the function
        
        description = takeStringInput('ENTER TASK DESCRIPTION: ') # description of the task
        completed =   bool(input('Enter anything to set status of task to completed else press enter: ')) # status of the task as bool if string entered is empty status of completion is false otherwise true
        
        obj = Task(title.title(), description, completed) # creates object/task of clas Task 
        cls.record[title.title()] = obj  # add that object to out record list

    @classmethod  
    def view_tasks(cls):  # to view all tasks present in our record
        for task in cls.record.values() : # task will be equal to object of class Task
            task.display()  # uses display method of class Task to display task details
        
        input()
        os.system('clear')

    @classmethod
    def find_record(cls, title) : #takes title as parameter and returs wheather that task already present in the record or not
        
        if not cls.record.get(title.title()) : 
            print('TASK NOT FOUND !!')
            return False
        
        return True
    
    @classmethod
    def mark_completed(cls):   # to update status of a task if completed or not
        title = takeStringInput("ENTER TITLE OF TASK YOU WANT TO MARK: ")

        if cls.find_record(title):  # if task found proceed to updation
          cls.record[title.title()].completed =  bool(input('Enter anything to set status of task to completed else press enter: '))
          print("Task status sucessfully updated")         

        input()
        os.system('clear')
    
    @classmethod
    def delete_task(cls): # deletes a task from the record 
       title = takeStringInput("ENTER TITLE OF TASK YOU WANT TO DELETE: ")

       if cls.find_record(title):  # if task found proceed for deletion
          cls.record.pop(title.title())
          print("Task status sucessfully updated")         

       input()
       os.system('clear')


choice = 1
while choice :
    ##print("\n0. To Exit\t\t1. Add Task\n2. View Tasks\n3. Edit Status\t\t4. Delete Task\n\n\n")
    choice = takeIntInput("\n0. To Exit\t\t1. Add Task\n\n\t   2. View Tasks\n\n3. Edit Status\t\t4. Delete Task\n\n\nENTER YOUR CHOICE: ", 0, 4) # Takes user input to perform suitable operation of Taskmanager
    
    os.system('clear')
    if choice == 1 :
        Taskmanager.add_task() 

    if choice == 2 :
        Taskmanager.view_tasks()
    
    if choice == 3 :
        Taskmanager.mark_completed()
    
    if choice == 4 :
        Taskmanager.delete_task()

    

