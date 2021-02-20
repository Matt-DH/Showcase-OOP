class Employee:
    def __init__(self, fname, lname, employee_id):
        self.fname = fname
        self.lname = lname
        self.employee_id = employee_id
    
    def __str__(self):
        return "Employee: " + str(self.fname) +\
        " " + str(self.lname) +\
        " (" + str(self.employee_id) + ")"

class WageEmployee(Employee):
    def __init__(self, fname, lname, employee_id, hourly_wage, weekly_hours):
        super().__init__(fname, lname, employee_id)
        self.hourly_wage = hourly_wage
        self.weekly_hours = weekly_hours

    def weekly_earnings(self):
        self.amtEarned = 0
        self.amtEarned = self.hourly_wage * self.weekly_hours

    def __str__(self):
        return "WageEmployee: " + str(self.fname) +\
        " " + str(self.lname) + \
        " (" + str(self.employee_id) + ") " +\
        "WEEKLY EARNINGS: $" + str(round(self.amtEarned, 2))

class SalaryEmployee(Employee):
    def __init__(self, fname, lname, employee_id, salary):
        super().__init__(fname, lname, employee_id)
        self.salary = salary

    def weeklyEarnings(self):
        self.weeklySalary = 0
        self.weeklySalary = self.salary / 52

    def __str__(self):
        return "SalaryEmployee: " + str(self.fname) +\
        " " + str(self.lname) +\
        " (" + str(self.employee_id) + ") " +\
        "WEEKLY EARNINGS: $" + str(round(self.weeklySalary, 2))


employee1 = Employee("Spongebob", "Squarepants", "RDY001")
employee2 = WageEmployee("Squidward", "Tentacles", "ART573", 7, 50)
WageEmployee.weekly_earnings(employee2)
employee3 = SalaryEmployee("Eugene", "Krabs", "MNY777", 142636)
SalaryEmployee.weeklyEarnings(employee3)

print (employee1)
print (employee2)
print (employee3)