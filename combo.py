''' 
This script takes the date of a puzzle as input and retrieves the puzzle ID
It then then uses that to get further puzzle data

It then builds the emoji guess matrix from the retieved data

'''

from pprint import pprint
import requests
from credentials import cookie as imported_cookie
from credentials import alt_cookie as alt_cookie
from wordleMatrix import build_emoji


#COOKIE = alt_cookie
COOKIE = imported_cookie

PUZZLE_DATE = "2024-06-25"

# retrieve puzzle ID from puzzle date
puzzledata = requests.get(f"https://www.nytimes.com/svc/wordle/v2/{PUZZLE_DATE}.json",timeout=10).json()
PUZZLE_ID = puzzledata['id']
puzzleSol = puzzledata['solution']

response_date = requests.get(
    f"https://www.nytimes.com/svc/wordle/v2/{PUZZLE_DATE}.json",
    timeout=10
).json()

WORDLE_ENDPOINT = f"https://www.nytimes.com/svc/games/state/wordleV2/latests?puzzle_ids={PUZZLE_ID}"
headers = {'Cookie': f'NYT-S=${COOKIE}'}

response = requests.get(WORDLE_ENDPOINT,headers=headers,timeout=10).json()

states = response['states'][0] # this is the data we want

PUZZLE_ID = states['puzzle_id']  # I know this is defined already
print_date = states['print_date']

game_data = states['game_data']

#pprint(game_data)

win_status = game_data['status']
current_guess = game_data['currentRowIndex']

if win_status == 'WIN':
    
    print(f"Wordle solved in {current_guess} guesses")
elif win_status == 'IN_PROGRESS':
    print(f"Wordle still in progress at guess #{current_guess}")


#print(puzzle_id)
pprint(game_data['boardState'])

guesses = game_data['boardState']

for each in guesses:
    #print(each)
    #i = i + 1 # guess number
    current_guess = each
    build_emoji(current_guess,puzzleSol)