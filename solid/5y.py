from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def insert(self, data: str) -> None:
        ...


class Oracle(Database):
    def insert(self, data: str) -> None:
        print(f"Inserting {data=} to Oracle database")


class Postgres(Database):
    def _fast_insert(self, data: str) -> None:
        print(f"Inserting {data=} to Postgres database")

    def insert(self, data: str) -> None:
        self._fast_insert(data=data)


class DbSaver:
    def __init__(self, database: Database) -> None:
        self.db = database()

    def save(self, data: str) -> None:
        self.db.insert(data=data)


oracle_db_saver = DbSaver(database=Oracle)
postgres_db_saver = DbSaver(database=Postgres)

oracle_db_saver.save("gelynder")
postgres_db_saver.save("zicherka")
