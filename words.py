#!/usr/bin/python
from random import randint

with open("/usr/share/dict/words","rt") as f:
    words = [ w.strip() for w in f ]
    random_words = [ words[randint(0,len(words))] for i in range(0,100)]

print random_words
