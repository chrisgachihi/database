
try:
    p = input("Enter the amount to be used as the principal!\n")
    r = input("Enter the rate of your interest!\n")
    t = input("Enter the duration of your interest!\n")

    converted_p = float(p)
    converted_r = float(r)
    converted_t = float(t)

    interest = (converted_p * converted_r * converted_t) / 100
    print("Your accumulated interest is", interest)

except:
    print("An error occurred")
