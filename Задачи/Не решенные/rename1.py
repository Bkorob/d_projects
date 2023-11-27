class MySQLDatabase:
    def save(self, data):
        print(f"Saving {data} to MySQL database")

class User:
    def __init__(self, db):
        self.database = db

    def save_user(self, data):
        self.database.save(data)

a = User(MySQLDatabase)

a.save_user('a')
