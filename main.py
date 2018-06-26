from ngrams import *

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
    - Class NGram, List unhashable
    - Hash ngram only based on internal list, else dict is useless
"""


if __name__=='__main__':
    ngrams = NGrams(n=10)
    ngrams.read_file('./testdata/heise_ldap.txt')
    print(ngrams.predict_next_word(['Sie',  'liegt',  'zurzeit']))