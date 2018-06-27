import re




class NGrams:

    def __init__(self, n):
        self.n = n
        self.ngrams = [{} for i in range(n+1)] # ngram[-1] is the "successor"

    def read_file(self, filename):
        with open(filename, encoding='utf-8') as file:
            t_line = []
            for line in file:
                line = line.strip()
                t_line += self.handle_interpunction(line).split(' ')
                if len(t_line) <= self.n:
                    continue
                for i in range(2, self.n+1):
                    self.extract_ngrams_from_line(t_line, i)
                t_line = []
        self.filter()

    def filter(self):
        for item in self.ngrams:
            keys_to_remove = []
            for key, value in item.items():
                for key_, value_ in item.items():
                    if key.words == key_.words and key.successor != key_.successor:
                        if key_ not in keys_to_remove and value > value_:
                            keys_to_remove.append(key_)
                        elif key not in keys_to_remove:
                            keys_to_remove.append(key)
            for key in keys_to_remove:
                item.pop(key)


    def extract_ngrams_from_line(self, line, n):
        for i in range(len(line)):
            ngram = []
            for j in range(i, min(n+i, len(line))):
                ngram.append(line[j])
            ngram = NGram(ngram)
            self.ngrams[n].update({ngram:self.ngrams[n].get(ngram, 0)+1})

    def test(self):
        # General testing stuff
        print(f'Len: {len(self.ngrams)}')
        for ngrams in self.ngrams:
            for key, _ in ngrams.items():
                print(key)
                print(id(ngrams))
                break
       
        print(self.ngrams[-1])
        
    def predict_next_word(self, words):
        if len(words) >= self.n:
            words = words[1-(self.n):len(words)]
        n = len(words) + 1
        
        # TODO Map currently useless, O(1) Searching not used
        for i in range(n, 1, -1):
            ngrams = self.ngrams[i]
            print(ngrams)
            for key, _ in ngrams.items():
                if key.words == words:
                    return key.successor

    def finish_sentence(self, words):
        prediction = self.predict_next_word(words)
        while prediction != None:
            if prediction == None:
                print(words)
                break
            words += [prediction]
            prediction = self.predict_next_word(words)
        return words
        

    def handle_interpunction(self, s):
        # Inserts whitespace before each punctuation mark so it gets dealt with like a word
        s = re.sub('([.,!?()])', r' \1 ', s)
        s = re.sub('\s{2,}', ' ', s)
        return s
        
class NGram:

    def __init__(self, words):
        self.successor = words[-1]
        self.words = words[:-1]
        self.i = 0

    def __str__(self):
        return str(self.words + [self.successor])
    
    def __eq__(self, other):
        return self.words == other.words and self.successor == other.successor

    def __hash__(self):
        val = 0
        for word in self.words:
            val += word.__hash__()
        return val

    __repr__ = __str__    


