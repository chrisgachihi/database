from database import Administration

administration = Administration.select()
for administration in administration:
    print(Administration.name, Administration.number, Administration.course,
          Administration.room, Administration.age)
