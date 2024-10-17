import json


def load_tasks(filename="/tasks.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_tasks(tasks, filename="/tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks, task):
    tasks.append({"task": task, "completed": False})


def list_tasks(tasks):
    for idx, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else "✗"
        print(f"{idx}. {task['task']} [{status}]")


def complete_task(tasks, task_number):
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True


if __name__ == "__main__":
    tasks = load_tasks()
    while True:
        action = input("Choose: (a)dd, (l)ist, (c)omplete, (q)uit: ").lower()
        if action == "a":
            task = input("Enter a task: ")
            add_task(tasks, task)
        elif action == "l":
            list_tasks(tasks)
        elif action == "c":
            list_tasks(tasks)
            task_num = int(input("Enter task number to complete: "))
            complete_task(tasks, task_num)
        elif action == "q":
            save_tasks(tasks)
            break
