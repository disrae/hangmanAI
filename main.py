import string
import csv

# TODO: augment chars found to track position


def initWords():
    with open('words.csv') as f:
        words = []
        for row in csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE):
            words += row
    return words


def containsCharsFoundSoFar(word: str) -> bool:
    doesContainAllChars = all(char in word for char in charactersFound)
    return doesContainAllChars


def renderProgress() -> None:
    for char in charactersFound:
        if char:
            print(char, ' ', end='')
        else:
            print('_ ', end='')
    print('     tries remaining: ', triesRemaining, '\n')


def getMaxChar(counts: dict) -> str:
    inverse = [(value, key) for key, value in counts.items()]
    return max(inverse)[1]


def populateFreqCount(charCount: dict):
    # iterate over all words: checking length matches and chars contained
    print('helllooo?')
    for word in possibleWords:
        if wordIsRightLength(word) and containsCharsFoundSoFar(word):
            for char in word:
                char = char.lower()
                try:
                    charCount[char] += 1
                except:
                    pass


def makeGuess() -> str:
    ''' 
        count frequency of characters in possible 
        words, -> return max probability character
    '''
    # init new dictionary of alphabet freq count
    charCount = dict.fromkeys(string.ascii_lowercase, 0)
    populateFreqCount(charCount)
    guess = getMaxChar(charCount)
    print('guessed ', guess)
    charactersGuessed[guess] = guess
    return guess


def verifyGuess(guess: str):
    numFound = wordToFind.count(guess)
    print(numFound)
    # if no match decrement tries
    if numFound == 0:
        global triesRemaining
        triesRemaining -= 1
    else:
        for i, char in enumerate(wordToFind):
            if wordToFind[i] == guess:
                print('found at pos', i, 'character:', char)
                charactersFound[i] = guess
                numFound += 1
    print(triesRemaining)


def identifyPositions():
    '''
    inputs: wordToFind, englishDictionary, charsFound
    purpose: find words in dict with charsFound in same positions; count alphabet freq; ret max char
    output: dict of positions and char
    '''


# Main
triesRemaining = 6
# Members.
possibleWords = initWords()
wordToFind = input('input word for hangman: ')
charactersGuessed = {}
charactersFound = [None] * len(wordToFind)
numFound = 0

# Filter possibleWords.
while (triesRemaining > 0):
    for i, currentWord in enumerate(possibleWords):
        lengthsDontMatch = len(currentWord) != len(wordToFind)
        charsFoundDontMatch = False
        for position, character in charactersGuessed.items():
            print(currentWord[position], '!=', character)
            if currentWord[position] != character:
                charsFoundDontMatch = True

        if lengthsDontMatch or charsFoundDontMatch:
            print('del words')
            del possibleWords[i]

    # Count highest frequency character.
    characterFrequencies = {}
    for word in possibleWords:
        for char in word:
            char = char.lower()
            try:
                characterFrequencies[char] += 1
            except:
                characterFrequencies[char] = 1
    guess = getMaxChar(characterFrequencies)
    print('the guess is:', guess)
    verifyGuess(guess)
    renderProgress()
    if len(set(wordToFind)) == numFound:
        print('ᕙ(⇀‸↼‶)ᕗ *~~* WINNER *~~* ᕙ(⇀‸↼‶)ᕗ\n')
        break
