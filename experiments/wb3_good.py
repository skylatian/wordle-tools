''' builds the wordle matrix of emoji guesses from input '''

def get_solution_by_date():
    ''' get the solution to the wordle puzzle by date. input date in format YYYY-MM-DD '''
    pass

solution = 'sassy'

guesses = ['sssss','sasds','sassd','sassy']
#guesses = ['sssss']

i = 0
def build_emoji(guess):
    matrix = [0,0,0,0,0]
    scount = dict()
    guessed_letters = dict()

    for letter in guess:
        scount[letter] = (solution.count(letter))
        guessed_letters[letter] = 0

    for li, letter in enumerate(guess):
        if solution[li] == letter:
            matrix[li] = "🟩"
            guessed_letters[letter] = guessed_letters[letter] + 1



    for li2, letter in enumerate(guess):
        #print(guessed_letters[letter], solution.count(letter))
        
        if letter in solution and guessed_letters[letter] < solution.count(letter) and  matrix[li2] == 0:
            matrix[li2] = "🟨"
            guessed_letters[letter] = guessed_letters[letter] + 1
        elif letter in solution and guessed_letters[letter] >= solution.count(letter) and  matrix[li2] == 0:
            matrix[li2] = "⬛"
        elif letter not in solution:
            matrix[li2] = "⬛"
            #print(matrix)
        #print(guessed_letters, solution.count(letter))
    #print(matrix)

    #print(matrix)
    for i in matrix:
       print(i, end="")
    print("")
   # print(guessed_letters)
    
        

for each in guesses:
    #print(each)
    #i = i + 1 # guess number
    current_guess = each
    build_emoji(current_guess)


