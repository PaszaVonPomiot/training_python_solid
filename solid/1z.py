class Employee:
    def __init__(self, name: str, title: str, salary: float) -> None:
        self.name = name
        self.title = title
        self.salary = salary

    def get_employee_info(self) -> str:
        return f"{self.name} is a {self.title} earning {self.salary} per year."


class EmployeeDatabase:
    def save_employee_to_database(self, employee: Employee) -> None:
        print(f"Saving {employee.name} to database...")


employee = Employee(name="John", title="Engineer", salary=6666.66)
print(employee.get_employee_info())

employee_db = EmployeeDatabase()
employee_db.save_employee_to_database(employee=employee)
