class Oracle:
    def insert(self, data: str) -> None:
        print(f"Inserting {data} to Oracle database")


class Postgres:
    def _cool_insert(self, data: str) -> None:
        print(f"Inserting {data} to Postgres database")


class DbSaver:
    def __init__(self) -> None:
        self.db = Oracle()

    def save(self, data: str) -> None:
        self.db.insert(data=data)


db_saver = DbSaver()
db_saver.save(data="klopsztanga")

"""
Above DbSaver has a hard dependency to Oracle
Use Dependency Inversion to refactor the code
Save a string to both databases
Tip 1: Make an abstract class for databases
Tip 2: Make sure Postgres is compatible with DbSaver
"""
