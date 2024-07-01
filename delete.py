def delete_task(tasks, task_number):
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task}' deleted successfully.")
    elif task_number == 0:
        pass
    else:
        print("Invalid task Number!")