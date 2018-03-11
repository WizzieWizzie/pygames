SECRET_WORD = "empress"
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
NUMBER_OF_ATTEMPTS = 10


def isWordGuessed(word, lettersGuessed):
    numberOfLettersGuessed = 0
    for i, c in enumerate(word):
        if c in lettersGuessed:
            numberOfLettersGuessed += 1
    return numberOfLettersGuessed == len(word)


def getWordToDisplay(word, lettersGuessed):
    index = 0
    wordToShow = ['_ '] * len(word)

    for i, c in enumerate(word):
        index += 1
        if c in lettersGuessed:
            wordToShow.insert(index - 1, c)
        else:
            wordToShow.insert(index - 1, ' _ ')
        wordToShow.pop(index)
        if index == len(word):
            return ''.join(str(letter) for letter in wordToShow)


def getRemainingLetters(lettersGuessed):
    return ''.join(c for c in ALPHABET[:] if c not in lettersGuessed)


def hangman(word):
    lettersGuessed = []
    guessesLeft = NUMBER_OF_ATTEMPTS
    wordGuessed = False

    while 0 < guessesLeft <= NUMBER_OF_ATTEMPTS and wordGuessed is False:
        if word == getWordToDisplay(word, lettersGuessed):
            wordGuessed = True
            break
        print 'You have ' + str(guessesLeft) + ' guesses left.'
        print 'Choose one from the following letters: ' + getRemainingLetters(lettersGuessed)
        guess = raw_input('Please guess a letter: ').lower()
        if guess in word:
            lettersGuessed.append(guess)
            print 'The letter is in the word: ' + getWordToDisplay(word, lettersGuessed)
        else:
            lettersGuessed.append(guess)
            guessesLeft -= 1
            print 'The letter is not in the word: ' + getWordToDisplay(word, lettersGuessed)

    if wordGuessed:
     print ('Congratulations, you guessed it!')
    elif guessesLeft == 0:
     print 'No more guesses available. The word was ' + word


secretWord = SECRET_WORD
hangman(secretWord)

# Exercises
# 1. Create an array of words and choose a random word for the game
# 2. Read the words from a text file instead of hard-coding them in the array
# 3. Try to use the same guess multiple times? What happens? If someone tries the same letter multiple times, print an appropriate message.
