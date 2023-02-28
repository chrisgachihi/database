from peewee import *
from os import path
db_connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(db_connection, "eMobilis.db"))


# create a table for users
class User(Model):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db


User.create_table(fail_silently=True)


class Product(Model):
    name = CharField()
    qtty = CharField()
    price = CharField()

    class Meta:
        database = db


Product.create_table(fail_silently=True)


class Employee(Model):
    name = CharField()
    duty = CharField()
    salary = CharField()

    class Meta:
        database = db


Employee.create_table(fail_silently=True)


class Administration(Model):
    name = CharField()
    number = CharField()
    course = CharField()
    room = CharField()
    age = CharField()

    class Meta:
        database = db


Administration.create_table(fail_silently=True)


class Hesabu(Model):
    principal = CharField()
    rate = CharField()
    time = CharField()
    pi = CharField()
    radius = CharField()
    height = CharField()

    class Meta:
        database = db


Hesabu.create_table(fail_silently=True)














