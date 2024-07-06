from datetime import datetime, timedelta
import time
from pprint import pprint
import math

from functions.puzzle_processing import get_puzzle
from functions.sheets_handler import append_rows, get_last_date, setup_sheet

date_format = '%Y-%m-%d'


def start_date_handler(usr, start_override=None, start_default=None):
    ''' determines the start date'''

    if start_default is None:
        start_default = "2022-1-1"

    prev_date = get_last_date(usr.worksheet)
    end_date = datetime.today()

    if start_override is not None:
        start_date = datetime.strptime(start_override, date_format)
    elif start_override is None and prev_date is not None:
        start_date = prev_date + timedelta(days=1)
    elif prev_date is None and start_override is None:
        print("Error: no start date or override provided. defaulting to", start_default)
        start_date = datetime.strptime(start_default, date_format)
        time.sleep(0)
    
    return start_date, end_date

def daterange(start, end):
    '''Generate a range of dates from start_date to end_date.'''
    for n in range((end - start).days + 1):
        yield start + timedelta(n)

def chunked(user, start_date, end_date):
    '''
    splits sheet write operations into chunks to avoid rate limit
    used by default
    
    the logic is definitely overcomplicated and is probably already a library somewhere

    it splits up the list of dates into chunks, loads data for each chunk into a list,
    then writes that list to the sheet.
    
    '''
    dateList = list(daterange(start_date, end_date))
    count = len(dateList)

    print("number of dates:", count)

    div = 10 # divisor
    firstloops = math.floor(count / div)
    finalLoop = count % div
    print(firstloops, finalLoop)

    for i in range(firstloops):
        new_entries = []
        for y in range(div):
            single_date = (str(dateList[i*div + y].strftime(date_format)))
            #print(single_date)
            emoji, play, puzzle, status = get_puzzle(user.cookie, single_date)    
            new_entries.append([single_date, emoji, status])
            pprint(new_entries)
        append_rows(worksheet, new_entries)
        print("----")

    print("last loop")
    new_entries = []
            
    for i in range(finalLoop):

        single_date = (str(dateList[(firstloops*div)+i].strftime(date_format)))
        print(single_date)
        emoji, play, puzzle, status = get_puzzle(user.cookie, single_date)
        new_entries.append([single_date, emoji, status])

    pprint(new_entries)
    append_rows(user, new_entries)

## MAIN ##
def runnerd(usr, start_override=None):
    usr.worksheet = setup_sheet(usr)
    start_date, end_date = start_date_handler(usr,start_override)
    chunked(usr, start_date, end_date)
    

## END MAIN ##
