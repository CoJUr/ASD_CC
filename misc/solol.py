# a program that prints 4 characters from an opened file
file = open("filename.txt", "r")
for i in range(21):
    print(file.read(4))
file.close()

# open a file, read its content and print its length
file = open("filename.txt", "r")
str = file.read()
print(len(str))
file.close()

# readlines() method can return a list wherein each el is a line in the file
file = open("filename.txt", "r")
print(file.readlines())
file.close()
# output: ['line1 text \n', 'line2 text \n', 'line3 text']

# what will the following print if the file has 7 lines of content?
len(open("test.txt").readlines())
# 7


# modes for open() include w(rite), r(ead), a(ppend), r+(read and write), ect
# can include a b for binary mode for non-text files. e.g "wb" for write binary
