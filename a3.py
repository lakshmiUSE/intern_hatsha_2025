class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_salary(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_details(self):
        print("Name:", self.name)
        print("Department:", self.department)
        print("Total Salary:", self.salary)


m = Manager("harsha", 60000, "HR")
m.display_details()
