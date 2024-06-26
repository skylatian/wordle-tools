import requests
from datetime import datetime, timedelta
from credentials import cookie as imported_cookie, alt_cookie as alt_cookie, sheetkey as sheetkey
import gspread
import time

# Set up gspread and open the worksheet
gc = gspread.oauth()
sh = gc.open_by_key(sheetkey)
worksheet = sh.get_worksheet(0)

DATE_FORMAT = '%Y-%m-%d' # date format for the sheet (ex 2023-06-25)


def append_rows(var_in):

    worksheet.append_rows(var_in, value_input_option='USER_ENTERED')  # append each row to the worksheet
    time.sleep(0.5)
# https://docs.gspread.org/en/v5.1.0/api.html

append_rows([["a", 'b'], ["c", 'd']])