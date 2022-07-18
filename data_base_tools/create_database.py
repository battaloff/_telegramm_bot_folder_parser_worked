import sqlite3


def connect_database(db_path: str = "../database_folders.sqlite") -> tuple:
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    return connection, cursor


class InitDataBase:
    def __init__(self):
        self.connection, self.cursor = connect_database()

    def create_file_names(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS plates(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company VARCHAR(30),
        plate_size VARCHAR(30),
        quantity INTEGER,
        file_name VARCHAR(50),
        date_time VARCHAR(50),
        UNIQUE (file_name, quantity, plate_size, company)
        )""")

    def init(self):
        self.create_file_names()
        self.connection.commit()
        self.connection.close()


if __name__ == "__main__":
    InitDataBase().init()
