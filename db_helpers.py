from db_settings import *

def db_table_init():
    if not VideoModel.table_exists():
        db.create_tables([VideoModel])
    if not BadVideoModel.table_exists():
        db.create_tables([BadVideoModel])