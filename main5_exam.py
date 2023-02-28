from database import Hesabu

try:
    p = input("Enter the amount to be used as the principal!\n")
    r = input("Enter the rate of your interest!\n")
    t = input("Enter the duration of your interest!\n")
    Hesabu.create(principal=p, rate=r, time=t)

    converted_p = float(p)
    converted_r = float(r)
    converted_t = float(t)

    interest = (converted_p * converted_r * converted_t) / 100
    print("Your accumulated interest is", interest)

except:
    print("An error occurred")

try:
    pi = input("Enter the pi function to be used!\n")
    r = input("Enter the radius of your cylinder!\n")
    h = input("Enter the height of your cylinder!\n")

    converted_pi = float(pi)
    converted_r = float(r)
    converted_h = float(h)

    volume = converted_pi * pow(converted_r, 2) * converted_h
    print("The volume of your cylinder is", volume, )

except:
    print("An error occurred")
