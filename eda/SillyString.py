class SillyString(str):
    # this method gets called when use == on the obj
    def __eq__(self, other):
        print(f"Comparing {self} and {other}")
        #if self and other have same length, return True
        return len(self) == len(other)


print('hello world' == 'world hello') # False
print('hello world' == 'hello world') # True

#compare a str with a sillystr
print('hello world' == SillyString('world heyyo')) # True

#compare a sillystr with a list
print(SillyString('hello world') == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])