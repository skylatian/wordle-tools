''' builds the wordle matrix of emoji guesses from input '''

def get_solution_by_date():
    ''' get the solution to the wordle puzzle by date. input date in format YYYY-MM-DD '''
    pass

solution = 'aacde'

guesses = ['12aaa']

i = 0

def build_emoji(guess):
    li = 0

    for letter in guess:
        li = li + 1
        #print(f"{li} {letter}")
        if solution[li-1] == letter:
            print(f"🟩", end="")
            pass
        elif letter in solution:
            let[letter] =  
            if (solution.count(letter) < guess.count(letter)):
                
                #print(solution.count(letter), guess.count(letter))
                print(f"n", end="")
            else:
                print(f"🟨", end="")
                #print(solution.count(letter), guess.count(letter))
                pass
        else:
            print(f"⬛", end="")
            pass
    
    print("")

for each in guesses:
    #print(each)
    #i = i + 1 # guess number
    current_guess = each
    build_emoji(current_guess)

