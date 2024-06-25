from combo_func import get_data
from datetime import datetime, timedelta, date
from sync_to_sheets import append, get_last_date

#latest_date = all_values[len(all_values)-1][0]
#latest_date = "Feb 03 2023"
date_format_in = '%b %d %Y'
date_format_out = '%Y-%m-%d'

start_date = "2023-02-05"

#start_date = datetime.strptime(latest_date, date_format_in) + timedelta(days=1)
sheet_start_date = str(get_last_date()) #datetime.strptime(start_date, date_format_out)
end_date = datetime.today()

print(datetime.strptime(sheet_start_date, date_format_out))

try:
    sheet_start_date = datetime.strptime(sheet_start_date, date_format_out)
    start_date = sheet_start_date
    print("Previous date found in sheet:", start_date)
except Exception:
    print("Invalid date format, defaulting to", start_date)

def daterange(start, end):
    '''Generate a range of dates from start_date to end_date.'''
    for n in range((end - start).days + 1):
        yield start + timedelta(n)

for single_date in daterange(start_date, end_date):

    single_date = (str(single_date.strftime(date_format_out)))
    print(single_date)
    
    output = get_data(single_date)
    #if ['⬛','🟩','🟨'] not in output:
    
    if output == None:
        output = "no data"    
    elif '⬛' not in output or '🟩' not in output or '🟨' not in output:
        output = "No Attempt Made"
    else:
        pass

    print(output)

    #build new row:
    row = [single_date, output]
    append(row)