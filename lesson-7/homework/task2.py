import os

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"


class EmployeeManager:
    FILE_NAME = "employees.txt"

    def __init__(self):
        if not os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, 'w'):
                pass  # Create the file if it does not exist

    def add_employee(self):
        employee_id = input("Enter Employee ID: ").strip()
        if self._employee_exists(employee_id):
            print("Employee ID already exists. Please try again.")
            return

        name = input("Enter Name: ").strip()
        position = input("Enter Position: ").strip()
        salary = input("Enter Salary: ").strip()

        try:
            salary = float(salary)
        except ValueError:
            print("Invalid salary. Please enter a number.")
            return

        employee = Employee(employee_id, name, position, salary)
        with open(self.FILE_NAME, 'a') as file:
            file.write(str(employee) + "\n")
        print("Employee added successfully!")

    def view_all_employees(self):
        try:
            with open(self.FILE_NAME, 'r') as file:
                employees = file.readlines()
                if not employees:
                    print("No employee records found.")
                    return

                print("Employee Records:")
                for record in employees:
                    print(record.strip())
        except FileNotFoundError:
            print("No employee records found.")

    def search_employee(self):
        employee_id = input("Enter Employee ID to search: ").strip()
        employee = self._find_employee(employee_id)
        if employee:
            print("Employee Found:")
            print(employee)
        else:
            print("Employee not found.")

    def update_employee(self):
        employee_id = input("Enter Employee ID to update: ").strip()
        employees = self._get_all_employees()

        for i, employee in enumerate(employees):
            if employee.employee_id == employee_id:
                print("Current details:")
                print(employee)

                name = input("Enter new Name (leave blank to keep current): ").strip()
                position = input("Enter new Position (leave blank to keep current): ").strip()
                salary = input("Enter new Salary (leave blank to keep current): ").strip()

                if name:
                    employee.name = name
                if position:
                    employee.position = position
                if salary:
                    try:
                        employee.salary = float(salary)
                    except ValueError:
                        print("Invalid salary. Update aborted.")
                        return

                employees[i] = employee
                self._write_all_employees(employees)
                print("Employee updated successfully!")
                return

        print("Employee not found.")

    def delete_employee(self):
        employee_id = input("Enter Employee ID to delete: ").strip()
        employees = self._get_all_employees()
        employees = [employee for employee in employees if employee.employee_id != employee_id]

        if len(employees) < len(self._get_all_employees()):
            self._write_all_employees(employees)
            print("Employee deleted successfully!")
        else:
            print("Employee not found.")

    def _employee_exists(self, employee_id):
        return self._find_employee(employee_id) is not None

    def _find_employee(self, employee_id):
        employees = self._get_all_employees()
        for employee in employees:
            if employee.employee_id == employee_id:
                return employee
        return None

    def _get_all_employees(self):
        employees = []
        try:
            with open(self.FILE_NAME, 'r') as file:
                for line in file:
                    parts = line.strip().split(', ')
                    if len(parts) == 4:
                        employee_id, name, position, salary = parts
                        employees.append(Employee(employee_id, name, position, float(salary)))
        except FileNotFoundError:
            pass
        return employees

    def _write_all_employees(self, employees):
        with open(self.FILE_NAME, 'w') as file:
            for employee in employees:
                file.write(str(employee) + "\n")

    def menu(self):
        while True:
            print("\nWelcome to the Employee Records Manager!")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == '1':
                self.add_employee()
            elif choice == '2':
                self.view_all_employees()
            elif choice == '3':
                self.search_employee()
            elif choice == '4':
                self.update_employee()
            elif choice == '5':
                self.delete_employee()
            elif choice == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    manager = EmployeeManager()
    manager.menu()
