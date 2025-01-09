import json
import csv

def load_tasks(file_name):
    """Load tasks from a JSON file."""
    try:
        with open(file_name, 'r') as file:
            tasks = json.load(file)
        return tasks
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return []

def display_tasks(tasks):
    """Display all tasks."""
    print("\nTasks:")
    print(f"{'ID':<5}{'Task Name':<20}{'Completed':<10}{'Priority':<10}")
    print("-" * 45)
    for task in tasks:
        print(f"{task['id']:<5}{task['task']:<20}{task['completed']:<10}{task['priority']:<10}")

def save_tasks(tasks, file_name):
    """Save tasks back to the JSON file."""
    with open(file_name, 'w') as file:
        json.dump(tasks, file, indent=4)

def calculate_statistics(tasks):
    """Calculate and display task statistics."""
    total_tasks = len(tasks)
    completed_tasks = sum(task['completed'] for task in tasks)
    pending_tasks = total_tasks - completed_tasks
    average_priority = sum(task['priority'] for task in tasks) / total_tasks if total_tasks > 0 else 0

    print("\nTask Completion Statistics:")
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")
    print(f"Average priority: {average_priority:.2f}")

def convert_json_to_csv(json_file, csv_file):
    """Convert JSON task data to a CSV file."""
    tasks = load_tasks(json_file)
    if tasks:
        with open(csv_file, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'task', 'completed', 'priority'])
            writer.writeheader()
            for task in tasks:
                writer.writerow(task)
        print(f"Tasks have been successfully exported to '{csv_file}'.")

# Main Program
if __name__ == "__main__":
    json_file_name = "tasks.json"
    csv_file_name = "tasks.csv"

    # Sample JSON file creation
    sample_tasks = [
        {"id": 1, "task": "Do laundry", "completed": False, "priority": 3},
        {"id": 2, "task": "Buy groceries", "completed": True, "priority": 2},
        {"id": 3, "task": "Finish homework", "completed": False, "priority": 1}
    ]

    # Save sample tasks to tasks.json (if not exists)
    with open(json_file_name, 'w') as file:
        json.dump(sample_tasks, file, indent=4)

    # Load tasks
    tasks = load_tasks(json_file_name)

    # Display tasks
    display_tasks(tasks)

    # Display task statistics
    calculate_statistics(tasks)

    # Modify a task (example)
    tasks[0]['completed'] = True
    save_tasks(tasks, json_file_name)

    # Convert JSON data to CSV
    convert_json_to_csv(json_file_name, csv_file_name)
