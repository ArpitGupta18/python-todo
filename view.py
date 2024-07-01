def view_tasks(tasks):
    if len(tasks) == 0:
        print("There are no tasks to display")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")