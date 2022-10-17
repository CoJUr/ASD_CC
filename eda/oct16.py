"""
A function that stutters a word as if someone is struggling to read it.
The first two letters are repeated twice with an ellipsis ... and space after
each, and then the word is pronounced with a question mark ?.
Example:  stutter("incredible") ➞ "in... in... incredible?"
"""


# mine:
def stutter(word):
    ltr1 = word[0]
    ltr2 = word[1]

    str = ltr1 + ltr2 + "... " + ltr1 + ltr2 + "... " + word + "?"
    return str


# others:


def stutter(word):
    return word[:2] + '... ' + word[:2] + '... ' + word + '?'


def stutter(word):
    letter1 = word[0]
    letter2 = word[1]
    return letter1 + letter2 + "... " + letter1 + letter2 + "... " + word + "?"


def stutter(word):
    return '{0}... {0}... {1}?'.format(word[:2], word)


def stutter(word):
    return (2 * (word[:2] + '... ')) + word + '?'


def stutter(word):
    return '{0:.2}... {0:.2}... {0}?'.format(word)


def stutter(word):
    return word[0:2] + '... ' + word[0:2] + '... ' + word + '?'


def stutter(word):
    return "{s}... {s}... {w}?".format(s=word[0:2], w=word)


"""
 Create a function that takes three arguments prob, prize, 
 pay and returns True if prob * prize > pay; otherwise return False.
 e.g:  profitable_gamble(0.2, 50, 9) ➞ True
 """


# mine:
def profitable_gamble(prob, prize, pay):
    return (prob * prize) > pay


# others:
def profitable_gamble(prob, prize, pay):
    outcome = prob * prize - pay
    if outcome > 0:
        return True
    else:
        return False


def profitable_gamble(prob, prize, pay):
    return True if prob * prize > pay else False


"""
A function that returns the number of frames shown in a given 
number of minutes for a certain FPS. 
e.g:  frames(1, 1) ➞ 60   frames(10, 25) ➞ 15000
"""


# mine
def frames(minutes, fps):
    return minutes * (fps * 60)


# a function that accepts a name and returns a greeting
# e.g:  hello_name("Gerald") ➞ "Hello Gerald!"

# mine:
def hello_name(name):
    return "Hello " + name + "!"


# others:
def hello_name(name):
    return "Hello {}!".format(name)


def hello_name(name):
    return ("Hello %s!") % name


def hello_name(name):
    a = "Hello {}!"
    return a.format(name)


def hello_name(name):
    return 'Hello {name}!'.format(name=name)


# a vehicle needs 10x the amount of fuel than the distance it travels. however
# it must always carry a min of 100 fuel before setting off.
# given distance, return the amount of fuel it needs.   calculate(3) ➞ 100

# mine:
def calculate_fuel(n):
    if n * 10 < 100:
        return 100
    else:
        return n * 10


# others:
def calculate_fuel(n):
    return max(n*10, 100)


def calculate_fuel(n):
    return n*10 if n*10 >= 100 else 100