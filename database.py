def add_task():
    task=input("enter your task ")
    tasks.append(task)
    print(f"{task} task added successfully")
    

def delete_task():
    view_task()
    print("delete task via name ")
    task=input("enter a task to delete ")
    tasks.remove(task)
    print(f"{task} removed successfully")
    
    

def update_task():
    view_task()
    print("update task via index number")
    task=int(input("enter index number to update task "))
    update_task=input("enter task to be updated ")
    tasks[task]=update_task
    print("task updated successfully")

def view_task():
    for i,j in enumerate(tasks):
        print(i,j)
    



tasks=[]
while(True):
    print("Welcome to Task manager")
    print("1.Add task")
    print("2.delete task")
    print("3.update task")
    print("4.view task")
    print("5.Exit")
    choice=int(input("Enter your choice "))
    if choice==1:
        add_task()
    elif choice==2:
        delete_task()
    elif choice==3:
        update_task()
    elif choice==4:
        view_task()
    elif choice==5:
        print("You exited from the task manager")
        break
