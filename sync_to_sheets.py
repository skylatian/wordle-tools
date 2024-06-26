import requests
from datetime import datetime, timedelta
from credentials import cookie as imported_cookie
import gspread
import time

# Set up gspread and open the worksheet
gc = gspread.oauth()
sh = gc.open_by_key('17gaArLv_hniaZQTBDr_M-FUT4hsUdRk5EY0eDpyTSgo')
worksheet = sh.get_worksheet(0)

date_format = '%b %d %Y'

# Get all values from the worksheet
#all_values=worksheet.get_all_values()

# Get the latest date recorded in the sheet
#latest_row_a = all_values[len(all_values)-1][0]

#worksheet.append_row('test', value_input_option='USER_ENTERED')  # append each row to the worksheet


#worksheet.append_row(['test\ntest', 'test', 'test'], value_input_option='USER_ENTERED')  # append each row to the worksheet

def get_last_date():
    ''' Get the latest date recorded in the sheet '''
    #worksheet = open_sheet()
    try:
        all_values=worksheet.get_all_values()
        latest_row_a = all_values[len(all_values)-1][0]
        return latest_row_a

    except Exception:
        print("sync_to_sheets.py: sheet empty")

def append(varIN: list):
    ''' takes list as input '''
    #worksheet = open_sheet()
    try:
        worksheet.append_row(varIN, value_input_option='USER_ENTERED')  # append each row to the worksheet
        time.sleep(0.1)
    except Exception:
        print("rate limited. waiting 30 seconds")
        time.sleep(30)

