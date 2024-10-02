##Slide 5 - One way selection statement
# name = input("Enter your username: ")
# if name == 'admin':
#     print("Access granted - secret area unlocked")
# #
# print()
# print("Welcome feel free to explore ")
#
#


#Slide 6 - If/else statement
# name = input("Enter your username: ")
# if name == 'admin':
#     print("Access granted - secret area unlocked")
# else:
#     print("Incorrect username")




##Slide 7: Multi-way selection
# number = int(input('Enter the numeric grade: '))
# if number > 100:
#     letter = 'invalid input'
# elif number > 89:
#     letter = 'A'
# elif number > 79:
#     letter = 'B'
# elif number > 69:
#     letter = 'C'
# else:
#     letter = 'F'
#
# print('The letter grade is', letter)



# print("What color is the traffic light?")
# trafficLight = input("(r)ed, (y)ellow, or (g)reen: ")

# if pass or pass:
#     print("Stop!")
# elif pass or pass:
#     print("Proceed with caution.")
# elif pass or pass:
#     print("Go ahead.")
# else:
#     print("Check your vision!")


##Slide 8 ACTIVITY
# mood = input("How are you feeling?")
# if mood == 'okay':
#     print("have a good day")
# elif mood == 'tired':
#     print("Get some rest")
# else:
#     print('not sure what that is')



##Slide 9
# x = 10
# y = 5
# z = 2
#
# print(x == y) #False
# print(x > y) #True
# print(y > x/z) #
# print(x != y) #True
# print() #

##Slide 11
# a = True
# b = False

# print(a or(a and b)) #True
# print(b and (a or b)) #False
# print(not b or (a and b)) #True
# print(a and not b or b and not a) #False

#Write your own challenging logic statement, make it as long as you want
# print(b and not a or (not a and not b or not a)) #False


##Slide 11
# x = 40
# y = 20
# print(x == y or x == 2*y)
# print(x > y and x > 2*y)
# print(not(x == y or x == 2*y))

##slide 12
# grade = int(input("What is your grade: "))
# if grade >= 90 and grade < 101:
#     print('Nice Job')
# elif grade < 90 and grade >= 80:
#     print('Not bad')
# elif grade <= 79 and grade >= 70:
#     print('There is room for improvement')
# else:
#     print("Better luck next time")

##WRAP UP ACTIVITY
# valid_user = 'user123'
# is_active = True
#
# user = input("Enter username: ")
#
# if user == valid_user and is_active:
#     print('access granted')
#
# elif user == valid_user and is_active != True:
#     print('access denied')
#
# else:
#     print('no user found')



"""9/23/24"""

##Slide 15
# a = 10
#
# for a in range(1):
#     # print("It's alive!", sep = '****' )
#     print(type(range(1)))
#     print(a)



##Slide 17
# number = 1
# for i in range(4):
#     print(number)
#     number = number + 3
#
# print(number)


##Slide 18
# number = 1
# times_2 = 2
#
# print(number)
# for i in range(5):
#     number = number * times_2
#     print(number)

##Slide 19
# for i in range(10):
#     print(i, end = ' ')


##Equivelant to the following but twice as long
# count = 0
# for i in range(11):
#     print(count, end=' ')
#     count = count + 1

##Checkpoint Activity
"""
Write a for loop that counts 20 ‘Mississippis’, such as -
1 Mississippi
2 Mississippi
...
...
20 Mississippi
"""""
# for i in range(21):
#     print(i, end = ' Mississippi\n')


##Slide21
# stop = 20
# for i in range(10,20):
#     print(i)
#

##SLide 22
#Count by threes
# for i in range(3,101,3):
#     print(i, end = ' ')

#Count backwards from 100
# for i in range(101,1,-1):
#     print(i)


##Slide 23
a = 5
b = 3
# print(a, b)

# a +=5
# b +=5
# print(a, b)


c = 2
d = 3
# print(c, d)

c *=5
d **=2
# print(c, d)


# first_name = 'Bob'
# first_name += 'Doe'
# print(first_name)

###EXTRA DEMO

#Not the best solution
# total = 0
# add_one = 0
# for i in range(1,101):
#     total +=add_one
#     add_one +=1
# print(total)

#Better solution
# total = 0
# for i in range(1,101):
#     total +=i
# print(total)

####FIZZ BUZZ SOLUTION
# for i in range(1,101):
#     if i%3 == 0 and i%5 == 0:
#         print('FizzBuzz')
#     elif i%3 == 0: #There is no remainder
#         print('Fizz')
#     elif i%5 == 0:
#         print("Buzz")
#     else:
#         print(i)



##Slide 26
# stop = 1000
# total = 0
#
# while total < stop:
#     numb = int(input("Pretty Please enter a number: "))
#     total += numb #instead of total = total + numb
#     print(total)


##slide 28 ACTIVITY
# stop = 1000
# total = 1
# numb = int(input("Pretty Please enter a number: "))
# print(total)
#
# while total < stop:
#     total += numb #instead of total = total + numb
#     print(total)




##Slide 29
# theSum = 0.0
# data = input('Enter a number or just enter to quit: ')
#
# while data !="":
#     number = float(data)
#     theSum += number
#     data = input('Enter a number or just enter to quit: ')
#     print('The sum is', theSum)


##Slide 30
# theSum = 0.0
# while True:
#     data = input("Enter a number or just enter to quit: ")
#     if data == '':
#         break
#
#     number = float(data)
#     theSum += number
#     print("The sum is", theSum)



##Slide 32
# while True:
#     number = int(input("Enter the numeric grade: "))
#     if 100 >= number >= 0:
#         break
#
#     else:
#         print("Error: grade must be between 100 and 0")
#         print(number) # Just echo the valid input
#

##Slide 33
# done = False
#
# while not done:
#     number = int(input("Enter the numeric grade: "))
#     if number >= 0 and number <= 100:
#         print("Setting 'done' to True")
#         done = True
#
#     else:
#         print("Error: grade must be between 100 and 0")
#         print(number) # Just echo the valid input


##Slide 34
# Fail to break loop
# while True:
#     number = int(input('Enter the numeric grade: '))
#     if number >= 0 and number <= 100:
#         print(number)
#         ###Fixing it
#         break
#
#     else:
#         print('Error: grade must be between 100 and 0')
#         print(number) # Just echo the valid input

################infinite Loop, not updating variable
# a = 0
# while a < 1000:
#     print(a)
#     ##FIxing this
#     a +=1

################Did not test for a = 500 condition
###Edge case - Checking for a condition that is not common

# a = 0
# while a < 1000:
#     a +=1
#     if a < 500:
#         print("Boom", a)
#     elif a > 500:
#         print('Pow', a)
#     elif a == 500:
#         print("WAM")



##Slide 35
# import random
# # from random import randint, random
# print(random.random()) #Number between 0 and 1
# print(random.randint(1,20))



##Slide 36
##Dice rolling simulator
from random import randint

for roll in range(100):
    print(randint(1,100))



##Guess the number game
import random

myNumber = random.randint(1,100)
count = 0

while True:
    count += 1
    userNumber = int(input("Enter your guess: "))
    if userNumber < myNumber:
        print("Too small!")
    elif userNumber > myNumber:
        print("Too large!")
    else:
        print("Congratulations! You've got it in", count, "tries!")
        break
