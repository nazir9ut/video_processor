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
    start_dt = DateTimeField(default=datetime.datetime.now)



class BadFileModel(BaseModel):
    path_and_file = TextField(unique=True)
    is_resolved = BooleanField(default=False)
    start_dt = DateTimeField(default=datetime.datetime.now)
