import add
import read
import delete
import view

filename = "todo_task.txt"
tasks = read.read_tasks(filename)

while True:
    print("--------List of activities you can perform--------")
    print("1. Add task")
    print("2. Delete task")
    print("3. View task")
    print("4. Exit")

    print(f"{'-'*50}")

    choice = input("Enter your choice (1-4): ")

    print(f"{'-'*50}")

    if choice == '1':
        view.view_tasks(tasks)
        print(f"{'-'*50}")
        task = input("Enter the task you want to add: ")
        add.add_task(tasks, task)
        add.save_task(tasks, filename)

    elif choice == '2':
        while True:
            view.view_tasks(tasks)
            print(f"{'-'*50}")
            try:
                task_number = int(input("Enter the task number to delete(0 to delete none): "))
                print(f"{'-'*50}")
                if task_number == 0:
                    print("No task deleted")
                delete.delete_task(tasks, task_number)
                add.save_task(tasks, filename)
                break
            except ValueError:
                print("Please enter a valid Number")
                print(f"{'-'*50}")

    elif choice == '3':
       print("\n------------------List of tasks-------------------")
       view.view_tasks(tasks)
    
    elif choice == '4':
        print("Exiting")
        add.save_task(tasks, filename)
        print(f"{'='*50}")
        print("--------------Thank you for visiting--------------\n\n")
        break
    
    else:
        print("Invalid Choice!! Enter again")
        
    print(f"{'='*50}\n\n")
