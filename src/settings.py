import os

from dotenv import load_dotenv

load_dotenv()

DATABASE: str = os.environ['DATABASE']
EXCEL_FILE_PATH: str = os.environ['EXCEL_FILE_PATH']
