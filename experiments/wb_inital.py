''' 
DO NOT USE
(attempts to) build the wordle matrix of emoji guesses from input.
The issue is it doesn't deal with repeated letters in the solution correctly

'''

def get_solution_by_date():
    ''' get the solution to the wordle puzzle by date. input date in format YYYY-MM-DD '''
    pass

solution = 'sassy'

guesses = ['sssss']

i = 0
def build_emoji(guess):
    li=0
    matrix = [0,0,0,0,0]
    scount = dict()
    gcount = dict()
    for letter in guess:
        scount[letter] = (solution.count(letter))
        gcount[letter] = (guess.count(letter))
    #print(scount)
    print(gcount)
    letters_guessed = guess
    print(letters_guessed)


    matrix[0] = [0,0,0,0,0]

    for letter in guess:
        li = li + 1
        #gcount[letter] = gcount[letter] + 1
        #print(f"{li} {letter}")
        

        # if letter is in wrong place
        if letter in solution and solution[li-1] != letter:
            if gcount[letter] > solution.count(letter):
                print(f"🟨", end="")
            else:
                print(f"⬛", end="")
        
        # if letter is not in solution
        if letter not in solution:
            print(f"⬛", end="")

        # if letter is in correct location
        if solution[li-1] == letter:
            print(f"🟩", end="")
        
            gcount[letter] = gcount[letter] - 1


    print("")
        

for each in guesses:
    #print(each)
    #i = i + 1 # guess number
    current_guess = each
    build_emoji(current_guess)

