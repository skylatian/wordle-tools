''' builds the wordle matrix of emoji guesses from input '''

def get_solution_by_date():
    ''' get the solution to the wordle puzzle by date. input date in format YYYY-MM-DD '''
    pass

solution = 'sassy'

guesses = ['sxxxx', "ssxxx", "sssxx", "ssssx"]

i = 0
def build_emoji(guess):
    array =  ['⬛','⬛','⬛','⬛','⬛']
    scount = dict()
    guessed_letters = dict()
    for letter in guess:
        scount[letter] = (solution.count(letter))
        guessed_letters[letter] = 0

    for li, letter in enumerate(guess):
        if solution[li] == letter:
            array[li] = "🟩"
            guessed_letters[letter] = guessed_letters[letter] + 1

    for li2, letter in enumerate(guess):
         if letter in solution and guessed_letters[letter] < solution.count(letter) and  array[li2] ==  '⬛':
             array[li2] = "🟨"
             guessed_letters[letter] = guessed_letters[letter] + 1
        
        
    return array
    #print(matrix)
    #print(guessed_letters)
    
        

for i, eachg in enumerate(guesses):
    i = i+1
    matrix = ['0','0','0','0','0']
    current_guess = eachg

    matrix[i] = build_emoji(current_guess)
    for i in matrix[i]:
        print(i, end="")
    print("")

