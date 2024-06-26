from director import get_puzzle
from datetime import datetime, timedelta, date
from sheets_handler import append, append_rows, get_last_date
import time
from pprint import pprint
import math

date_format = '%Y-%m-%d'

start_override =  None # "2023-02-03"
start_default = "2023-02-03"

prev_date = get_last_date()
end_date = datetime.today()

if start_override is not None:
    start_date = datetime.strptime(start_override, date_format)
elif start_override is None and prev_date is not None:
    start_date = prev_date + timedelta(days=1)
elif prev_date is None and start_override is None:
    print("Error: no start date or override provided. defaulting to", start_default)
    start_date = datetime.strptime(start_default, date_format)
    time.sleep(0)

def daterange(start, end):
    '''Generate a range of dates from start_date to end_date.'''
    for n in range((end - start).days + 1):
        yield start + timedelta(n)

def chunked():
    '''
    splits sheet write operations into chunks to avoid rate limit
    used by default
    '''

    count = len(list(daterange(start_date, end_date)))
    print("number of dates:", count)

    div = 10 # divisor
    firstloops = math.floor(count / div)
    finalLoop = count % div
    print(firstloops, finalLoop)

    dateList = list(daterange(start_date, end_date))

    for i in range(firstloops):
        new_entries = []
        for y in range(div):
            single_date = (str(dateList[i*div + y].strftime(date_format)))
            emoji, play, puzzle, stats = get_puzzle(single_date)
            new_entries.append([single_date, emoji, stats])
        pprint(new_entries)
        append_rows(new_entries)
        print("----")

    print("last loop")
    new_entries = []
            
    for i in range(finalLoop):

        single_date = (str(dateList[(firstloops*div)+i].strftime(date_format)))
        emoji, play, puzzle, stats = get_puzzle(single_date)
        new_entries.append([single_date, emoji, stats])

    pprint(new_entries)
    append_rows(new_entries)

def single():

    ''' 
    writes to sheet one row at a time, no chunking.
    usually hits rate limit. included for posterity/example
    '''

    for single_date in daterange(start_date, end_date):

        single_date = (str(single_date.strftime(date_format)))
        print(single_date)
        
        emoji, play, puzzle, stats = get_puzzle(single_date)

        #build new row:
        row = [single_date, emoji, stats] 
        append(row)

chunked()
#single()