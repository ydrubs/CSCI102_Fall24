##Slide 5 - Defining lists
# fruits = ['apples', 'orange', 'kiwi']
# profile = [24, 'Wichita', [3.21, 5.6]]
# freinds = []
#
# print(fruits)
# print(f'my favotire fruits are {fruits[0]} {fruits[1]}')
# print(profile[2][1])


##Storing the result of a math operation in a list
# import math
# x = 2
# lst = [x, math.sqrt(x), math.pi]
# print(lst)
# print(lst[2])
# print(lst[x])
# print(lst[x+1]) #Index error


#Slide 6 - Your turn
# superheroes = ['Batman', 'Spiderman', 'Superman', 'Incredibles']
# superheroes.append('Iron Man')
# superheroes.append('Ghost Rider')
# print(superheroes)
#
# #Reference list elements by item (directly)
# for superhero in superheroes:
#     print(superhero)


##Reference list element by index
# for i in range(len(superheroes)):
#     print(i, superheroes[i])
    # print(superheroes[3], superheroes[i]) ##Important difference




##Slide 7
# first = [1,2,3,4]
# second = list(range(1,1001))
# print(second)

# for number in second:
#     print(number)

# print(max(second)) #returns the biggest value in the list
# print(min(second)) #returns the smallest value in a list
# print(sum(second)) #returns the sum of a list

##What is the average of the list
# avg = sum(second)/len(second)
# print(avg)


##Build a list from a string
# message = 'Hello There, good moeninrg'
# message_lst = list(message)
# print(message_lst)
#
# #Other list operations
# print(len(message_lst)) #chek the number of elements in a list
# print(message_lst + list('freind')) #Combine two lists together with a '+' sign

# message_lst = ''.join(message_lst) #Combine back into a string
# print(message_lst)

#Slide 8
##This example allows you to add people to a roster by looping through the number of people that get added
# roster_size = int(input("Enter the number of people to add: ")) #Get input about number
# roster_lst = [] #Create an empty list to hold the people
#
# for name in range(roster_size): #Loop through however many people we said we wanted to add
#     new_member = input("What is the new members name? ") #Get the persons name
#     roster_lst.append(new_member) #Add the person to the end of the roster list
#
# print(roster_lst) #print results
# roster_lst.append('Fabrel')

# print(roster_lst)



##This example generates n random numbers between 1 and 365 and puts them into a list
# from random import randint
# number_lst = [] #empty list to hold numbers
# n = 21 #How much elements to put in the list
#
# for i in range(n):
#     number = randint(1,365) #Choose random number
#     number_lst.append(number) #append that number to list
#
# print(number_lst)



##SLide 9 - Your Turn


##Slide 10 - Skill Review for exercise 5.1
##Stopping a loop when the 'enter' key is pressed.
# while True:
#     data = input("Enter some data: ")
#     if data == '':
#         break
    # data = int(data)
    # lst.append(data)





#Slide 12 - Different operations and list slicing techniques that are possible
first = [1,2,3,4]
# print(len(first))
# print(first[0])
# print(first[2:4])
first = first + [5, 6]
# print(first)
# #
#
second = list(range(1,7))
# print(first == second) # TRUE because all the elements in first are also in second
# print(first is second) #Why do you think the 'is' keyword returns False here?
# print(id(first), id(second)) # Not the same place in memory
# third = first # Third IS first
# print(id(first), id(third))


##Searching through a list
# print(1 in first) #True
# print('one' in first) #False
# print(int('1') in first) #False, Ture if int('1')



import random
csci102_Roster = ['Eliud', 'Jayce', 'Javier', 'Miguel', 'Colby', 'Ada', 'Aiden G', 'Francisco', 'Ruth', 'Ashley',
                  'Jackie', 'Allan', 'Anivar', 'Joscelyn', 'Dominic', 'Zahmari', 'Aiden P', 'Devin', 'Juan',
                  'Jordan', 'Edwin', 'Tye', 'Fabrel']
random_student = random.choice(csci102_Roster)
# print(random_student)
# print('Jordan' in csci102_Roster)
#
# print(f'{random.randint(-20,20)} extra credit points goes to {random_student}')


##Slide 13 - Changing elements in a list
# first = [1,2,3,4]
# first[0] = 5
# print(first)

# csci102_Roster[0] = 'Taylor Swift'
# print(csci102_Roster)


##Slide 14 - Manipulating through looping
# numbers = [2,3,4,5]
# for i in range(len(numbers)):
#     numbers[i] = numbers[i] ** 2
#
# print(numbers)
#
# sentence = "Python is a good beginner programming language"
# sentence = sentence.split() #Split into individual words and make a list
# print(sentence)
# print(f"The sentence is {len(sentence)} words.")

# for i in range(len(sentence)): #Loop through each element by index
#     print(sentence[i].isupper())
#     sentence[i] = sentence[i].upper() #Change each word to upper case and save it into the same position

# print(sentence)

# for i, word in enumerate(sentence):
#     sentence[i] = word.upper()

# print(sentence)


##Slide 15 - adding elements by index
# csci102_Roster[1] = 'Kanye'
# print(csci102_Roster)
# csci102_Roster.insert(0,'Eliud')
# print(csci102_Roster)


# new_students = ['Stewie G.', 'Yuriy', 'Brendan Flowers']
# csci102_Roster.extend(new_students)
# print(csci102_Roster)
#
# csci102_Roster = csci102_Roster + ['James Hatfield', 'Chritian Bale']
# print(csci102_Roster)




##Slide 16 - removing elements
# pass
# print(last_person)
#
# pass
# print(first_person)
#
# print(csci102_Roster)

##Remove an element using its name
# last_person = csci102_Roster.pop()
# print(last_person)
# a_person = csci102_Roster.pop(random.randint(0,20))
# print(a_person)
#

# freind = csci102_Roster.index('Javier')
# print(freind)
# extra_creidt = csci102_Roster.pop(csci102_Roster.index('Javier'))

##Slide 19 - searching and sorting
##Building a list from conditions in another list (numbers greater then 15)
from random import randint
#
# lst = []
# for i in range(20):
#     lst.append(randint(1,20))
# print(lst)
#
# new_lst = []
# for n in lst:
#     if n > 15:
#         new_lst.append(n)
#
# print(new_lst)

##Slide 20
##Given a list of 20 random integers between 1 and 20, create a new list of all integers that appear more then once.
# from random import randint
#
lst = []
for i in range(20):
    lst.append(randint(1,20))
# print(lst)


# new_lst = []
# for n in lst: # Check each element in the original
#     if lst.count(n) > 1: # If that element appears more then once
#         new_lst.append(n) # Move THAT element to a new list

# print(new_lst)
# new_lst = set(new_lst)
# print(new_lst)
#
# new_lst = list(new_lst)
# # print(new_lst)

##Given TWO lists of random numbers between 1 and 20 create a new list that has the common elements of both lists
# lst2 = []
# for i in range(20):
#     lst2.append(randint(1,20))
#
# print(lst)
# print(lst2)

new_lst = []
# for n in lst:
#     if n in lst2:
#         new_lst.append(n)
#         lst2.pop(lst2.index(n))
# #
# print(new_lst)


##Slide 21 - Sorting a list
# lst = [4,10,2,1,7]
#
# lst.sort() #in-place sorting
# print(lst)
# #
# lst2 = [4,10,2,1,7]
# lst_2 = sorted(lst2)
# print(lst2)
# print(lst_2)

# print(pass) # This returns the list sorted in numeric order
# print(lst2) #Notice that this returns the original list - not the sorted one
#
# lst3 = pass
# print(lst3)
#
# print(pass)





##Slide 23 - Intro to Tuples
cards = () #Empty tuple container
cards = (6,7,8,9,10,'Jack') #Tuples of card ranks
# cards = ((2,'hearts'), (8, 'spades'), ('Ace', 'Clubs')) #Tuple of tuples
cars = ([2020, 'Chevy', 'Corvette'], [2023, 'Toyota', 'Prius']) #Tuple of lists

# print(cards[0])
# cards[0] = 'King' #Demonstrates you can't modify a tuple like you can a list
# print(cards)

# cars[0][1] = 'Ford'
# cars[0][2] = 'Mustang GT 500'
# print(cars)



##SLide 25
###Building a deck of cards by combining tuples
import random

suit_tuple= ('hearts', 'diamomds', 'spades', 'clubs')
rank_tuple = ('2', '3', '4', '5', '6', '7', '8','9', '10', 'jack', 'queen', 'king', 'ace')

deck = []
for suit in suit_tuple:
    for rank in rank_tuple:
        card = (rank, suit) #Temporary variable to store the current card in loop
        deck.append(card) #Add this card to the deck list

print(deck)
print(deck[random.randint(0,len(deck))])

random.shuffle(deck)
print(deck)

##Slide 26 (IN_CLASS_TUPLE PRACTICE)
point1 = (6,6)
point2 = (9,1)

x1 = point1[0]
y1 = point1[1]

x2 = point2[0]
y2 = point2[1]

slope = (y2-y1)/(x2-x1)
print(slope)

slope_alt = (point2[1]-point1[1]/point2[0]-point1[0])





##Slide 28
##Defining a simple function




##Slide 29
##Pass arguments into a function (no limit on amount or data type)






##Slide 30
##Pass default values into a function (order of keyword parameters vs. positional parameters matters!)
##positional parameters need to be defines FIRST!




##Try it:
"""Write a function called find_bigger that accepts two decimal number and returns the bigger of the two"""


##Slide 31
"""Write a function named only_ints that takes two parameters.
Your function should return True if both parameters are integers, and False otherwise."""







# ##Slide 32
##Write a function that removes digits from a string and returns it back with only alphabetic characters.






##Slide 33
##Write a function that accepts an integer and returns the sum of its digits







###########Extra Example
"""Write a function that takes an integer and returns all integers within a range whose sum of digits is equal to the integer passed in.
For example if 11 is passed in then 29,38,47,etc.. are returned because 2+9=11, 3+8=11, etc..."""

# def sum_digits(number):
#     for i in range(10,200):
#         current_number = list(str(i))
#         # print(current_number)
#         sum = 0
#         for digit in current_number:
#             sum += int(digit)
#             if sum == number:
#                 print(i)
#
# sum_digits(11)
