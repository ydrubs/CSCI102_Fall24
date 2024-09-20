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
x = 10
y = 5
z = 2
#
# print(x == y) #False
# print(x > y) #True
# print(y > x/z) #
# print(x != y) #True
# print() #

##Slide 11
a = True
b = False

# print(a or(a and b)) #True
# print(b and (a or b)) #False
# print(not b or (a and b)) #True
# print(a and not b or b and not a) #False

#Write your own challenging logic statement, make it as long as you want
print(b and not a or (not a and not b or not a)) #False


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
valid_user = 'user123'
is_active = True

user = input("Enter username: ")

if user == valid_user and is_active:
    print('access granted')

elif user == valid_user and is_active != True:
    print('access denied')

else:
    print('no user found')


##Slide 15
# a = 4

# pass
# pass
# pass



##Slide 17
# number = 1
# pass
# pass
# pass

##Slide 18
# number = 1
# times_2 = 2
# for i in range(5):
#     number = number * times_2
#     print(number)

##Slide 19
# for
# pass


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


##Slide21
# pass
# pass


##SLide 22
#Count by threes

#Count backwards from 100

##Slide 23
# a = 5
# b = 5
# print(a, b)

# pass
# pass
# print(a, b)


# c = 2
# d = 3
# print(c, d)

# pass
# pass
# print(c, d)


# pass
# print(d)

##Slide 26



##slide 28 ACTIVITY





##Slide 29
# theSum = 0.0
# data = input('Enter a number or just enter to quit: ')
#
# while pass:
#     number = float(data)
#     theSum += number
#     data = input('Enter a number or just enter to quit: ')
#     print('The sum is', theSum)


##Slide 30
# theSum = 0.0
# while pass:
#     data = input("Enter a number or just enter to quit: ")
#     if data == pass:
#         pass
#
#     number = float(data)
#     theSum += number
#     print("The sum is", theSum)

##Slide 32
# while True:
#     number = int(input("Enter the numeric grade: "))
#     if pass:
#         pass
#
#     else:
#         print("Error: grade must be between 100 and 0")
#         print(number) # Just echo the valid input


##Slide 33
# done = False
#
# while not done:
#     number = int(input("Enter the numeric grade: "))
#     if number >= 0 and number <= 100:
#         print("Setting 'done' to True")
#         pass
#
#     else:
#         print("Error: grade must be between 100 and 0")
#         print(number) # Just echo the valid input


##Slide 34
#Fail to break loop
# while True:
#     number = int(input('Enter the numeric grade: '))
#     if number >= 0 and number <= 100:
#         print(number)
#
#     else:
#         print('Error: grade must be between 100 and 0')
#         print(number) # Just echo the valid input

################infinite Loop, not updating variable
# a = 0
# while a < 1000:
#     print(a)

################Did not test for a = 500 condition
# a = 0
# while a < 1000:
#     a +=1
#     if a < 500:
#         print("Boom", a)
#     if a > 500:
#         print('Pow', a)

##Slide 34
# pass
# pass
# pass


##Slide 36
##Dice rolling simulator
# pass
# pass
# pass


##Guess the number game
# import random
#
# myNumber = random.randint(1,100)
# count = 0
#
# while True:
#     count += 1
#     userNumber = int(input("Enter your guess: "))
#     if userNumber < myNumber:
#         print("Too small!")
#     elif userNumber > myNumber:
#         print("Too large!")
#     else:
#         print("Congratulations! You've got it in", count, "tries!")
#         break
