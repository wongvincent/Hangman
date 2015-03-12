# HANGMAN game
# An offline Hangman game against the computer!

# Note: this uses an offline version of Webster's Dictionary
# Check out Wordnik API for an online version of a dictionary


#import webster dictionary module/lib

def new_game():
    global answer, answerWithSpace, word, guesses, misses, notGuessed
    guesses = ""
    misses = ""
    word = ""
    #get_word_from_lib store in answer
    answer = notGuessed =  "hangman".upper() #just for testing
    answerWithSpace = answer.replace(""," ")[1:-1]
    for ch in range (0, len(answer)):
        word += "_ "
    print "Let's play HANGMAN! \n"
    guess()

def guess():
    global guesses, misses, notGuessed, word
    letter = raw_input("Enter a letter: ").upper()
    if len(letter) != 1 or not letter.isalpha():
        print "Invalid guess.\n"
        guess()
    elif letter in guesses or letter in misses:
        print "You have already tried this letter.\n"
        guess()
    elif letter in answer:
        notGuessed = notGuessed.replace(letter, "");
        guesses += letter
        word = answerWithSpace
        for ch in notGuessed:
                word = word.replace(ch, "_")
        check_status()
    else:
        misses += letter
        check_status()

def check_status():
    global word
    if not "_" in word:
        printResults()
        word = answer
        print "You win!\n"
        #print definition of word
        print "\n\n"
        finished()
    elif len(misses) == 6:
        printResults()
        word = answer
        print "You lost! - the answer was " + word + "\n"
        #print definition of word
        print "\n\n"
        finished()
    else:
        printResults()
        guess()

def printResults():
    printHangman()
    print "Word: " + word
    print "Guess: " + guesses.replace("",",")[1:-1].lower()
    print "Misses: " + misses.replace("",",")[1:-1].lower()
    print "\n"

def printHangman():
    i = len(misses)
    if i==0:
        print "   _____"  
        print "  |     |"  
        print "  |"  
        print "  |"  
        print "  |"  
        print "  |"  
        print "  |"  
        print "-------"  
    if i==1:
        print "   _____"  
        print "  |     |"  
        print "  |     0"  
        print "  |"  
        print "  |"  
        print "  |"  
        print "  |"  
        print "-------"  
    if i==2:
        print "   _____"  
        print "  |     |"  
        print "  |     0"  
        print "  |     |"  
        print "  |     |"  
        print "  |"  
        print "  |"  
        print "-------"  
    if i==3:
        print "   _____"  
        print "  |     |"  
        print "  |     0"  
        print "  |    \\|"  
        print "  |     |"  
        print "  |"  
        print "  |"  
        print "-------"  
    if i==4:
        print "   _____"  
        print "  |     |"  
        print "  |     0"  
        print "  |    \\|/"  
        print "  |     |"  
        print "  |"  
        print "  |"  
        print "-------"  
    if i==5:
        print "   _____"  
        print "  |     |"  
        print "  |     0"  
        print "  |    \\|/"  
        print "  |     |"  
        print "  |    /"  
        print "  |"  
        print "-------"  
    if i==6:
        print "   _____"  
        print "  |     |"  
        print "  |     0"  
        print "  |    \\|/"  
        print "  |     |"  
        print "  |    / \\ "  
        print "  |"  
        print "-------"  

def finished():
        whatNow = raw_input("Enter 'n' to play again or q to quit: ")
        if whatNow == "n":
            print "\n\n"
            new_game()
        elif whatNow == "q":
            exit(0)
        else:
            print "Invalid Input.\n"
            finished()

new_game()
