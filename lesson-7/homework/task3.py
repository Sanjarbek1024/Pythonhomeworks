import json
import csv
import os
from datetime import datetime

class Task:
    def __init__(self, task_id, title, description, due_date=None, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status
        }

    @staticmethod
    def from_dict(data):
        return Task(
            task_id=data["task_id"],
            title=data["title"],
            description=data["description"],
            due_date=data.get("due_date"),
            status=data["status"]
        )

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date or 'N/A'}, {self.status}"


class FileHandler:
    def save(self, tasks, file_name):
        raise NotImplementedError("Subclasses must implement this method.")

    def load(self, file_name):
        raise NotImplementedError("Subclasses must implement this method.")


class JSONHandler(FileHandler):
    def save(self, tasks, file_name):
        with open(file_name, 'w') as file:
            json.dump([task.to_dict() for task in tasks], file, indent=4)

    def load(self, file_name):
        if not os.path.exists(file_name):
            return []

        with open(file_name, 'r') as file:
            return [Task.from_dict(data) for data in json.load(file)]


class CSVHandler(FileHandler):
    def save(self, tasks, file_name):
        with open(file_name, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["task_id", "title", "description", "due_date", "status"])
            writer.writeheader()
            writer.writerows([task.to_dict() for task in tasks])

    def load(self, file_name):
        if not os.path.exists(file_name):
            return []

        with open(file_name, 'r') as file:
            reader = csv.DictReader(file)
            return [Task.from_dict(row) for row in reader]


class ToDoApplication:
    def __init__(self, file_handler: FileHandler, file_name: str):
        self.file_handler = file_handler
        self.file_name = file_name
        self.tasks = self.file_handler.load(self.file_name)

    def add_task(self):
        task_id = input("Enter Task ID: ").strip()
        if any(task.task_id == task_id for task in self.tasks):
            print("Task ID already exists. Please try again.")
            return

        title = input("Enter Title: ").strip()
        description = input("Enter Description: ").strip()
        due_date = input("Enter Due Date (YYYY-MM-DD, leave blank if none): ").strip()
        status = input("Enter Status (Pending/In Progress/Completed): ").strip()

        if due_date:
            try:
                due_date = datetime.strptime(due_date, "%Y-%m-%d").date().isoformat()
            except ValueError:
                print("Invalid date format. Task not added.")
                return

        self.tasks.append(Task(task_id, title, description, due_date, status))
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return

        print("Tasks:")
        for task in self.tasks:
            print(task)

    def update_task(self):
        task_id = input("Enter Task ID to update: ").strip()
        for task in self.tasks:
            if task.task_id == task_id:
                print("Current details:")
                print(task)

                title = input("Enter new Title (leave blank to keep current): ").strip()
                description = input("Enter new Description (leave blank to keep current): ").strip()
                due_date = input("Enter new Due Date (YYYY-MM-DD, leave blank to keep current): ").strip()
                status = input("Enter new Status (Pending/In Progress/Completed, leave blank to keep current): ").strip()

                if title:
                    task.title = title
                if description:
                    task.description = description
                if due_date:
                    try:
                        task.due_date = datetime.strptime(due_date, "%Y-%m-%d").date().isoformat()
                    except ValueError:
                        print("Invalid date format. Update aborted.")
                        return
                if status:
                    task.status = status

                print("Task updated successfully!")
                return

        print("Task ID not found.")

    def delete_task(self):
        task_id = input("Enter Task ID to delete: ").strip()
        initial_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.task_id != task_id]

        if len(self.tasks) < initial_count:
            print("Task deleted successfully!")
        else:
            print("Task ID not found.")

    def filter_tasks(self):
        status = input("Enter Status to filter by (Pending/In Progress/Completed): ").strip()
        filtered_tasks = [task for task in self.tasks if task.status == status]

        if filtered_tasks:
            print("Filtered Tasks:")
            for task in filtered_tasks:
                print(task)
        else:
            print("No tasks found with the given status.")

    def save_tasks(self):
        self.file_handler.save(self.tasks, self.file_name)
        print("Tasks saved successfully!")

    def load_tasks(self):
        self.tasks = self.file_handler.load(self.file_name)
        print("Tasks loaded successfully!")

    def menu(self):
        while True:
            print("\nWelcome to the To-Do Application!")
            print("1. Add a new task")
            print("2. View all tasks")
            print("3. Update a task")
            print("4. Delete a task")
            print("5. Filter tasks by status")
            print("6. Save tasks")
            print("7. Load tasks")
            print("8. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                self.update_task()
            elif choice == '4':
                self.delete_task()
            elif choice == '5':
                self.filter_tasks()
            elif choice == '6':
                self.save_tasks()
            elif choice == '7':
                self.load_tasks()
            elif choice == '8':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    print("Choose file format: 1 for JSON, 2 for CSV")
    format_choice = input("Enter your choice: ").strip()

    if format_choice == '1':
        handler = JSONHandler()
        file_name = "tasks.json"
    elif format_choice == '2':
        handler = CSVHandler()
        file_name = "tasks.csv"
    else:
        print("Invalid choice. Defaulting to JSON format.")
        handler = JSONHandler()
        file_name = "tasks.json"

    app = ToDoApplication(handler, file_name)
    app.menu()

