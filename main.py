from ngrams import *





if __name__=='__main__':
    ngrams = NGrams(n=10)
    ngrams.read_file('./testdata/heise_ldap.txt')
    print(ngrams.ngrams)