from .create_database import connect_database


class BaseTools:
    def __init__(self):
        self.connection, self.cursor = connect_database("database_folders.sqlite")


class DataBaseTools(BaseTools):
    def insert_plate_info_in_table(self, company, plate_size, quantity, file_name, date_time):
        try:
            self.cursor.execute("""INSERT INTO plates (
            company, plate_size, quantity, file_name, date_time)
            VALUES (?,?,?,?,?)
            """, (company, plate_size, quantity, file_name, date_time))
        except:
            pass
        else:
            self.connection.commit()
        finally:
            self.connection.close()

    def get_plates_info(self) -> tuple:
        self.cursor.execute("""SELECT *
            FROM plates
            WHERE id = 1
        """)
        plate_info: tuple = self.cursor.fetchone()
        self.connection.close()
        return plate_info

    def get_last_row_from_database(self):
        self.cursor.execute("""SELECT * 
            FROM plates 
            ORDER BY id DESC LIMIT 1
        """)
        plate_info: tuple = self.cursor.fetchone()
        self.connection.close()
        return plate_info
