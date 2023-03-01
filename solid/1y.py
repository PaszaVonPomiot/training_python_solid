class Employee:
    def __init__(self, name: str, title: str, salary: float) -> None:
        self.name = name
        self.title = title
        self.salary = salary

    def get_employee_info(self) -> str:
        return f"{self.name} is an {self.title} earning {self.salary} per year."

    def save_employee_to_database(self) -> None:
        print(f"Saving {self.name} to database...")


employee = Employee(name="John", title="Engineer", salary=6666.66)
print(employee.get_employee_info())
employee.save_employee_to_database()

"""
Refactor above to resolve SRP violation
Call both methods get_employee_info() and save_employee_to_database()
Tip 1: Make a separate class responsible for database operations
"""
