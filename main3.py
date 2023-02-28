from database import Employee

try:
    emp_name = input("Enter employee name\n")
    emp_duty = input("Enter employee duty\n")
    emp_salary = input("Enter employee salary\n")
    Employee.create(name=emp_name, duty=emp_duty, salary=emp_salary)
    print("Employee details saved")
except:
    print("Something went wrong!!")