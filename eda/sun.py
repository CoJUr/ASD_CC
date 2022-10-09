# write a function that takes 2 ints and converts them to seconds and adds them
#convert(1, 3) -> 3780
# mine:
def convert(hours, minutes):
    from_hours = hours*60*60
    from_mins = minutes*60

    return from_hours + from_mins


# others:
def convert(h, m):
    return (h*3600) + m*60


convert=lambda a,b:a*3600+b*60


def convert(hours, minutes):
    minutes += hours * 60
    return minutes * 60


#a func that takes a number and returns True if <= 0, otherwise False
# mine:
def less_than_or_equal_to_zero(num):
    bool = num <= 0
    return bool



# others:
def less_than_or_equal_to_zero(num):
    return num <= 0


less_than_or_equal_to_zero = lambda x: x <= 0


def less_than_or_equal_to_zero(num):
    if(num <= 0):
        return True
    return False



#a funct that takes a list of numbers and returns the smallest number
# mine:
def find_smallest_num(lst):
    smallest = 1000000
    for i in lst:
        if i < smallest:
            smallest = i
    return smallest


# others:
def find_smallest_num(lst):
    return min(lst)


def find_smallest_num(lst):
    lst.sort()
    return lst[0]


def find_smallest_num(lst):
    mn=lst[0]
    for i in range(len(lst)):
        if lst[i]<mn: mn=lst[i]
    return mn


findSmallestNum = min


#a funct that takes a base num and an exponent num and returns the solution
# calculate_exponent(5, 5) -> 3125
# mine:
def calculate_exponent(num, exp):
    return num ** exp

# a funct that takes a list and returns the difference between the biggest
# and smallest numbers    difference_max_min([44, 32, 86, 19]) -> 67
# mine:

def difference_max_min(lst):
    return max(lst) - min(lst)


# others:
def difference_max_min(lst):
    lst.sort()
    return lst[-1] - lst[0]


def difference_max_min(lst):
    return abs(min(lst) - max(lst))


def difference_max_min(lst):
    mx=lst[0]
    mi=lst[0]
    for i in lst:
        if mx<i:
            mx=i
        if mi>i:
            mi=i
    return mx-mi


def difference_max_min(lst):
    max = lst[0]
    min = lst[0]
    for num in lst:
        if (num > max): max = num
        elif (num < min): min = num
    return max - min


# Given an n-sided regular polygon n, return the total sum of internal
# angles (in degrees). sum_polygon(3) -> 180   n always > 2    n-2 * 180
# mine:
def sum_polygon(n):
    return (n-2) * 180


# others:
def sum_polygon(n):
    if n > 2:
        return (n-2)*180


sum_polygon = lambda x: (x-2) * 180


def sum_polygon(n):
    result = 180*(n-2)
    return result