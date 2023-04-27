import datetime
from random import randint

import openpyxl
from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet

from settings import EXCEL_FILE_PATH
from storage import Storage


class Parser:

    def parse_data(self) -> None:
        worksheet: Worksheet = self._get_worksheet()
        for i in range(3, 23):
            row: list = []
            for col in worksheet.iter_cols(1, 10):
                row.append(col[i].value)
            row = self._sum_data(row)
            self._add_date(row)
            Storage().insert_row(row)

    @staticmethod
    def _get_worksheet() -> Worksheet:
        workbook: Workbook = openpyxl.load_workbook(EXCEL_FILE_PATH)
        return workbook.active

    @staticmethod
    def _sum_data(row: list) -> list:
        return [row[0], row[1], row[2] + row[3], row[4] + row[5], row[6] + row[7], row[8] + row[9]]

    @staticmethod
    def _add_date(row: list) -> None:
        row.append(datetime.date(2023, 4, randint(5, 14)))
