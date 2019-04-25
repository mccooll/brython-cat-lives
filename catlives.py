import random

class Catlives:

    def __init__(self):
        self.guessedLetters = []
        self.word = self.selectWord()
        self.wordLetters = list(self.word)
        self.wordLettersRemaining = list(set(self.wordLetters))
        self.answer = [''] * len(self.wordLetters)
        self.numberOfGuesses = 9
        self.alreadyGuessed = False
        self.hasWon = False
        self.hasLost = False

    def loadDictionary(self):
        with open('big_dict.txt') as dictionary:
            words = dictionary.read().split()
        return words

    def selectWord(self):
        words = self.loadDictionary()
        return words[random.randint(0,len(words)-1)]

    def guess(self,letter):
        self.alreadyGuessed = self.checkIfGuessed(input=letter)
        if self.alreadyGuessed == True:
            return True
        self.guessedLetters.append(letter)
        self.guessedLetters.sort()
        self.CorrectorIncorrect = self.checkIfCorrect(letter)
        self.fillInTheBlanks(letter)
        self.hasWon = self.checkForWin()
        self.hasLost = self.checkForLoss()

    def checkIfGuessed(self,input):
        for guessedLetter in self.guessedLetters:
            if input == guessedLetter:
                return True

    def checkIfCorrect(self,input):
        isCorrect = False
        if input in self.wordLetters:
            self.wordLettersRemaining.remove(input)
            isCorrect = True
        else:
            isCorrect = False
        return isCorrect

    def fillInTheBlanks(self,input):
        index=0
        while index < len(self.wordLetters):
            if input == self.wordLetters[index]:
                self.answer[index] = input
            index += 1

    def checkForWin(self):
        if len(self.wordLettersRemaining) == 0:
            return True

    def checkForLoss(self):
        if self.CorrectorIncorrect == False:
            self.numberOfGuesses = self.numberOfGuesses - 1
            if self.numberOfGuesses == 0:
                return True
            return False
