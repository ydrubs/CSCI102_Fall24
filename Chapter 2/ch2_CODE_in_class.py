# ##Slide 2
age = 122 #age of the oldest ever living person

#give the age of the person
# print(age)
#
"""
Sometimes there is a need to explain or document a portion of code beyond one line.
For this we can use a docstring to extend to multiple lines.
Docstrings are also used to attribute programs and explain functions.
"""

##Slide 5
a = 2
b = a
# print(id(a))
# print(id(b))

# c = float(input("how old are you: "))
# print(c, type(c))

# print(234_5_6_7_8_9_0)




##Slide 7
# print('A wise person once said, fail often')
# print("This is a 'bad' \nquote")


# print("A double quoted string")
# print('does the same thing as a single quoted string')
#
# print("However, there'll be times when a string needs to include a single quote within it, so a double quote is useful.")

##Printing Multiline strings
# welcomeText = '''Welcome to my game!
#             I will think of a number from 1 to 100, and you must try
#             to guess it. I'll tell you if your guess is too small
# or too large.
# Enter an integer between 1 and 100 when prompted.'''
# print(welcomeText)


##Slide 8
# print("1. hello " + 'there') #Substitute one of the escape chars for the '#'
# print("2. hello\b " + ' there')
# print("3. hello\n " + ' there')
# print("4. hello\t " + ' there')
# print("5. hello\\ " + ' there')
# print("6. hello\' " + 'there')
# print("7.hello\" " + ' there')
#
# s1 = "Green eggs and ham"
# s2 = 'Sam-I-am'
# s3 = 'I like the backslash (\\) character!'
# s4 = "I do not like them\n Sam-I-am!"
# print(s4)

###Activity - slide 9 Experiment with escape character in the space below



##Slide 10
# print("Hello")
# print("there")
# #
#
# var = ':::;;;'
# print("Hello", end=var)
# print('there')


##Slide 11
name = 'Yoda'
age = 900
home_planet = 'Dagobah'
#
# print(name, age, home_planet)
# print(name, age, home_planet, sep = '\n')
# print(name, age, home_planet, sep = 'Iluffstarwars')
# print()
# print()

##slide 12
# def = 2 # not allowed
# 1age = 30 # Can't do

# age1 = 30
# $name = 'Yuriy'

# my_name = 'Yuriy'
# _name = 'Yuriy'
# @name = "yuriy" #can't do

# NAME = 'yuriy'
# print(NAME)
#
# my_name = 'bob'
# age = 0

###Activity


##Slide 14
# first_name = "Obi-Wan"
# last_name = "Kenobi"
# full_name = first_name + ' ' +  last_name
# print(full_name)


# #Reassigning Variables to new values
x = 125
y = x / 5    # y defined in terms of x
# print(type(y))

# print(x, y)
# #
x = 100    # redefining x
# print(x, y)
# #
y = 2 * y    # redefining y by modifying
# print(x, y)

##Slide 15
first_name = 5
last_name = 6
#
# print(first_name, last_name)
# print(first_name + last_name )


s1 = 'waaz'
s2 = 'a'
s3 = 'p'
# print((s1 + s2*5 +s3 + ' :) ')*3)
# print(pass)


###ACTIVITY slide 16
symbol1 = '^'
symbol2 = '#'
# print((symbol1*10 + '\n') + ((symbol2*10 + '\n')*3) + (symbol1*10 + '\n'))

##Operations
a = 3
b = 4
# print(a**b)
#
# print(b/a)
# print(b//a)

# print(a/b) # 3/4
# print(a//b)

# print(11%3)


##Slide 18 - Examples of right associative
# print(2**3**4)
# print(2**81)
#
# a = 1
# a = a + 1
# print(a)



## Slide 20
# a = 6
# b = 3
# print(pass, type(a))
# print(pass, type(a/b))
# print(pass, type(a//b))
#
# pass
# pass
# pass

#Slide 23
# print(round(6.75))
# print(round(6.75,0))
# print(round(6.75,1))
# print(round(6.75,2))
# print(round(6.75,3))

##Slide 24
# print(chr(ord('a')))
print(ord('~')+100)
print(chr(123457))

# s1 = "Mary Poppins"
# s2 = "Freddy"

# print(pass) #Get the lenght of string s1 and s2
# print(pass) # Get the ASCII code of the character
# print(pass) #Get the character from the ASCII code
# print(min(s2), max(s2)) #Find the smallest and largest ASCII character of s2


##Playing around with some character codes in unicode
# print(chr(0x265e))
# print(chr(0x250C))
# print(chr(103436))

# print(int(0x265e))
#
# print('The ASCII code for the letter \'a\' is ' + str(ord('a')))

for i in range (9000, 10000):
    print(chr((i)), end = ', ')

