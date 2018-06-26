import re

"""
Dumb:
    - For each word: save all predecessing n-grams and their frequency
    - dict of string, array of strings --> key=word, array of n-grams
    - dict of string, array of numbers --> key=word, array of frequencies

Maybe smarter:
    - For each n-sequence of words, save all successing (single) words and their frequency
    - dict of array of strings, array of strings --> key=ngram, value=successors
    - dict of array of strings, array of numbers --> key=ngram, value=frequencies of successors
TODO
    - Interpunction = ?
    - save interpunction like words --> ngrams, frequency
"""


class NGrams:

    def __init__(self, n):
        self.n = n
        self.ngrams = {}
        self.frequencies = {}

    def read_file(self, filename):
        # Handle lines with less than n words
        with open(filename) as file:
            for line in file:
                self.extract_ngrams_from_line(line)

    def extract_ngrams_from_line(self, line):
        ngrams = []
        line = self.handle_interpunction(line).split(' ')
        frequencies = [0] * (len(line)-20)
        for i in range(0, len(line), self.n):
            return
            
            
    def handle_interpunction(self, s):
        # Inserts whitespace before each punctuation mark so it gets dealt with like a word
        s = re.sub('([.,!?()])', r' \1 ', s)
        s = re.sub('\s{2,}', ' ', s)
        return s
        

