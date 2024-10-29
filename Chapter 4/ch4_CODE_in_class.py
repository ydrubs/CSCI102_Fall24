# #Slide 3
# string = 'Hello to you'
# for char in string: #Iterate through the individual characters
#     print(char, end = '')

# print()
# print(len(string)) #print the character at the specified index
#
# print(string[0])

# myNum = 10
# for digit in myNum: #Demonstrate that an integer cannot be broken down into digits like a string can
#     print(digit, end='')


#Slide 4
# name = 'Skywalker'
# print(name[0]) #The first letter is 'S'
#
# print(len(name))
# print(name[-1]) #negative index works backwards
# print(name[-2]) #Takes one less than the last value
#
# print(name[len(name)-1])
# print(pass)

##Slide 5
# data = 'Hi there!'
#
# ###Loop Through the indexes of the string
# for index in range(len(data)):
#     print(index, data[index])

# ##Loop through the elements of the string
# for char in data:
#     print(char)


##Slide 7
# mutable = ['G', 'O', 'O', 'D']
# print(mutable[0])
# mutable[0] = 'H'
# print(mutable)

# immutable = 'Good'
# print(immutable)
# print(immutable[0]) #This command is fine

# immutable[0] = 'H' # ..This is not. Can't override the individuals characters
# immutable = 'Hood' #...But you can override the variable itself
# print(immutable)



##Slide 9
# name = 'myfile.txt'
# print(name[0:])
# print(name[0:1]) #stops one short of the second argument
# print(name[0:2])
# print(name[2:6:2])

# print(name[len(name)::-1])

# print(name[0:3]+name[0:3])
# print(pass)

##Slide 9 - Try to run your own experiments with the string below
# my_string = "Give a man a program, frustrate him for a day. " \
#             "Teach a man to program, frustrate him for a lifetime."

##Slide 10 - Your turn - Move Two Letters



##Slide 11
# superhero = 'incredible HULK'
#
# print(superhero.upper())
# print(superhero.lower())
# print(superhero.title())
# print(superhero.split())

##Slide 12
# address = '123 Fake St.'

# for char in address:
#     print(char.isdigit())
# #
# for char in address:
#     print(char, char.isupper())
#
# for char in address:
#     print(char, char.islower())

# for char in address:
     # print(char, char.isalnum())

# print(address[0:3].isnumeric()) #returns True




##Slide 13
##Map a directory of files by using the split command
# string = "C:\\Users\\yuriy.drubinskiy\OneDrive - Garden City Community College\\Python Class\\Powerpoints and notes"
# string = string.split('\\')
# print(string)
# print(string[0])
#
# #
# print('\\'.join(string))


##Slide 13/14 - STRING METHODS SUMMARY
####COmmands that let you access and see info about what string methods do
# print(dir(str)) # A list of available methods for the 'string' object
# print(help(str)) # A more detailed description of each available method


##Slide 15
# text = """A long time ago in a galaxy far far away..
# It is a period of civil war.
# Rebel spaceships, striking
# from a hidden base, have won
# their first victory against
# the evil Galactic Empire."""

# print('war' in text)
# print('empire' in text)
# print('Empire' in text)
# #
# print(text.index('war'))
# print(text[60:70]) #SInce war first appears at character 67, we can see what characters 60-69 are




##Slide16
##the variable below defines a list data structure. We will lean more about this in chapter 5
# fileList = ['myfile.txt', 'myprogram.exe', 'yourfile.txt']
# for file in fileList:
#     if '.txt' in file:
#         print(file)




##Slide 17
# import this
# string = """Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!"""

# e_or_a_count = 0

# for letter in string:
#     # print(letter, end = '')
#     if 'a' in letter or 'e' in letter:
#         e_or_a_count +=1
#
# print(e_or_a_count)

# string = string.split()
# print(string)
#
# for word in string:
#     if 'e' or 'a' in string:
#         e_or_a_count +=1
#
# print(e_or_a_count)

#Slide 21
# f = open('myfile.txt', 'w')
# f.write("1. Justin Herbert $52.5 million\n2. Lamar Jackson $52 million\n3.Jalen Hurts $51 million")
# f.close()


####My try



#Slide 23
import random
f = open('integers.txt', 'w')

for count in range(500):
    n = random.randint(1,500)
    f.write(str(n) + '\n')

f.close()


##Slide 24
# f = open("myfile.txt", 'r')
# #
# # ##Since the text file is broken up into lines, readline() adds an extra carrige return (\n)
# while True: #As long as there's data to read, read it
#     line = f.readline()
#     if line == '':
#         break
#     print(line)

##Slide 25
## f = open('integers2.txt', 'r') #COMMENT OUT TO SEE WHY THIS FILE CANNOT BE READ
f = open('integers.txt', 'r')
theSum = 0
for line in f:
    # print(line)
    number = int(line)
    theSum += number
# pass

print('The sum is', theSum)

##Slide26
###GENERATE SOME DATA TO BE READ
# import random
#
# f = open('integers2.txt', 'w')
# for count in range(500):
#     number = random.randint(1, 500)
#     f.write(str(number) + ' ') # Create random ints with a space seperator
# f.close()

# ###Read from the file and sum it
# f = open('integers2.txt', 'r')
# theSum = 0
# pass:
#     pass #Split on space or newline (you can specify a string argument for other seperators)
#     pass:
#         pass
#         pass

# print('The sum is', theSum)

