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


We'll learn about list comprehension which actually lets you do this in a prettier and shorter way!


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
We do that in the same way as we did list comprehensions:
`{ <expression in the form 'key: value'> for <value> in <iterable> }`. 

```python
file = open("numbers.csv","rt")
dictionary = { line[0]: int(line[1]) for line in [ line.strip().split(',') for line in file ] }
file.close()
```

Here, the interable in our comprehension is another comprehension! We can also have a filter, like in list comprehensions.

```python
file = open("numbers.csv","rt")
# I really don't like Dave...
dictionary = { line[0]: int(line[1]) for line in [ line.strip().split(',') for line in file ] if line[0] != "Dave" }
file.close()
```

If you're interested in going beyond the tutorial, this would be a good place to learn about [context managers](https://docs.python.org/2/reference/compound_stmts.html#the-with-statement)!

###### Challenges

Now that we know about list comprehensions, let's do a couple challenges! They get harder as you go down the list. Try one out now!

1. (Project Euler #1): If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000. -- Try to do this in one line. You may need to use Python's `sum` function, which works like so:
`sum([1,2,3]) -> 6` 
2. [Here](https://github.com/hack101/AwesomePython/blob/master/words.txt) is a list of some random words. 
Take this list (you can copy and paste it) and create a new list using dictionary comprehension which only has words that start with a vowel. 
*Note:* This list of words was created using a list comprehension! Click [here](https://github.com/hack101/AwesomePython/blob/master/words.py) if you are interested in seeing how.
3. Try using list comprehension to flatten a list. For example, if `l=[ [1,2], [3,4], [5,6] ]`, we want to turn it into `[ 1, 2, 3, 4, 5, 6]`.
4. (FizzBuzz) Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”. -- Try to do this in one line. You will need to use [join](http://www.tutorialspoint.com/python/string_join.htm).

### 2. Lambda Expressions

In python, functions are variables. 
Sometimes we want to use them without defining them first, and sometimes we want to define them without a full `def` statement. 
Lambda expressions are how we do that. 

They have the following syntax:

```python
lambda <arguments>: <what to return from arguemnts>
```

For example, the function `lambda x: x+2` is equivalent to 
```python
def function(x):
    return x+2
```

And `val` has the same value in both of these cases:

```python
val = (lambda x: x+2)(5)

def function(x):
    return x+2

val = function(5)
```

"This is cool", you may be thinking, "but why?". 
One of the primary uses of lambda expressions is that we can use functions as arguments without defining them. 

For example, when sorting a list, you may not want to use the standard sorting built in to python.
The list sort method take a keyword argument `key`. 
The value of `key` should be a function that tells the sorting method what to sort by.

Maybe you want to do a reverse sort of a list.

```python
list = [ 3, 5, 2, 6, 10, 1 ]
list.sort()
print list # this prints [1, 2, 3, 5, 6, 10]

# Now let's use key to do a reverse sort.
# We tell sort that it should sort each element by its negative value
list.sort(key=lambda x: -x)
print list # this prints [10, 6, 5, 3, 2, 1]
```

##### Challenges

1. Take the list of words [here](https://github.com/hack101/AwesomePython/blob/master/words.txt) and sort them by their third letter.
2. (This one is a little difficult!) Try writing a method to sort a list using [quicksort](http://me.dt.in.th/page/Quicksort/) in only 1 line. 
You will need both list comprehension as well as lambda expressions. Hint: recursion is fine in lambda expressions. 
So `fib = lambda n: 1 if n == 1 else n * fib(n-1)`.

### 3. Built-in Functions

Built-in functions are exactly that, functions that are built into python. For a full list see [here](https://docs.python.org/2/library/functions.html).

This list includes `int`, `bool`, `str`, `float`, `list`, `dict`, `set`, and `tuple`, which are used for typecasting.

We already saw the `sum` funtion in one of the above challenges, (this function sums all the elements of a list). 
We'll go over a few other useful built-in functions now!

- `len`: returns a length of a list, set, tuple, string, or dictionary
- `min` and `max`: There built in functions find the min and max of a list.
- `zip`: This function "zips" together two lists, returning a list of tuples, where each tuple contains the corresponding elements for each list it zipped. It's best understood by example.
```python
list1 = [ 1, 2, 3, 4 ]
list2 = [ "a", "b", "c", "d" ]
list3 = [ "A", "B", "C", "D" ]
print zip(list1, list2, list3)
```
This prints `[(1, 'a', 'A'), (2, 'b', 'B'), (3, 'c', 'C'), (4, 'd', 'D')]`
- `filter`: This functions filters a list by a function which returns true or false. For example, the lambda expression `lambda x: x>5` will return true for all numbers greater than 5. Let's say we have a list of numbers `list = [1,2,3,4,5,6,7,8]`.
```python
new_list = filter(lambda x: x>5, list)
print new_list
```
This prints `[6, 7, 8]`.
- `map`: This function applys a funtion to a list and returns a new list. For example, if we want to (again) make a list of every number from 1 to 100 squared. we would do 
`list = map(lambda x: x ** 2, range(1,101))`. 
Or, if we wanted to square only the even numbers, we could so `list = map(lambda x: x ** 2, filter(lambda x: x%2 == 0, range(1,101)))`
We don't need to use lambda expressions, we can use any callable object. 
This turns a list of integers into strings: `map(str,[1,2,3,4,5])`
- `any`: Checks a list of booleans and returns true if any of them is true. Like `OR`ing every element. For example,
```python
if any(map(lambda x: x == 5, list)):
    print "5 is in the list!"
```
- `all`: Checks that all of a list booleans are true. Like `AND`ing every element. For example,
```python
if all(map(lambda x: x == 5, list)):
    print "This list is just 5s!!!"
```
- `reduce`: Repeatedly apply a function to a list. The function called must take two arguments. We'll walk through an example to see how it works.
Take a list `list = [1,2,3,4,5]`. We call `reduce(lambda x,y: x+y, list)` and this returns 15. It works like so:
    1. First the function is applied to the first two elements: 1 + 2 = 3.
    2. Next, the function is applied to the result of the last call, and the next element: 3 + 3 = 6
    3. Again, until the list is empty. 6 + 4 = 10; 10 + 5 = 15.
We basically just recreated the sum function!

##### Challenges:

1. Use `len` and `filter` to figure out how many of the words in [this list](https://github.com/hack101/AwesomePython/blob/master/words.txt) have an even number of letters.
2. Use `map` to turn [this](https://github.com/hack101/AwesomePython/blob/master/int_strings.txt) list of strings into their integer values + 2.
3. Find the second smallest in [this](https://github.com/hack101/AwesomePython/blob/master/numbers.txt) list of integers. (Do not sort!)
4. Use reduce to find the maximum of [this](https://github.com/hack101/AwesomePython/blob/master/numbers.txt) list of integers. (Do not use `max` or sort!!!)
5. Try doing number 3 without the `min` function.

### 4. Decorators

A lot of the time, while programming, we find outselves writing a whole load of similar functions. 
Remember, pythonic code is all about beauty and simplicity, and part of that is not repeating yourself.
Decorators are python's solution to many similar functions. 

A decorator is a function which wraps another function. 
For example, let's say a lot of your functions are throwing errors and you want to ignore them.
You might do something like this:

```python
try:
    function1()
except:
    pass

try:
    function2()
except:
    pass

try:
    function3()
except:
    pass
.
.
.
```

But you're repeating yourself! We're wrapping each function in a try/catch, so let's use a decorator to do that more easily.

First we define a function which takes a function as it's argument and returns a new function which does not throw errors.

```python
def noerrors(func): 
    def wrapper(*args): # define a new function which will be the function we return
        #inside this function, call the first function and catch all errors
        try:
            func(*args)
        except:
            pass
    return wrapper
```

The `args` with an asterisk is simply a way of saying "As many agruments as you like", since we don't know that arguments `func` may take. 
See [here](https://docs.python.org/2/tutorial/controlflow.html#arbitrary-argument-lists) for more. 

We now want to apply this new function to our function. Let's make a function which raises an error just to see how it this might work.

```python
def function():
    raise Exception()

function() # This raises an error, obviously. 

# now we wrap the function to stop errors
function = noerrors(function)

function() # No errors!!!
```


Decarators are just a shorthand for doing exactly what we did above! Instead of redefining 



Of course, we could have found a package on pip to do this for us...















