Hack101: Why Python Is Awesome
-------------------------------

Have you ever tried typing `import this` in python? If you do, the following poem is printed:

> The Zen of Python, by Tim Peters
> 
> Beautiful is better than ugly.
> Explicit is better than implicit.
> Simple is better than complex.
> Complex is better than complicated.
> Flat is better than nested.
> Sparse is better than dense.
> Readability counts.
> Special cases aren't special enough to break the rules.
> Although practicality beats purity.
> Errors should never pass silently.
> Unless explicitly silenced.
> In the face of ambiguity, refuse the temptation to guess.
> There should be one-- and preferably only one --obvious way to do it.
> Although that way may not be obvious at first unless you're Dutch.
> Now is better than never.
> Although never is often better than *right* now.
> If the implementation is hard to explain, it's a bad idea.
> If the implementation is easy to explain, it may be a good idea.
> Namespaces are one honking great idea -- let's do more of those! 

Writing "Pythonic" code is all about simplicity and readability.
Python is equipped with some awesome tools to help you write code in this fashion.

### 0. Pip

Being a powerful language isn't all about the built in tools. 
Python is also great because it has a very nice package manager and plenty of packages to tackle almost any problem.
You can think of pacakges as libraries: large amounts of code that someone else has written to complete a task, and that you can easily use in your code.

For example, lets say I wanted to find all the webpages that are linked to by an url. It's easy with Python! 
Use pip install a library called beautiful soup with:  `pip install beautifulsoup`, 
then we add beautiful soup to our program using `import`, then all we need are the following 9 (!!!!) lines of code:

```python
import httplib2
from BeautifulSoup import BeautifulSoup, SoupStrainer

http = httplib2.Http()
status, response = http.request('http://www.nytimes.com')

for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
    if link.has_attr('href'):
        print link['href']
```
[Source](http://stackoverflow.com/questions/1080411/retrieve-links-from-web-page-using-python-and-beautifulsoup)


We'll see later how we can actually do this in a prettier and shorter way!


One other great thing about python is that it has an interactive mode, which is great for developement. 
Unlike other languages (like C or Java) which need to be compiled before they are run, 
you can write python code in a shell and see the output.
For this tutorial, I will be writing my code in the interactive mode.
I'll also be using IPython, which is a special python shell you can install with (you guessed it) pip.
IPython offers things like tab-completion and basic OS commands. 
We'll see some of its awesome features as we go through the tutorial!

To get started with python, open up your terminal and type `python`.
If to use IPython, simply type `ipython`. If IPython doesn't exist,
you may need to run one `sudo pip install ipython` or `pip install ipython --user`, for your home computer or a Trottier computer respectively. 
If you don't have pip, see here: [http://pip.readthedocs.org/en/stable/installing/](http://pip.readthedocs.org/en/stable/installing/)


### 1. List and Dictonary Comprehension

One common problem in programming is building lists. For example. Let's say we're working in Java and we want a list of all numbers from 1 to 100, squared.
Our first approach may be like this:

```python
array = []
for i in range(1,101):
    array.append(i**2)
```

List comprehensions let us do this all in one expression!
List comprehensions are of the form: ` array = [ <expression> for <variable> in <iterable> ]`.
The code above becomes:

```python
array = [ i**2 for i in range(1,101) ]
```

As *The Zen of Python* states, our goals are readability and beauty. 
The new code is much more readable than the previous version.
Though it may seem insignificant for such a simple list, as lists become more and more complex,
list comprehenisions become infinitely more readable than their for loop-and-append couterparts.

They also have another feature, filters. Let's say we want to change the above list and only have a list of all even numbers from 1 to 100, squared.
We use the syntax `array = [<expression> for <variable> in <interable> if <condition>]`

```python
array = [ i**2 for i in range(1,101) if i%2 == 0]
```

We can also use these comprehensions for dictionaries! Let's say we have a CSV file with Names and Phone Numbers, and we want them in a python dictionary.

The file looks like so:

```
Name1,PhoneNumber1
Name2,PhoneNumber2
.
.
.
```

We can use a dictionary comprehension to grab this really quickly!

First we use list comprehension to get every line in the file and turn it into an array that looks like this:`[ [Name1,PhoneNumber1],[Name2,PhoneNumber2],...]`. 
Since files are iterables, list comprehension is the perfect choice for this! 

Each line looks like: `Name1,PhoneNumber1\n`. 
To turn it into an array like above, we use to methods.
First we use `strip` to get rid of the `\n`, then we use `split(',')` to split it at the comma. So the above array can be made like so:

```python
file = open("numbers.csv","rt")
[ line.strip().split(',') for line in file ]
```

Now, we want to turn this into a dictionary, where each name is used as a key to find each phone number (which is an integer).
We do that in the same way as we did list comprehensions

```
file = open("numbers.csv","rt")
dictionary = { line[0]: int(line[1]) for line in [ line.strip().split(',') for line in file ] }
```

















