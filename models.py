import datetime
import psycopg2
from peewee import *

DB = PostgresqlDatabase('courses', user='postgres')

class Course(Model):
    title = CharField()
    url = CharField(unique=True)
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DB

class Review(Model):
    course = ForeignKeyField(Course, related_name='review_set')
    rating = IntegerField()
    comment = TextField(default='')
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DB

def initialize():
    DB.connect()
    DB.create_tables([Course, Review], safe=True)
    DB.close()

