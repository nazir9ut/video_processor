from peewee import *
import datetime

# Database settings
db = SqliteDatabase('videos.db', threadlocals=True)
db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class VideoModel(BaseModel):
    path_and_file = TextField(unique=True)
    is_finished = BooleanField(default=False)
    is_bad = BooleanField(default=False)
    start_dt = DateTimeField(default=datetime.datetime.now)
    # end_dt = DateTimeField()



# class BadVideoModel(BaseModel):
#     path_and_file = TextField(unique=True)
#     start_dt = DateTimeField(default=datetime.datetime.now)
