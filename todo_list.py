import json
from datetime import datetime

class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at
        }

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print("Task added successfully!")

    def edit_task(self, index, new_description):
        if 0 <= index < len(self.tasks):
            self.tasks[index].description = new_description
            print("Task updated successfully!")
        else:
            print("Invalid task index!")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            print("Task deleted successfully!")
        else:
            print("Invalid task index!")

    def mark_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            print("Task marked as complete!")
        else:
            print("Invalid task index!")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for i, task in enumerate(self.tasks):
                status = "✓" if task.completed else " "
                print(f"{i}. [{status}] {task.description} (Created: {task.created_at})")

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            json.dump([task.to_dict() for task in self.tasks], f)
        print(f"Tasks saved to {filename}")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.tasks = [Task(**task_data) for task_data in data]
            print(f"Tasks loaded from {filename}")
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with an empty task list.")

def main():
    todo_list = TodoList()
    filename = "tasks.json"

    todo_list.load_from_file(filename)

    while True:
        print("\n--- Todo List Application ---")
        print("1. Add task")
        print("2. Edit task")
        print("3. Delete task")
        print("4. Mark task as complete")
        print("5. Display tasks")
        print("6. Save and quit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == '2':
            todo_list.display_tasks()
            index = int(input("Enter the index of the task to edit: "))
            new_description = input("Enter the new task description: ")
            todo_list.edit_task(index, new_description)
        elif choice == '3':
            todo_list.display_tasks()
            index = int(input("Enter the index of the task to delete: "))
            todo_list.delete_task(index)
        elif choice == '4':
            todo_list.display_tasks()
            index = int(input("Enter the index of the task to mark as complete: "))
            todo_list.mark_complete(index)
        elif choice == '5':
            todo_list.display_tasks()
        elif choice == '6':
            todo_list.save_to_file(filename)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()