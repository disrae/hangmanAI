import string
import csv


def initWords():
    with open('words.csv') as f:
        words = []
        for row in csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE):
            words += row
    return words


def containsCharsFoundSoFar(word: str) -> bool:
    doesContainAllChars = all(char in word for char in charsFound)
    return doesContainAllChars


def wordIsRightLength(word: str) -> bool:
    return len(word) == length


def renderProgress() -> None:
    for char in wordToGuess:
        if char in charsGuessed:
            print(char, ' ', end='')
        else:
            print('_ ', end='')
    print('     tries remaining: ', triesRemaining, '\n')


def getMaxChar(counts: dict) -> str:
    for char in charsGuessed:
        del counts[char]
    v = list(counts.values())
    k = list(counts.keys())
    return k[v.index(max(v))]


def makeGuess() -> str:
    ''' 
        count frequency of characters in possible 
        words, -> return max probability character
    '''
    # new dictionary of alphabet
    charCount = dict.fromkeys(string.ascii_lowercase, 0)
    # iterate all words: checking length matches and chars contained
    for word in listOfWords:
        if wordIsRightLength(word) and containsCharsFoundSoFar(word):
            for char in word:
                char = char.lower()
                try:
                    charCount[char] += 1
                except:
                    pass
    char = getMaxChar(charCount)
    print('guessed ', char)
    charsGuessed.append(char)
    return char


def verifyGuess(c: str):
    numFound = wordToGuess.count(c)
    # if no match decrement tries
    if numFound == 0:
        global triesRemaining
        triesRemaining -= 1
    else:
        charsFound.append(c)


# CONSTANTS/GLOBALS
triesRemaining = 5
listOfWords = initWords()
charsGuessed = []
charsFound = []

# main
wordToGuess = input('input word for hangman: ')
length = len(wordToGuess)

while triesRemaining > 0:
    char = makeGuess()
    verifyGuess(char)
    renderProgress()
    if len(set(wordToGuess)) == len(charsFound):
        print('ᕙ(⇀‸↼‶)ᕗ *~~* WINNER *~~* ᕙ(⇀‸↼‶)ᕗ\n')
        break
