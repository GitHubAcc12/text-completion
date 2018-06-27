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
    - Print autocompletion to file
    - Test with huge trainingdataset
"""


if __name__=='__main__':
    ngrams = NGrams(n=10)
    ngrams.read_file('./testdata/heise_ldap.txt')
    result = ngrams.finish_sentence(['Sie',  'liegt',  'zurzeit'])
    print(f' Result: {result}')
    # ngrams.test()