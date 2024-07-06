from runner import runnerd
from config import *
from functions.sheets_handler import setup_sheet
#runnerd()

# parameters we want:
# credentials(?)
# sheet ID
# worksheet ID
# start date/override

default = "2022-01-01"

#date_start_in = input(f"Enter start date (Default: {default}): ") or default
#date_start_out = input(f"Enter start date (Default: {default}): ") or default

#print(input)

#start_override =  None #"2023-12-25"

#print(user2.wsID)

runnerd(user1)
user = user1

COOKIE = user.cookie
wsID = user.wsID