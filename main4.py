from database import Administration

try:
    adm_name = input("Enter Administration name\n")
    adm_no = input("Enter Administration number \n")
    adm_course = input("Enter the Pursued course \n")
    adm_room = input("Enter Administration room\n")
    adm_age = input("Enter your age\n")
    Administration.create(name=adm_name, number=adm_no,course=adm_course,
                          room=adm_room, age=adm_age)
    print(adm_name, "details have been saved successfully")
except:
    print("Please enter valid credentials")
