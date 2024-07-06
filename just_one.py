from functions.puzzle_processing import get_puzzle
from pprint import pprint

single_date = "2024-06-18" #"2024-04-06"

emoji, playdata, puzzledata, status = get_puzzle(single_date)

#print(emoji,status)

pprint(playdata)
#print((playdata['states'][0]['game_data'])['currentRowIndex'])

#game_data = playdata['states'][0]['game_data']

#solved_in = game_data['currentRowIndex']