# # a program to check to see if two objects are equal, if so return True
# # else false
#
# # help(id)
#
# # intern strings - sys.intern() to compare memory addresses of strings
# from sys import intern
# a = {1, 2, 3}
# b = {1, 2, 3}
#
# print(a is b)
#
# print(id(a))
# print(id(b))
#
# # can ensure a and b point to the same object by using sys.intern()
# print(a is b)
#
# c = 1
# print(a is c)
# print(id(c))

# mine:
def is_equal(obj_one, obj_two):
    return obj_one is obj_two


# others:
is_equal = dict.__eq__

is_equal = lambda obj_one, obj_two: obj_one == obj_two


# Create a function which returns the Modulo of the two given numbers.
# mod(-13, 64) -> 51   mod(50, 25) -> 0   mod(-6, 3) -> 0

# mine:
def mod(m, n):
    times_went_in = m % n
    return times_went_in


# others:
mod = int.__mod__


def mod(m, n):
    return m % n


def mod(m, n):
    return mod(m + n, n) if m < 0 else m if m < n else mod(m - n, n)


mod = lambda m, n: m % n


# Given two numbers, return True if the sum of both numbers is less than 100.
# Otherwise return False.  less_than_100(22, 15) -> True

# mine:
def less_than_100(a, b):
    return a + b < 100


# others:
less_than_100 = lambda a, b: a + b < 100


def less_than_100(a, b):
    return True if a + b < 100 else False


# Create a function that returns True when num1 is equal to num2; otherwise
# return False. is_same_num(4, 8) -> False

# mine:
def is_same_num(num1, num2):
    return num1 == num2


# others:
is_same_num = lambda x, y: x == y


def is_same_num(num1, num2):
    return True if num1 is num2 else False


# Create a function that returns True if an integer is evenly divisible by
# 5, and False otherwise.  divisible_by_five(5) -> True
# divisible_by_five(-55) ➞ True

# mine:
def divisible_by_five(n):
    return True if n % 5 == 0 else False


# others:
def divisible_by_five(n):
    return not n % 5


def divisible_by_five(n):
    return (n/5).is_integer()


def divisible_by_five(n):
    return bool(n%5 == 0)

