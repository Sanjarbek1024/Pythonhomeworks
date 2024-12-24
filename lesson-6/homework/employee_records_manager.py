# File to store employee records
FILE_NAME = "employees.txt"

# Function to check if the file exists
def file_exists():
    """This function checks if the file exists and returns True or False."""
    try:
        with open(FILE_NAME, "r"):
            return True
    except FileNotFoundError:
        return False

# Function to add a new employee
def add_employee(emp_id, name, department, salary):
    """This function adds a new employee record to the file."""
    with open(FILE_NAME, "a") as file:
        file.write(f"{emp_id},{name},{department},{salary}\n")
    print("Employee added successfully!")

# Function to view all employee records
def view_employees():
    """This function displays all the employee records in the file."""
    if not file_exists():
        print("No employee records found.")
        return
    with open(FILE_NAME, "r") as file:
        print("Employee Records:")
        print("-" * 50)
        print("ID\tName\t\tDepartment\tSalary")
        print("-" * 50)
        for line in file:
            emp_id, name, department, salary = line.strip().split(",")
            print(f"{emp_id}\t{name}\t{department}\t{salary}")
        print("-" * 50)

# Function to update an employee record
def update_employee(emp_id, new_name=None, new_department=None, new_salary=None):
    """This function updates the employee record with the new details."""
    if not file_exists():
        print("No employee records found.")
        return
    
    updated = False
    with open(FILE_NAME, "r") as file:
        lines = file.readlines()
    
    with open(FILE_NAME, "w") as file:
        for line in lines:
            current_id, name, department, salary = line.strip().split(",")
            if current_id == emp_id:
                updated = True
                name = new_name if new_name else name
                department = new_department if new_department else department
                salary = new_salary if new_salary else salary
                file.write(f"{emp_id},{name},{department},{salary}\n")
                print(f"Employee {emp_id} updated successfully!")
            else:
                file.write(line)
    
    if not updated:
        print(f"Employee with ID {emp_id} not found.")

# Function to delete an employee record
def delete_employee(emp_id):
    """This function deletes an employee record by ID."""
    if not file_exists():
        print("No employee records found.")
        return
    
    deleted = False
    with open(FILE_NAME, "r") as file:
        lines = file.readlines()
    
    with open(FILE_NAME, "w") as file:
        for line in lines:
            current_id, name, department, salary = line.strip().split(",")
            if current_id == emp_id:
                deleted = True
                print(f"Employee {emp_id} deleted successfully!")
            else:
                file.write(line)
    
    if not deleted:
        print(f"Employee with ID {emp_id} not found.")

# Function to search for an employee by ID
def search_employee(emp_id):
    """Search for an employee by ID, and this function displays the details."""
    if not file_exists():
        print("No employee records found.")
        return
    
    with open(FILE_NAME, "r") as file:
        for line in file:
            current_id, name, department, salary = line.strip().split(",")
            if current_id == emp_id:
                print("Employee Details:")
                print("-" * 50)
                print(f"ID: {current_id}")
                print(f"Name: {name}")
                print(f"Department: {department}")
                print(f"Salary: {salary}")
                print("-" * 50)
                return
    print(f"Employee with ID {emp_id} not found.")

# Main program
def main():
    """The main function to run the Employee Records Manager."""
    while True:
        print("\nEmployee Records Manager")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee by ID")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Employee Name: ")
            department = input("Enter Employee Department: ")
            salary = input("Enter Employee Salary: ")
            add_employee(emp_id, name, department, salary)
        elif choice == "2":
            view_employees()
        elif choice == "3":
            emp_id = input("Enter Employee ID to search: ")
            search_employee(emp_id)
        elif choice == "4":
            emp_id = input("Enter Employee ID to update: ")
            print("Leave fields empty if no update is needed.")
            new_name = input("Enter new name: ")
            new_department = input("Enter new department: ")
            new_salary = input("Enter new salary: ")
            update_employee(emp_id, new_name, new_department, new_salary)
        elif choice == "5":
            emp_id = input("Enter Employee ID to delete: ")
            delete_employee(emp_id)
        elif choice == "6":
            print("Exiting Employee Records Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

# Call the main function directly
main()