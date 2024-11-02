from peewee import SqliteDatabase, Model, CharField, IntegerField
# подключаемся к базе данных my_database.db
db = SqliteDatabase("my_database.db")

# создаем модель User
class User(Model):
    # имя пользователя, CharField -- строка
    name = CharField()
    # возраст пользователя, IntegerField -- целое число
    age = IntegerField()

    # во внутреннем классе Meta указываем нашу базу данных
    class Meta:
        database = db

# создаем таблицу users в базе данных
db.create_tables([User])