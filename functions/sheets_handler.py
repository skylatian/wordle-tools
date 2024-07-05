import requests
from datetime import datetime
from ratelimit import limits, sleep_and_retry
import gspread

from config import cookie as imported_cookie,  alt_cookie, sheetkey, worksheetID, gspread_credentials


# Set up gspread and open the worksheet
gc = gspread.service_account_from_dict(gspread_credentials)
sh = gc.open_by_key(sheetkey)
worksheet = sh.get_worksheet_by_id(worksheetID)

DATE_FORMAT = '%Y-%m-%d' # date format for the sheet (ex 2023-06-25)


def get_last_date():
    ''' Get the latest date recorded in the sheet as a datetime object'''
    #worksheet = open_sheet()
    try:
        all_values=worksheet.get_all_values()
        latest_row_a = all_values[len(all_values)-1][0]
        start_date = datetime.strptime(latest_row_a, DATE_FORMAT)
        return start_date

    except (ValueError, IndexError):
        print("sync_to_sheets.py: sheet empty or error")
        return None


@sleep_and_retry
@limits(calls=60, period=60) # https://pypi.org/project/ratelimit/
def append(var_in: list):
    #worksheet = open_sheet()
    
    try:
        worksheet.append_row(var_in, value_input_option='USER_ENTERED')  # append each row to the worksheet
        #time.sleep(0.1)
    except Exception:
        print("rate limited") # waiting 30 seconds")

@sleep_and_retry
@limits(calls=60, period=60) # https://pypi.org/project/ratelimit/
def append_rows(var_in: list):

    worksheet.append_rows(var_in, value_input_option='USER_ENTERED')  # append each row to the worksheet
    #time.sleep(0.5)
# https://docs.gspread.org/en/v5.1.0/api.html