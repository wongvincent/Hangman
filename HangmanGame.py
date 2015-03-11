# HANGMAN game
# An offline Hangman game against the computer!

# Note: this uses an offline version of Webster's Dictionary
# Check out Wordnik API for an online version of a dictionary


#import webster dictionary module/lib

def new_game():
    global answer, word, guesses, misses
    #clear guesses array
    #clear misses array
    #get_word_from_lib store in answer
    #for loop create blanks matching letters in answer, store in word
    print "Let's play! \n"
    print word
    guess()

def guess():
    global guesses, misses
    letter = raw_input("Enter a letter: ")
    #if letter in guesses or misses
        print "You have already tried this letter.\n"
    #elif letter in answer
        #add to guesses
        #replace '_' with letter (might make helper func)
    #else:
        #add to misses
    check_status()

def check_status():
    #if word does not contain '_'
        printHangman()
        print "You win!\n"
        #print definition of word
        finished()
    #elif misses.length == 6
        global word
        word = answer
        printHangman()
        print "You lost!\n"
        #print definition of word
        finished()
    #else
        guess()

def printHangman():
    #print hangman[misses.length]
    #print word
    #print guesses
    #print misses

def finished()
        whatNow = raw_input("Enter 'n' to play again or q to quit")
        #if whatNow == "n"
            new_game()
        #elif whatNow == "q"
            exit(0)
        #else
            print "Invalid Input."
            finished()

new_game()

#see: http://en.wikipedia.org/wiki/Hangman_%28game%29#Example_game
