def task():
    tasks=[]
    
    "\n"
    print("----------welcome to the management app----------")
    
    
    total_task=int(input("enter your tasks you want to add="))
    for i in range(1,total_task+1):
        task_name=input(f"enter task number {i} =")
        tasks.append(task_name)
    print(f"todays tasks are \n{tasks}")
    while True:
        operation=int(input("enter 1-add\n2-update\n3-delete\n4-view\n5-exit/stop/="))
        if operation==1:
            add=input("add your task=")
            tasks.append(add)
            print(f"task {add} has sucessfully added into your list")
        elif operation==2:
            update=input("enter task which you want to update=")
            if update in tasks:
                up=input("this task already exist please enter new task ")
                ind=tasks.index(update)
                tasks[ind]=up
                print(f"updated task {up}")
            else:
                print(f"updated task is {update}")
        elif operation==3:
            del_val=input("enter your task which you want to delete or remove")
            if del_val in tasks:
                ind=tasks.index(del_val)
                del tasks[ind]
                print(f"your {del_val} has been deleted")
        elif operation==4:
            print(f"your tasks are {tasks}")
        elif operation==5:
            print("closing the program.........")
            break
        else:
            print("invalid input")



task()