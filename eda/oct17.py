# a function that returns true if a or b = 10 or if the sum of a and b = 10
# makes10(9, 10) ➞ True

# mine:
def makes10(a, b):
    return True if a == 10 or b == 10 or a + b == 10 else False


# others:
def makes10(a, b):
    return 10 in [a, b, a + b]


def makes10(a, b):
    return 10 in (a, b, a + b)


makes10 = lambda a, b: 10 in [a, b, a + b]


def makes10(a, b):
    return a == 10 or b == 10 or a + b == 10


# a function that returns true if k^k = n for input (n, k)
# k_to_k(4, 2) ➞ True

# mine:
def k_to_k(n, k):
    return True if k ** k == n else False


# others:
def k_to_k(n, k):
    return n == k ** k


k_to_k = lambda n, k: k ** k == n


# function that compares strings by count of characters. return true or false
# depending if they are equal length
# comp("AB", "CD") ➞ True

# mine:
def comp(txt1, txt2):
    return len(txt1) == len(txt2)


# others:
def comp(a, b):
    return len(a) is len(b)


# a function that returns true if a string is empty
# is_empty("") ➞ True

# mine:
def is_empty(s):
    return s == ""


# others:
def is_empty(s):
    return not s


def is_empty(s):
    return len(s) == 0


def is_empty(s):
    return s == str()


def is_empty(s):
    return False if s else True


# a function that takes a number and returns negative of that number
# return_negative(5) ➞ -5

# mine:
def return_negative(n):
    if n > 0:
        return n * -1
    else:
        return n


# others:
def return_negative(n):
    return -abs(n)


return_negative = lambda n: -abs(n)


def return_negative(n):
    if n < 0:
        return n
    else:
        return -n


def return_negative(n):
    return n * -1 if n > 0 else n


def return_negative(n):
    return int("-{}".format(str(abs(n))))
