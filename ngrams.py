import re




class NGrams:

    def __init__(self, n):
        self.n = n
        self.ngrams = {} # ngram[-1] is the "successor"

    def read_file(self, filename):
        with open(filename) as file:
            t_line = []
            too_short = False
            for line in file:
                line = line.strip()
                t_line += self.handle_interpunction(line).split(' ')
                if too_short:
                    continue
                self.extract_ngrams_from_line(t_line)
                t_line = []
        self.filter()

    def filter(self):
        keys_to_remove = []
        for key, value in self.ngrams.items():
            for key_, value_ in self.ngrams.items():
                if key.words == key_.words and key.successor != key_.successor:
                    keys_to_remove.append(key_ if value > value_ else key)
        for key in keys_to_remove:
            self.ngrams.pop(key)


    def extract_ngrams_from_line(self, line):
        for i in range(len(line)):
            ngram = []
            for j in range(i, min(self.n+i, len(line))):
                ngram.append(line[j])
            ngram = NGram(ngram)
            self.ngrams.update({ngram:self.ngrams.get(ngram, 0)+1})
        

    def handle_interpunction(self, s):
        # Inserts whitespace before each punctuation mark so it gets dealt with like a word
        s = re.sub('([.,!?()])', r' \1 ', s)
        s = re.sub('\s{2,}', ' ', s)
        return s
        
class NGram:

    def __init__(self, words):
        self.successor = words[-1]
        self.words = words[:-1]

    def __str__(self):
        return str(self.words + [self.successor])
    
    __repr__ = __str__    


