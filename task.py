my_tasks = []
check = 'y'

#Taking input
while check!='n':
    task = input("Enter the task ")
    my_tasks.append(task)
    check = input("Press y to enter tasks or n to stop ")

#Print before modification
for i,task in enumerate(my_tasks):
    print(i,task)

#Modifying and Printing
modify = input("Press y to modify any task or n to keep the previous tasks: ")
if modify == 'y':
    test = int(input("Enter the task number to modify "))
    new_task = input("Enter the new task " )
    my_tasks[test] = new_task
    for i, task in enumerate(my_tasks):
        print(i, task)