import logging
import os.path

from parser import Parser
from settings import EXCEL_FILE_PATH, DATABASE
from storage import Storage


def _check_file_paths_validation() -> None:
    if not os.path.exists(EXCEL_FILE_PATH):
        logging.error('Неверно указан путь excel файлу с данными')
        raise
    if not DATABASE.endswith('.db'):
        logging.error('Неверный формат файла базы данных')
        raise


def main() -> None:
    _check_file_paths_validation()
    try:
        Storage().create_database()
        if not Storage().check_exists_data():
            Parser().parse_data()
        print(Storage().get_totals())
    except Exception as er:
        raise er


if __name__ == '__main__':
    main()
