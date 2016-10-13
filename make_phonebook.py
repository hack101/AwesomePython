import csv
import names
from random import randint

def number():
    digits = [str(randint(0,9)) for _ in xrange(7)]
    return '514'+''.join(digits)

with open('phonebook.csv', 'w+') as f:
    w = csv.writer(f)
    for _ in xrange(20):
        w.writerow([names.get_full_name(), number()])
