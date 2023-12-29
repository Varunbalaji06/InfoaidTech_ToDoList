# To-Do List App Using Python
import json
class Task:
    def __init__(self, title, description, status='Incomplete'):
        self.title = title
        self.description = description
        self.status = status

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f'Task "{title}" deleted.')
                return
        print(f'Task "{title}" not found.')

    def view_tasks(self):
        if not self.tasks:
            print('No tasks available.')
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. Title: {task.title}\n   Description: {task.description}\n   Status: {task.status}\n")

    def save_tasks(self, filename='mytasks.json'):
        with open(filename, 'w') as file:
            task_list = [{'title': task.title, 'description': task.description, 'status': task.status} for task in self.tasks]
            json.dump(task_list, file)
        print(f'Tasks saved to {filename}.')

    def load_tasks(self, filename='mytasks.json'):
        try:
            with open(filename, 'r') as file:
                task_list = json.load(file)
                self.tasks = [Task(task['title'], task['description'], task['status']) for task in task_list]
            print(f'Tasks loaded from {filename}.')
        except FileNotFoundError:
            print(f'File {filename} not found. No tasks loaded.')

if __name__ == "__main__":
    todo_list = ToDoList()
    while True:
        print("\n--- To-Do List App ---")
        print("1.Add Task")
        print("2.Delete Task")
        print("3.View Tasks")
        print("4.Save Tasks")
        print("5.Load Tasks")
        print("0.Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            new_task = Task(title, description)
            todo_list.add_task(new_task)
        elif choice == "2":
            title = input("Enter the title of the task to delete: ")
            todo_list.delete_task(title)
        elif choice == "3":
            todo_list.view_tasks()
        elif choice == "4":
            todo_list.save_tasks()
        elif choice == "5":
            todo_list.load_tasks()
        elif choice == "0":
            print("Exiting the To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


