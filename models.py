import datetime

from peewee import Model, SqliteDatabase, IntegerField, CharField, TextField, DateTimeField

db = SqliteDatabase("bbs.sqlite")


# 投稿のモデル
class Post(Model):
    """Post Model"""

    id = IntegerField(primary_key=True)
    name = CharField()
    body = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
        table_name = "posts"


# テーブルがなければ作成する
db.create_tables([Post])
