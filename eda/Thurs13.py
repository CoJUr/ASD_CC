# fix the code so that the function returns true only if x = 7
#  is_seven(4) -> False


def is_seven(x):
    return False if x != 7 else True


print(is_seven(4))


#given a list of ints, return the diff between the largest and smallest
# difference([10, 15, 20, 2, 10, 6]) -> 18

#mine:
def difference(nums):
    return max(nums) - min(nums)


#others:
def difference(nums):
    nums.sort()
    return nums[-1] - nums[0]


def difference(nums):
    nums.sort()
    x = len(nums)
    return nums[x-1]-nums[0]


#concatenate two integer lists together
# concat([1, 3, 5], [2, 6, 8]) ➞ [1, 3, 5, 2, 6, 8]

#mine:
def concat(list1, list2):
    return list1 + list2


#others:
def concat(lst1, lst2):
    lst1.extend(lst2)
    return lst1


def concat(lst1, lst2):
    for i in lst2:
        lst1.append(i)
    return lst1


concat = lambda lst1, lst2: lst1 + lst2


def concat(lst1, lst2):
    new_l = []
    for elem in lst1:
        new_l.append(elem)
    for elem in lst2:
        new_l.append(elem)
    return new_l