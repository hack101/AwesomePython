#!/usr/bin/python
from random import sample

with open("/usr/share/dict/words","rt") as f:
    words = [ w.strip() for w in f ]
    random_words = [words[i] for i in sample(xrange(len(words)),100)]

print random_words
