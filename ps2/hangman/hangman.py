import random
import string

WORDLIST_FILENAME = "/Users/vihaandas/Desktop/MIT Python/ps2/hangman/words.txt"


def load_words():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    return random.choice(wordlist)

wordlist = load_words()

def is_word_guessed(secretWord, lettersGuessed):
    check = True

    for letter in secretWord:
        if letter not in lettersGuessed:
            check = False

    return check

def get_guessed_word(secretWord, lettersGuessed):
    guessedWord = ""
    for letter in secretWord:
        if letter in lettersGuessed:
            guessedWord += letter
        else:
            guessedWord += " _ "
    return guessedWord



def get_available_letters(lettersGuessed):
    allLetters = string.ascii_lowercase
    lettersAvailable = ""
    for letter in allLetters:
        if letter not in lettersGuessed:
            lettersAvailable += letter
    return lettersAvailable
    
    

def hangman(secret_word):
    wordLength = len(secret_word)
    guessesLeft = 6
    guess = ""
    lettersGuessed = ""
    print("Welcome to Hangman!")
    print("I am thinking of a letter that is " + str(wordLength) + " letters long")

    while guessesLeft > 0:
        print("You have " + str(guessesLeft) + " guesses left")
        lettersAvailable = get_available_letters(lettersGuessed)
        print("Available letters: " + lettersAvailable)
        guess = input("Guess a letter: ")
        lettersGuessed += guess
        for letter in secret_word:
            if guess == letter:
                check = True
                break
        else:
            check = False
        if check == True:
            print("Good guess!")
        elif check == False:
            print("That letter is not in the word")
            guessesLeft -= 1
        print(get_guessed_word(secret_word, lettersGuessed))

    check2 = is_word_guessed(secret_word,lettersGuessed)
    if check2 == True:
        print("You won! The word was " + secret_word)
    elif check2 == False:
        print("You lost, the word was " + secret_word)

def match_with_gaps(my_word, other_word):
    match = True
    for letter in my_word:
        if letter not in other_word:
            match = False

    return match



def show_possible_matches(my_word):
    matches = []
    for word in wordlist:
        check = match_with_gaps(my_word,word)
        if check == True:
            matches += word
    if len(matches) == 0:
        matches += "No matches"

    return matches



def hangman_with_hints(secret_word):
    wordLength = len(secret_word)
    guessesLeft = 6
    guess = ""
    lettersGuessed = ""
    print("Welcome to Hangman!")
    print("I am thinking of a letter that is " + str(wordLength) + " letters long")

    while guessesLeft > 0:
        print("You have " + str(guessesLeft) + " guesses left")
        lettersAvailable = get_available_letters(lettersGuessed)
        print("Available letters: " + lettersAvailable)
        guess = input("Guess a letter: ")
        lettersGuessed += guess
        check = True
        if guess == "*":
            check = True
            hints = show_possible_matches(get_guessed_word(secret_word, lettersGuessed))
            print(hints)
        else:
            for letter in secret_word:
                if guess == letter:
                    check = True
                    break
        if check == True:
             print("Good guess!")
        elif check == False:
             print("That letter is not in the word")
             guessesLeft -= 1
        print(get_guessed_word(secret_word, lettersGuessed))

    check2 = is_word_guessed(secret_word,lettersGuessed)
    if check2 == True:
        print("You won! The word was " + secret_word)
    elif check2 == False:
        print("You lost, the word was " + secret_word)

if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)