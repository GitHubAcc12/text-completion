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


def is_punctuation_mark(sign):
    return sign in ['.', ',', '-', '!', '?', '/', '(', ')']

def clear_file(filename):
    with open(filename, 'w') as file:
        return

def write_to_file(words, filename='output.txt'):
    clear_file(filename)
    with open(filename, 'a') as file:
        towrite = ''
        for i in range(len(words)-1):
            towrite += words[i]
            if not is_punctuation_mark(words[i+1]) and (not words[i] == '"' or words[i+1] == '"'):
                towrite += ' '
            if len(towrite) > 100 and words[i] in ['.', ',', '!', '?']:
                file.write(towrite)
                towrite = ''
        towrite += words[-1]
        file.write(towrite)



if __name__=='__main__':
    ngrams = NGrams(n=10)
    ngrams.read_file('./testdata/heise_ldap.txt')
    result = ngrams.finish_sentence(['Sie'])
    write_to_file(result)
    # ngrams.test()