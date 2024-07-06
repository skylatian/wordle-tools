''' 
This script takes the date of a puzzle as input and retrieves the puzzle ID
It then then uses that to get further puzzle data

It then builds the emoji guess matrix from the retieved data

'''

from pprint import pprint
import requests
from config import cookie1 as imported_cookie, cookie2
#from functions.build_grid import build_emoji

COOKIE = cookie2
#COOKIE = imported_cookie

# retrieve puzzle ID from puzzle date

def build_emoji(guess,puzzleSol):
    '''
    builds the wordle matrix of emoji guesses from input
    messy for now
    '''
    matrix = ["", "", "", "", ""]
    scount = dict()
    guessed_letters = dict()

    solution = puzzleSol
    for letter in guess:
        scount[letter] = (solution.count(letter))
        guessed_letters[letter] = 0

    for li, letter in enumerate(guess):
        if solution[li] == letter:
            matrix[li] = "🟩"
            guessed_letters[letter] = guessed_letters[letter] + 1

    for li2, letter in enumerate(guess):
        #print(guessed_letters[letter], solution.count(letter))
        
        if letter in solution and guessed_letters[letter] < solution.count(letter) and  matrix[li2] == "":
            matrix[li2] = "🟨"
            guessed_letters[letter] = guessed_letters[letter] + 1
        elif letter in solution and guessed_letters[letter] >= solution.count(letter) and  matrix[li2] == "":
            matrix[li2] = "⬛"
        elif letter not in solution:
            matrix[li2] = "⬛"
            #print(matrix)
        #print(guessed_letters, solution.count(letter))
    #print(matrix)

    #print(matrix)
    s = ""
    stremoji = s.join(matrix) # joins into one string
    return stremoji
    
    #for i in matrix:
    #   print(i, end="")
    #print("")
   # print(guessed_letters)


def parse_emoji(game_data,solution):
    '''send data to emoji builder'''

    guesses = game_data['boardState']
    emoji = "" # initialize emoji string

    for current_guess in guesses:
        line = build_emoji(current_guess,solution)
        emoji = emoji + line + "\n"
    emoji = emoji.rstrip('\r\n') # remove trailing newline(s)
    return emoji

def parse_puzzle(playdata,puzzledata):
    ''' parse the API response '''

    solution = puzzledata['solution']
    #game_date = puzzledata['print_date']

    states = playdata['states'][0] # this is the data we want #guesses = ((states['game_data'])['boardState'])
    game_data = states['game_data']

    #win_status = game_data['status']
    #current_guess = game_data['currentRowIndex']

    return parse_emoji(game_data,solution)

def get_puzzle(PUZZLE_DATE):

    puzzledata = requests.get(f"https://www.nytimes.com/svc/wordle/v2/{PUZZLE_DATE}.json",timeout=10).json()
    puzzle_id = puzzledata['id']

    wordle_endpoint = f"https://www.nytimes.com/svc/games/state/wordleV2/latests?puzzle_ids={puzzle_id}"
    headers = {'Cookie': f'NYT-S=${COOKIE}'}
    playdata = requests.get(wordle_endpoint,headers=headers,timeout=10).json()
    
    #pprint(playdata)
    #pprint(playdata['states'][0]['game_data']['boardState'])

    attempt_flag = 0


    if playdata['states'] == []:
        attempt_flag = 0
        #print('empty states')
        #print(playdata['states'])
    elif playdata['states'][0]['game_data']['boardState'] == ['', '', '', '', '', '']:
        attempt_flag = 0
        #print('full states no attempt')
        #print(playdata['states'][0]['game_data']['boardState'])
    else:
        #print(playdata['states'][0]['game_data']['boardState'])
        #print('attempt!')
        attempt_flag = 1

    if attempt_flag == 0:
        #print('return no attempt')
        return ['N/A', None, None, 'NOT_STARTED'] # emoji, playdata, puzzledata, status
    elif attempt_flag == 1:
        #pprint(playdata["states"])
        out = parse_puzzle(playdata,puzzledata), playdata, puzzledata, (playdata['states'][0]['game_data'])['status'] # emoji, playdata, puzzledata, status
        #pprint(out)
        return out