import logging
import os
import sqlite3
from sqlite3 import OperationalError

from settings import DATABASE


class Storage:

    @staticmethod
    def __connect_database():
        try:
            return sqlite3.connect(DATABASE)
        except OperationalError as er:
            logging.error('Ошибка в подключении к базе данных. Проверьте валидность пути к файлу')
            raise er

    def check_exists_data(self) -> bool:
        with self.__connect_database() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM prices;")
            return bool(cursor.fetchone()[0])

    def create_database(self) -> None:
        if not os.path.exists(DATABASE):
            with self.__connect_database() as conn:
                conn.execute("""
                    CREATE TABLE IF NOT EXISTS prices (
                        ID INT NOT NULL PRIMARY KEY,
                        COMPANY VARCHAR(20) NOT NULL,
                        QLIQ_FACT INT NOT NULL,
                        QOIL_FACT INT NOT NULL,
                        QLIQ_FORECAST INT NOT NULL,
                        QOIL_FORECAST INT NOT NULL,
                        DATE DATE NOT NULL
                    );
                """)
                conn.commit()

    def insert_row(self, row: list) -> None:
        with self.__connect_database() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO prices VALUES (?,?,?,?,?,?,?)", row)
            conn.commit()

    def get_totals(self) -> list[tuple]:
        with self.__connect_database() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT DATE, SUM(QLIQ_FACT), SUM(QOIL_FACT), SUM(QLIQ_FORECAST), SUM(QOIL_FORECAST) FROM prices
                GROUP BY DATE;
            """)
            return cursor.fetchall()
