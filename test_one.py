# Write a  logic to implement a simple calculator
# capable of computing two numbers entered by the user
# as input2*
# Make sure the program can compute with either of
# the four mathematical operations

number_one = input("Enter the first  number \n")
number_two = input("Enter the second  number \n")
function = input("Enter the desired function \n")

converted_number_one = float(number_one)
converted_number_two = float(number_one)

if function == "*":
    print(converted_number_two * converted_number_two)
elif function == "+":
    print(converted_number_two + converted_number_two)
elif function == "-":
    print(converted_number_two - converted_number_two)
elif function == "/":
    print(converted_number_two / converted_number_two)
else:
    print("Enter a valid operation!!")

# Create  a function to ascertain that the user has "eMobilis" as
# username and "eMobilis@123" as password. Henceforth,proceed
# to calculate the BMI of the user and display the results of the
# BMI as either 1. Underweight, 2.normal weight, 3.Overweight
# or 4. Obese
# NOTE: All the data should be provided by the user as input
# use the scale below for the BMI
#       0 ----- 18 ------ Underweight
#       18.1 ----- 29 ------ Normal weight
#       29.1 ----- 34 ------ Overweight
#       34.1 ----- above ------ Obese

user_name = input("Enter name\n")
user_password = input("Enter password\n")
w = input("Enter your weight\n")
h = input("Enter your height\n")

converted_w = float(w)
converted_h = float(h)

if user_name == "eMobilis":
    if user_password == "eMobilis@123":
        bmi = converted_w / (converted_h * converted_h)
        if bmi <= 18:
            print("Underweight")
        elif bmi <= 29:
            print("Normal weight")
        elif bmi <= 34:
            print("Overweight")
        else:
            print("Obese")
        print("Your BMI is", bmi)
    else:
        print("Enter a valid password!!")
else:
    print("Enter a valid username!!")



