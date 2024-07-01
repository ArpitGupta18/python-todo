def read_tasks(filename):
    try:
        with open(filename, 'r') as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []
    
