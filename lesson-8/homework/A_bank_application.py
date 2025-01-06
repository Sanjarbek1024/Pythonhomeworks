import os

class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def to_string(self):
        return f"{self.account_number},{self.name},{self.balance}"

    @staticmethod
    def from_string(account_str):
        account_number, name, balance = account_str.split(",")
        return Account(int(account_number), name, float(balance))


class Bank:
    def __init__(self):
        self.accounts = {}
        self.file_path = "accounts.txt"
        self.ensure_file_exists()
        self.load_from_file()

    def ensure_file_exists(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as file:
                pass

    def create_account(self, name, initial_deposit):
        if initial_deposit < 0:
            raise ValueError("Initial deposit cannot be negative.")

        while True:
            try:
                account_number = int(input("Enter a unique account number: "))
                if account_number in self.accounts:
                    print("Account number already exists. Please try again.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = account
        self.save_to_file()
        return account_number

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            return account
        else:
            raise ValueError("Account not found.")

    def deposit(self, account_number, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        account = self.accounts.get(account_number)
        if account:
            account.balance += amount
            self.save_to_file()
        else:
            raise ValueError("Account not found.")

    def withdraw(self, account_number, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        account = self.accounts.get(account_number)
        if account:
            if account.balance >= amount:
                account.balance -= amount
                self.save_to_file()
            else:
                raise ValueError("Insufficient funds.")
        else:
            raise ValueError("Account not found.")

    def save_to_file(self):
        with open(self.file_path, "w") as file:
            for account in self.accounts.values():
                file.write(account.to_string() + "\n")

    def load_from_file(self):
        try:
            with open(self.file_path, "r") as file:
                for line in file:
                    account = Account.from_string(line.strip())
                    self.accounts[account.account_number] = account
        except FileNotFoundError:
            pass


def main():
    bank = Bank()

    while True:
        print("\nWelcome to the Bank Application")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                name = input("Enter your name: ")
                initial_deposit = float(input("Enter initial deposit: "))
                account_number = bank.create_account(name, initial_deposit)
                print(f"Account created successfully! Your account number is {account_number}.")

            elif choice == "2":
                account_number = int(input("Enter your account number: "))
                account = bank.view_account(account_number)
                print("Account Details:")
                print(f"Account Number: {account.account_number}")
                print(f"Name: {account.name}")
                print(f"Balance: {account.balance}")

            elif choice == "3":
                account_number = int(input("Enter your account number: "))
                amount = float(input("Enter deposit amount: "))
                bank.deposit(account_number, amount)
                print("Deposit successful!")

            elif choice == "4":
                account_number = int(input("Enter your account number: "))
                amount = float(input("Enter withdrawal amount: "))
                bank.withdraw(account_number, amount)
                print("Withdrawal successful!")

            elif choice == "5":
                print("Thank you for using the Bank Application. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
