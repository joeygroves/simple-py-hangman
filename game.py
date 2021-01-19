#CO1102 Programming Fundamentals COURSEWORK 2 (2018/19)
#Authors: Joey Groves and Sean Raisi

import random

def is_secret_guessed(secret_word, letters_guessed): #Authors: Joey Groves and Sean Raisi
    letters_guessed = sorted(letters_guessed)       #Sorts letters_guessed in alphabetical order
    secret_word = secret_word.lower()       #Changes secret_word into lowercase
    unique_secret_char = []        #Initialises a list of unique characters from secret word

    try:        #Try statement will attempt to remove duplicate letters from secret_word
        for i in secret_word:       #Removes duplicates from secret_word
            if i not in unique_secret_char:        
                unique_secret_char.append(i)
    except:
        print("An Error in removing duplicate characters has occured")
    
    unique_secret_char = sorted(unique_secret_char)       #Sorts unique_char in alphabetical order
    
    if set(letters_guessed) > set(unique_secret_char):      #If the set of characters of the secret word
        return True                                         #is a subset of letters guessed or is equivalent then True is returned
    elif set(letters_guessed) == set(unique_secret_char):   #otherwise false is returned
        return True
    else:
        return False

    
def get_current_guess(secret_word, letters_guessed): #Authors: Sean Raisi and Joey Groves
    guess= []
    for x in range(len(secret_word)):
        guess.append("_")       #For every letter in the secret word, an underscore is added to an empty list
    
    for i in range (len(letters_guessed)):    #The letter in each position for each index in the range of the length of the list letters_guessed
        for j in range(len(secret_word)):     #and secret_word and if they are equal then the letter is added to the corresponding position in guess
            if letters_guessed[i] == secret_word[j]:
                guess[j] = letters_guessed[i]
                
    guess = ''.join(guess)                  #Joins the substring from list 'guess' so it becomes one uniform string
    return guess


def choose_secret_word(): #Author: Sean Raisi and Joey Groves
    try:                                        #Try statement to attempt to open file: words.txt
        words_txt = open("words.txt", "r")
        list_words=[]                           #list_words list initialised
        try:                                    #Try statement to attempt to append every single word from file into 'list_words'
            for line in words_txt:
                list_words.append(line)
            rand_word= random.choice(list_words)        #rand_word chooses a random word from 'list_words'
            rand_word= ' '.join(rand_word.split())      #Then rand_word removes and empty spaces from the start or at the end of the string
        finally:
            words_txt.close()                           #File is closed
    except:
        print("Error: File cannot be opened!")          #Exception is raised if program is unable to open file
    return rand_word


def decision(): #Author Joey Groves
    print()
    try:            #Try statement to handle non-integer values inputted by the user
        decision_user = int(input("Enter '1' if you would like to start another game, otherwise enter any number to quit: "))
        
    except ValueError:      #Exception raised if a non-integer value is inputted
        print("A non-integer value has been inputted")

    return decision_user


def first_game(secret_word): #Author: Joey Groves
    print("-----------------------------------------------------")      #Opening Main Menu
    print("             Welcome to the Hangman Game             ")        
    print("             By: Joey Groves and Sean Raisi          ")
    print("-----------------------------------------------------")
    print()
    print("First Game: Secret Word Is Manually Selected")
    print()

    secret_word = secret_word.lower()       #Casts lowercase function onto selected secret word
    length_sw = len(secret_word)        #Stores length of secret word for while loop
    print("The secret word has", str(length_sw), "characters.")
    print()
    
    number_of_guesses = 10     #Stores value of no. of guesses user is allowed
    count = 0                   #Counter to increment number of guesses left for user
    letters_guessed = []        #Initialises a list of letters_guessed
    win_Bool = False            #Initialises a Boolean value for while condition
    lose_Bool = False           #Initialises a Boolean value for while condition
    win_count = 0               #Initialises a count for the number of wins
    lose_count = 0              #Initialises a count for the number of loses
    
    while (count != number_of_guesses) and (win_Bool != True) and (lose_Bool != True):      #While Loop will stop running if either: count reaches the number of guesses; the user wins or if the user loses
        print("You have " + str((number_of_guesses) - (count)) +" guesses")     #Variable storing string with number of guesses, the user has left
        
        try:
            usr_guess_char = input("Guess a character in the secret word: ").lower() #Gets users input
            assert len(usr_guess_char) == 1
            
            if usr_guess_char not in letters_guessed:       #Checks to see if user's guess has been guessed before and appends them to the letters_guessed list
                letters_guessed.append(usr_guess_char)
            else:
                print()
                print("You have already guessed '", str(usr_guess_char), "'")

            tmp_current_guess = get_current_guess(secret_word, letters_guessed)        #Gets the current guess and displays the partially guessed secret word
            print("The partially guessed word is:", tmp_current_guess)
            print()

            if is_secret_guessed(secret_word, letters_guessed) == True:         #Checks to see if the secret word has been guessed by the user; User Wins
                win_Bool = True
                print("It's a win!")
                win_count += 1
                    
        except AssertionError:          #Deals with user string input being greater than length 1
            print()
            print("ERROR: String entered has a length greater than 1, please enter a character")
            print()
        
        count += 1      #Increments counter


    if (count == number_of_guesses) and (win_Bool == False):      #Checks to see if user has ran out of guesses; User Loses
        print("You have ran out of guesses\nIt's a loss!")
        print("The word was:", str(secret_word))
        lose_count += 1
        lose_Bool = True
            
    return win_count


def second_game(): #Author: Joey Groves
    print()
    print("-----------------------------------------------------")      #Opening Main Menu
    print("             Welcome to the Hangman Game             ")        
    print("             By: Joey Groves and Sean Raisi          ")
    print("-----------------------------------------------------")
    print()
    print("Second Game: Secret Word Is Randomly Selected")
    print()

    secret_word = choose_secret_word()     #Casts lowercase function onto selected secret word
    length_sw = len(secret_word)        #Stores length of secret word for while loop
    
    print("The secret word has", str(length_sw), "characters.")
    print()
    
    number_of_guesses = 18      #Stores value of no. of guesses user is allowed
    count = 0                   #Counter to increment number of guesses left for user
    letters_guessed = []        #Initialised a list of letters_guessed
    win_Bool = False            #Initialises a Boolean value for while condition
    lose_Bool = False           #Initialises a Boolean value for while condition
    win_count = 0               #Initialises a count for the number of wins
    lose_count = 0              #Initialises a count for the number of loses
    
    while (count != number_of_guesses) and (win_Bool != True) and (lose_Bool != True):          #While Loop will stop running if either: count reaches the number of guesses; the user wins or if the user loses
        print("You have " + str((number_of_guesses) - (count)) +" guesses")     #Variable storing string with number of guesses, the user has left

        try:
            usr_guess_char = input("Guess a character in the secret word: ").lower() #Gets users input
            assert len(usr_guess_char) == 1
            
            if usr_guess_char not in letters_guessed:       #Checks to see if user's guess has been guessed before and appends them to the letters_guessed list
                letters_guessed.append(usr_guess_char)
            else:
                print()
                print("You have already guessed '", str(usr_guess_char), "'")

            tmp_current_guess = get_current_guess(secret_word, letters_guessed)        #Gets the current guess and displays the partially guessed secret word
            print("The partially guessed word is:", tmp_current_guess)
            print()

            if is_secret_guessed(secret_word, letters_guessed) == True:         #Checks to see if the secret word has been guessed by the user; User Wins
                win_Bool = True
                print("It's a win!")
                win_count += 1
                    
        except AssertionError:          #Deals with user string input being greater than length 1
            print()
            print("ERROR: String entered has a length greater than 1, please enter a character")
            print()
        
            
        count += 1      #Increments counter

    if (count == number_of_guesses) and (win_Bool == False):      #Checks to see if user has ran out of guesses; User Loses
        print("You have ran out of guesses\nIt's a loss!")
        print("The word was:", str(secret_word))
        lose_count += 1
        lose_Bool = True
    
    return win_count


def game_stats(numberOfGames): #Author: Joey Groves
    global lose_count           #Global Variable lose_count 
    game_stats_tup = ();        #Game Stats tuple initialised
    lose_count = numberOfGames - win_count  #Calculates loses by subtracting the number of wins from the number of games
    avg_win = win_count/numberOfGames       #Calclulates the average win of the user

    game_stats_tup += (win_count,)          #Adds win count, lose count and average win of user in the tuple
    game_stats_tup += (lose_count,)
    game_stats_tup += (avg_win,)
    
    print()
    print()
    print("-----------------------------------------------------")      #Game Stats Menu
    print("                     GAME STATS                      ")        
    print("-----------------------------------------------------")
    print()
    print("Number of Wins:", str(game_stats_tup[0]), "\nNumber of Loses:", str(game_stats_tup[1]), "\nAverage Wins for the Player:", str(game_stats_tup[2]), "\nNumber of Games Played:", str(numberOfGames))
    print()                         #Prints Number of wins, loses and games as well as the average number of wins
    print()
    print("THANK YOU FOR PLAYING OUR GAME")
    
    
def Main(): #Author: Joey Groves
    global win_count        #Global variable win_count
    win_count = first_game("dog")       #Runs first_game() function and the return value from the outcome of the game is stored 
    numberOfGames = 1               #Initialises the number of games
    
    game_cont = True            #Boolean value for while loop condition    
    while game_cont != False:
        if decision() == 1:         #Gets decision from user by calling the decision() function
            game_cont = True
            numberOfGames += 1          #Increments number of games by 1 if user decides to play another game
            win_count += second_game()  #Global Variable 'win_count' is incremented by the outcome of the function 'second_game()'
        else:
            game_cont = False       #Ends game and while loop if user decides to stop playing
    
    game_stats(numberOfGames)       #Calls the function game_stats(numberOfGames)

    
if __name__ == "__main__":
    Main()
