# a function that returns the argument concatenated with "something" and " "
# in front of it.

# mine:
def give_me_something(a):
    return "something " + a


# others:
def give_me_something(a):
    return 'something {}'.format(a)


give_me_something = lambda a: 'something ' + a


# a function that takes the w-d-l record of a soccer team and returns the
# number of points it has earned so far. w = 3   d = 1   l = 0

# mine:
def football_points(wins, draws, losses):
    total = int(wins * 3) + int(draws * 1) + int(losses * 0)
    return total


# others:
def football_points(wins, draws, losses):
    return wins*3 + draws


football_points=lambda a,b,c:a*3+b


def football_points(wins, draws, losses):
    total = 0
    win_points = wins * 3
    total = win_points + draws
    return total


# two functions: one returns the passed int to str, the other vice versa

# mine:
def to_int(txt):
    return int(txt)


def to_str(num):
    return str(num)

# others:
to_int = int
to_str = str




def to_int(txt):
    try:
        out=int(txt)
    except:
        out="impossible"
    return out


def to_str(num):
    try:
        out=str(num)
    except:
        out="impossible"
    return out



def to_int(txt):
    return int(txt)


def to_str(num):
    return "{}".format(num)