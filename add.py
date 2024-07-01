def add_task(tasks, task):
    tasks.append(task)
    print(f"{'-'*50}")
    print(f"Task '{task}' added successfully.")


def save_task(tasks, filename):
    with open(filename, 'w') as file:
        [file.write(task + '\n') for task in tasks]