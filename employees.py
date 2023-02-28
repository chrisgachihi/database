from database import Employee

employee = Employee.select()
for employee in employee:
    print(employee.name, employee.duty, employee.salary)
