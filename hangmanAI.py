import string
import csv


def initWords(length):
    with open('smallDictionary.csv') as f:
        words = []
        for word in csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE):
            if len(word[0]) == length:
                words += word

    return words


def generateNewPossibleWords():
    newPossibleWords = []
    for i, currentWord in enumerate(possibleWords):

        charsFoundPositionsMatch = True
        for position, character in enumerate(charactersFound):
            shouldCheckCharacter = character != '_'
            if shouldCheckCharacter and currentWord[position] != character:
                charsFoundPositionsMatch = False

        if charsFoundPositionsMatch:
            newPossibleWords.append(currentWord)

    return newPossibleWords


def countCharacters(possibleWords):
    characterFrequencies = {}
    for word in possibleWords:
        for char in word:
            char = char.lower()
            try:
                characterFrequencies[char] += 1
            except:
                characterFrequencies[char] = 1

    return characterFrequencies


def maxFrequencyNovelCharacter(characterFrequency, charactersGuessed):
    # Remove previous guesses.
    for char in charactersGuessed:
        try:
            del characterFrequency[char]
        except:
            pass

    # Count Frequencies.
    invertedFrequencies = [(freq, char)
                           for char, freq in characterFrequency.items()]
    return max(invertedFrequencies)[1]


def populateCharactersFound(wordToFind, guess):
    found = False

    for i, char in enumerate(wordToFind):
        if char == guess:
            charactersFound[i] = guess
            found = True


# Variables.
wordToFind = input('\ninput word for hangman: ')
possibleWords = initWords(len(wordToFind))

charactersGuessed = []
charactersFound = ['_'] * len(wordToFind)
attempt = 0

while ('_' in charactersFound):
    attempt += 1
    print('\nattempt:', attempt)

    possibleWords = generateNewPossibleWords()
    # print('Guessing character from:\n', possibleWords)
    if len(possibleWords) == 1:
        print('Guessing the word is:', possibleWords[0])
        break

    characterFrequency = countCharacters(possibleWords)

    guess = maxFrequencyNovelCharacter(characterFrequency, charactersGuessed)
    charactersGuessed.append(guess)

    populateCharactersFound(wordToFind, guess)
    print('guessed', guess, ', word so far', charactersFound)
