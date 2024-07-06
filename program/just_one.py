from functions.puzzle_processing import get_puzzle
from pprint import pprint
from config import *

single_date = "2024-06-18" #"2024-04-06"

cookie = user1.cookie

emoji, playdata, puzzledata, status, guesses = get_puzzle(cookie, single_date)

#print(emoji,status)

pprint(playdata)
#print((playdata['states'][0]['game_data'])['currentRowIndex'])

#game_data = playdata['states'][0]['game_data']

#solved_in = game_data['currentRowIndex']
print('-----------------')
print(emoji)