#Hangman.py
#Tim Wu

import string

#setStage will define the underscores + guessing areas for the user. Stage when used in context of this whole program will refer to where letters and underscores are displayed.
def setStage(userstring):

    
    indexposition = 0
    stage = ""

    #Making punctuation and whitespace lists to determine if the indexed string will be require an underscore or not. 
    punctuation = []
    whitespace = []
    
    for character in string.punctuation:
        punctuation.append(character)
    for character in string.whitespace:
        whitespace.append(character)

    for x in range(len(userstring)):

        #If it's a letter then it'll recieve an underscore in its place.
        if ord(userstring[indexposition]) <= 122 and ord(userstring[indexposition]) >= 65:
            stage = stage + " _ "

        if ord(userstring[indexposition]) <= 57 and ord(userstring[indexposition]) >= 48:
            stage = stage + " _ "

        #Checks if indexed string is whitespace or punctuation
        if userstring[indexposition] in whitespace or userstring[indexposition] in punctuation:
            stage = stage + userstring[indexposition]

        
        indexposition += 1
        
    stage = stage.strip()
    return stage

#Defines function to determine where the guessed character is in the hangword.
def indexer(character,list):

    #Utilizes enumerate function to loop over the given list w/ an automatic counter.
    indexes = [x for x, letter in enumerate(list) if letter == character.lower() or letter == character.upper()]

    return indexes


#The game itself.
def guessProcess(hangword,stage):

    #Initializes variables and lists.
    guesses = 6
    
    letters_left = 0

    #newstage is what will be printed after the user enters their guess.
    newstage = stage

    #For every alphabetic character in the word, the letters left to guess will be incremented by one.
    for character in hangword:
        if ord(character) >=65 and ord(character) <=122:
            letters_left += 1
        elif ord(character) >=48 and ord(character) <= 57:
            letters_left += 1

    #Breaks the word to guess up in order to check the presence of a guessed letter    
    hangword_brokenup = []

    for character in hangword:
        hangword_brokenup.append(character)


    #Strips the stage of its whitespace to make it easier to replace underscores w/ guessed letters.
    #Then uses the indexer function to determine where white space that may have previously been in the word was, and puts them back in.
        
    stripped_stage = stage.replace(" ","")
    
    whitespacelocation = indexer(" ",hangword_brokenup)
    
    stage_list = []

    for character in stripped_stage:
        stage_list.append(character)

    
    for index in whitespacelocation:
        stage_list.insert(index," ")
        


    #Punctuation list to check for invalid inputs
    punctuation = []

    for character in string.punctuation:
        punctuation.append(character)

    wronganswers = []
    
    #Infinite loop. Condition doesn't matter here because the loop break MUST happen at the end of the loop regardless of the condition.
    while 1 == 1:
    
        #Information + user prompt
        print("You currently have",guesses,"tries.")
        print("Your current list of wrong letters is:",(", ").join(wronganswers))
        userguess = input("Enter your guess.")
        
        #Checks the user's input against various lists, variables, etc.

        if len(userguess) > 1:
            print("\n")
            print("Your guess must be only one letter long!")
            print("\n")
            
        elif userguess in string.punctuation:
            print("\n")
            print("Don't try to try and be clever. Punctuation is already given to you.")
            print("\n")
            print(newstage)
            print("\n")

        elif userguess in string.whitespace:
            print("\n")
            print("Spaces are not a valid guess.")
            print("\n")
            print(newstage)
            print("\n")

        elif userguess in wronganswers:
            print("\n")
            print("That letter has already been incorrectly guessed.")
            print("\n")
            print(newstage)
            print("\n")

        elif userguess.lower() in newstage or userguess.upper() in newstage:
            print("\n")
            print("That letter has already been correctly guessed!")
            print("\n")
            print(newstage)
            print("\n")
        
        #Process for a correct guess.
        elif userguess.lower() in hangword_brokenup or userguess.upper() in hangword_brokenup:
            
            #Calls the indexer function to determine the location of the guessed character.
            
            indexes = indexer(userguess,hangword_brokenup)

            #Replaces each index spot's underscore w/ the corresponding guessed letter.
            for spot in indexes:
                if userguess.lower() == hangword[spot]:
                    stage_list[spot] = userguess.lower()
                    
                elif userguess.upper() == hangword[spot]:
                    stage_list[spot] = userguess.upper()

            #Sets the newstage as the now updated stage_list.
            
            newstage = (" ").join(stage_list)
            print("\n")
            print("Your character is in the word!")
            print("\n")
            print(newstage)
            print("\n")

            #Updates the letters left based on how many times it appears in the character.
            letters_left = letters_left - len(indexes)

        #Process for if user enters an incorrect guess
        elif userguess not in hangword_brokenup:
            guesses -= 1
            wronganswers.append(userguess)
            
            print("\n")
            print("That letter is not in the word! Minus one try!")
            print("\n")
            print(newstage)
            print("\n")

        #As stated in the line 74 comment - Condition for loop doesn't matter, much easier to make the loop break at the end depending on conditions so that it doesn't loop again.
        if letters_left == 0:
            break
        elif guesses == 0:
            break

    #Returns game outcome
        
    if guesses == 0:
        return False
    
    elif letters_left == 0:
        return True
    
    


#Main function. 
def main():

    print("Welcome to this program. Hangman is a game where you attempt to guess a word by guesing letters. You have limited choices, and if you use them all up, you fail!")
    
    print("\n")
    
    print("After this, you will be prompted to enter a word to be guessed. Then, underscores will replace the letters.")
    print("For example, the word \"Hello\" will show up as \"_ _ _ _ _\".")
    print("Have a friend enter the phrase if you want to be surprised or have a challenge!")
    
    print("\n")
    
    print("The user must guess characters of a word in an attempt to fill in the blanks to reach the full word.")
    print("VALID INPUTS WILL INCLUDE: Letters AND digits.")
    
    print("\n")
    
    print("When you enter a correct answer, the underscore corresponding to the letter in the word will be replaced with that letter.")
    print("For example, when you enter \"h\" as your guess for the word \"Hello\", you will see \"H _ _ _ _\".")
    
    print("\n")
    
    print("When you enter an incorrect answer, you will lose one try, and be prompted to enter another guess.")
    print("The only way you'll be penalized for an incorrect answer is you'll lose a try, nothing more!")
    print("You will be allowed to have 6 incorrect guesses in total.")
    
    print("\n")
    
    print("Invalid inputs include: Whitespace, Punctuation.")
    print("So for example, guesses such as: \" \",\"-\", will not be accepted.")
    print("You will be provided with whitespace and punctuation, so there is no need to try and guess those. You only need to worry about guessing the word correctly!")

    print("\n")
    
    print("If you correctly guess the word, you will win!")
    print("However, if you fail to guess the word by using up all your guesses, you will lose!")

    print("\n")
    print("If you would like to read more about Hangman, you can go to this link in your browser: https://en.wikipedia.org/wiki/Hangman_(game) ")
    print("\n")
    
    print("\n")
    
    hangword = input("Enter the word to be guessed.")
            

    print("\n")
    print("------")
    print("\n")

    hangstage = setStage(hangword)

    print("You will have 6 chances to guess.")
    print("\n")
    print("Your word has a total of ", hangstage.count("_") , "letters.")
    print("Your word is broken up into a total of", hangword.count(" ") + 1, "word(s).")
    print(hangstage)
    print("\n")

        

    #Returns False if the user ran out of guesses or True if they got the word correct.
    win_status = guessProcess(hangword,hangstage)

    #Will prompt user to enter whether they would like to run the program again or not.
    if win_status == False:
        print("\n")
        print("------")
        print("\n")
        continue_prompt = input(("You've run out of guesses. The correct word was:", hangword, "Would you like to try again? (Y/N)"))
        print("\n")
        if continue_prompt.lower() == "y":
            print("Roger that. Running the program again!")
            print("\n")
            main()
        else:
            print("Thanks for playing!")

    elif win_status == True:
        print("\n")
        print("------")
        print("You win!")
        print("\n")
        continue_prompt = input(("Would you like to try again? (Y/N)"))
        print("\n")
        if continue_prompt.lower() == "y":
            print("Roger that. Running the program again!")
            print("\n")
            main()
        else:
            print("Thanks for playing!")
    


    

main()
