import requests
from pprint import pprint
from config import *

single_date = "2023-06-01" #"2024-04-06"
PUZZLE_DATE = single_date
COOKIE = user1.cookie

class puzzle:
    def __init__(self):
        self.name = "puzzle"
        self.states = None
        self.status = None
        self.rowIndex = None
        self.playdata = None
        self.attempt_flag = 0
        self.solution = None
        self.data = []
        self.id = 0
        self.player = []
        self.game_data = []
        self.emoji = None

pz = puzzle()

def parse_emoji(game_data,solution):
    '''send data to emoji builder'''

    guesses = game_data['boardState']
    emoji = "" # initialize emoji string

    for current_guess in guesses:
        line = line_builder(current_guess,solution)
        emoji = emoji + line + "\n"
    emoji = emoji.rstrip('\r\n') # remove trailing newline(s)
    pz.emoji = emoji
    return emoji

def line_builder(guess,puzzleSol):
    '''
    builds the wordle matrix of emoji guesses from input
    messy for now. it works.
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
   
## get_puzzle_data ##
def get_puzzle(PUZZLE_DATE, COOKIE):
    pz.data = requests.get(f"https://www.nytimes.com/svc/wordle/v2/{PUZZLE_DATE}.json",timeout=10).json()
    pz.id = pz.data['id']
    pz.solution = pz.data['solution']

    wordle_endpoint = f"https://www.nytimes.com/svc/games/state/wordleV2/latests?puzzle_ids={pz.id}"
    headers = {'Cookie': f'NYT-S=${COOKIE}'}
    pz.playdata = requests.get(wordle_endpoint,headers=headers,timeout=10).json() # this is the most information

    pz.states = pz.playdata['states']
    pz.player = pz.playdata['player']

    if pz.playdata['states'] == [] or pz.playdata['states'][0]['game_data']['boardState'] == ['', '', '', '', '', '']:
        pz.attempt_flag = 0 # empty states = no attempt. also, sometimes states has content, but boardState is empty
        pz.status = "NOT_STARTED"

    else:
        pz.states = pz.playdata['states'][0]
        pz.attempt_flag = 1  # generally this means there was an attempt
        pz.game_data = pz.playdata['states'][0]['game_data']
        pz.status = pz.playdata['states'][0]['game_data']['status']
        pz.rowIndex = pz.playdata['states'][0]['game_data']['currentRowIndex'] # emoji, playdata, puzzledata, status
        parse_emoji(pz.game_data,pz.solution)

get_puzzle(PUZZLE_DATE, COOKIE)

#print(pz.status)
#print(pz.solution)
#print(pz.emoji)
