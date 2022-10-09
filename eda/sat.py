# # a function that returns the argument concatenated with "something" and " "
# # in front of it.
#
# # mine:
# def give_me_something(a):
#     return "something " + a
#
#
# # others:
# def give_me_something(a):
#     return 'something {}'.format(a)
#
#
# give_me_something = lambda a: 'something ' + a
#
#
# # a function that takes the w-d-l record of a soccer team and returns the
# # number of points it has earned so far. w = 3   d = 1   l = 0
#
# # mine:
# def football_points(wins, draws, losses):
#     total = int(wins * 3) + int(draws * 1) + int(losses * 0)
#     return total
#
#
# # others:
# def football_points(wins, draws, losses):
#     return wins*3 + draws
#
#
# football_points=lambda a,b,c:a*3+b
#
#
# def football_points(wins, draws, losses):
#     total = 0
#     win_points = wins * 3
#     total = win_points + draws
#     return total
#
#
# # two functions: one returns the passed int to str, the other vice versa
#
# # mine:
# def to_int(txt):
#     return int(txt)
#
#
# def to_str(num):
#     return str(num)
#
# # others:
# to_int = int
# to_str = str
#
#
#
#
# def to_int(txt):
#     try:
#         out=int(txt)
#     except:
#         out="impossible"
#     return out
#
#
# def to_str(num):
#     try:
#         out=str(num)
#     except:
#         out="impossible"
#     return out
#
#
#
# def to_int(txt):
#     return int(txt)
#
#
# def to_str(num):
#     return "{}".format(num)
#
#
# num = input("Enter a number: ")
# if num < 0:
#     raise ValueError("Sorry, no numbers below zero")

# can use the raise keyword outside the except block
#
# try:
#     num = 5 / 0
# except:
#     print("An error occurred")
#     raise


# buggy code problem, Emmy and Mubashir
# mine:
def greeting(name):

    if name == "Mubashir":
        return "Hello, my Love!"

    return "Hello, " + name + "!"


# others:
def greeting(name):
    return 'Hello, {}!'.format('my Love' if name == 'Mubashir' else name)


greeting = lambda n:"Hello, my Love!" if n == "Mubashir" else "Hello, " + n + "!"


def greeting(n):
    if n=="Mubashir":return"Hello, my Love!"
    return"Hello, "+n+"!"


# function to find largest number in a list
# mine:
def findLargestNum(nums):
    return max(nums)


# others:

def findLargestNum(nums):
    largest = nums[0]
    for i in nums:
        if i > largest:
            largest = i
    return largest


def findLargestNum(nums):
    return sorted(nums)[-1]


def findLargestNum(nums):
    largest, left, right = nums[0], 1, len(nums)-1
    while left<=right:
        if nums[left]>largest:
            largest = nums[left]
        if nums[right]>largest:
            largest = nums[right]
        left += 1
        right -= 1
    return largest


def findLargestNum(nums):
    nums.sort()
    return nums[-1]