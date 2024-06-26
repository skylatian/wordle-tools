'''
builds the wordle matrix of emoji guesses from input
messy for now
'''

#guesses = ['sssss']

i = 0
def build_emoji(guess,puzzleSol):
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
    
        

