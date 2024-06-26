from combo_func import get_puzzle
from datetime import datetime, timedelta, date
from sheets_handler import append, get_last_date
import time

#latest_date = all_values[len(all_values)-1][0]
#latest_date = "Feb 03 2023"
date_format = '%Y-%m-%d'

start_override = None # "2023-02-03"
start_default = "2023-02-03"

prev_date = get_last_date()
end_date = datetime.today()



    #start_date = datetime.strptime(start_date, date_format_out)
    #end_date = datetime.strptime(end_date, date_format_out)

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

for single_date in daterange(start_date, end_date):

    single_date = (str(single_date.strftime(date_format)))
    print(single_date)
    
    emoji, play, puzzle, stats = get_puzzle(single_date)
    
    #print(output)

    #build new row:
    row = [single_date, emoji, stats] 
    ## CHANGE THIS TO BUILD IN CHUNKS OF ROWS TO AVOID THE RATE LIMIT!!
    append(row)