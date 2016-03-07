# HANGMAN game
# A Hangman game!

import json
import re
import socket
import offlinewords

# Wordnik API
from wordnik import *
apiUrl = 'http://api.wordnik.com/v4'
apiKey = '3c50e7b5e1e604f09956ea7cca5010850216618e67e05bf76'
client = swagger.ApiClient(apiKey, apiUrl)
wordsApi = WordsApi.WordsApi(client)

def getWordOnline(minCorpus, maxCorpus, minDictionary, maxDictionary, minL, maxL):
    randomWord = wordsApi.getRandomWord(includePartOfSpeech='noun',
                                        excludePartOfSpeech='conjunction',
                                        hasDictionaryDef='true',
                                        minCorpusCount=minCorpus,
                                        maxCorpusCount=maxCorpus,
                                        minDictionaryCount=minDictionary,
                                        maxDictionaryCount=maxDictionary,
                                        minLength=minL,
                                        maxLength=maxL).word
    if re.search("[\s|\-]", randomWord):
        return getWordOnline(minCorpus, maxCorpus, minDictionary, maxDictionary, minL, maxL)
    else:
        return randomWord        
        
def new_game(randomWord):
    global answer, answerWithSpace, word, guesses, misses, notGuessed
    guesses = ""
    misses = ""
    word = ""
    answer = notGuessed = randomWord.upper()
    answerWithSpace = answer.replace(""," ")[1:-1]
    for ch in range (0, len(answer)):
        word += "_ "
    print "Let's play HANGMAN! \n"
    guess()

def normal_game():
    if hasConnection:
        randomWord = getWordOnline(10000, -1, 1, -1, 7, 12)
    else:
        randomWord = offlinewords.get_normal_word()
    new_game(randomWord)

def hard_game():
    if hasConnection:
        randomWord = getWordOnline(1, 2000, 1, -1, 12, -1)
    else:
        randomWord = offlinewords.get_hard_word()
    new_game(randomWord)

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
        start()
    elif len(misses) == 6:
        printResults()
        word = answer
        print "You lost! - the answer was " + word + "\n"
        #print definition of word
        print "\n\n"
        start()
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

def start():
        whatNow = raw_input("Enter 'n' to play on normal difficulty or 'd' for a difficult word: ")
        if whatNow == "n":
            print "\n"
            normal_game()
        elif whatNow == "d":
            print "\n"
            hard_game()
        # elif whatNow == "q":
        #    exit(0)
        else:
            print "Invalid Input.\n"
            start()

def check_connection():
    try:
        REMOTE_SERVER = "www.google.com"
        # see if we can resolve the host name -- tells us if there is a DNS listening
        host = socket.gethostbyname(REMOTE_SERVER)
        # connect to the host -- tells us if the host is actually reachable
        s = socket.create_connection((host, 80), 2)
        print "Connection found \n"
        return True
    except:
        pass
    print "No connection \n"
    return False


def main():
    global hasConnection
    print "Checking for internet connection... ",
    hasConnection = check_connection()
    start()

main()
