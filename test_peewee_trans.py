from peewee import *
from db_settings import *


with db.atomic() as txn:
    # This is the outer-most level, so this block corresponds to
    # a transaction.
    VideoModel.create(path_and_file='1111')

    # with db.atomic() as nested_txn:
    #     # This block corresponds to a savepoint.
    #     User.create(username='huey')
    #
    #     # This will roll back the above create() query.
    #     nested_txn.rollback()

    VideoModel.create(path_and_file='111')

