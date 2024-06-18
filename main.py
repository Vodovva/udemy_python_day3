# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# # If Statement

# if height >= 120:
#     print('You can ride the rollercoaster!')
# else:
#     print('Sorry you have to grow taller before you can ride.')


# Comparison Operators
# Greater than >
# Less than <
# Greater than or equal to >=
# Less than or equal to <=
# Equal to ==
# Not equal to !=
    


# Lesson 1
    
# Write a program that works out whether if a given number is an odd or even number.
# Even numbers can be divided by 2 with no remainder.e.g. 86 is even because 86 ÷ 2 = 43
#43 does not have any decimal places. Therefore the division is clean.
# e.g. 59 is odd because 59 ÷ 2 = 29.5
# 29.5 is not a whole number, it has decimal places. Therefore there is a remainder of 0.5, so the division is not clean.
# The modulo is written as a percentage sign (%) in Python. It gives you the remainder after a division.
# e.g.
# 6 ÷ 2 = 3 with no remainder.
# therefore: 6 % 2 = 0
# 5 ÷ 2 = 2 x 2 + 1, remainder is 1.
# therefore: 5 % 2 = 1
# 14 ÷ 4 = 3 x 4 + 2, remainder is 2.
# therefore: 14 % 4 = 2
# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.
# Example 1 Input
# 43
# Example 1 Output
# This is an odd number.
    
# # Which number do you want to check?
# number = int(input())
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇
# if number % 2 == 0:
#     print('This is an even number.')

# else:
#     print('This is an odd number.')

# Else Statement


# /Nested if/else statement
# if condition:
#     if another condition:
#     else: 
#         do this
# else:
#     do this


# <12 $5
# 12 - 18 $7
# > 18 $12


# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print('You can ride the rollercoaster!')
#     age = int(input('What is your age?'))
#     if age <= 18:
#         print('Please pay $7.')
#     else:
#         print('Please pay $12.')
# else:
#     print('Sorry you have to grow taller before you can ride.')


#  Elif s are endless you can add as many as you want. 
# <12 $5
# 12 - 18 $7
# > 18 $12
    
# if height >= 120:
#     print('You can ride the rollercoaster!')
#     age = int(input('What is your age?'))
#     if age < 12:
#         print('Please pay $5.')
#     elif age <= 18:
#         print('Please pay $7')
#     else:
#         print('Please pay $12.')
# else:
#     print('Sorry you have to grow taller before you can ride.')


# Lesson 2 actually
    
# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
# It should tell them the interpretation of their BMI based on the BMI value.
# Under 18.5 they are underweight
# Equal to or over 18.5 but below 25 they have a normal weight
# Equal to or over 25 but below 30 they are slightly overweight
# Equal to or over 30 but below 35 they are obese
# Equal to or over 35 they are clinically obese.
    
# Enter your height in meters e.g., 1.55
# height = float(input())
# # Enter your weight in kilograms e.g., 72
# weight = int(input())
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# bmi = weight / (height * height)
# if bmi < 18.5:
#     print(f'Your BMI is {bmi}, you are underweight')
# elif bmi < 25:
#     print(f'Your BMI id {bmi}, you have a normal weight.')
# elif bmi < 30:
#     print(f'Your BMI is {bmi}, you are slightly overweight.')
# elif bmi < 35:
#     print(f'Your BMI is {bmi}, you are obese.')
# else:
#     print(f'Your BMI is {bmi}, you are clinically obese.')


# Lesson 3
# Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice.
# This is how you work out whether if a particular year is a leap year.
# on every year that is divisible by 4 with no remainder
# except every year that is evenly divisible by 100 with no remainder
# unless the year is also divisible by 400 with no remainder
# If english is not your first language or if the above logic is confusing, try using this flow chart .
# e.g. The year 2000:
# 2000 ÷ 4 = 500 (Leap)
# 2000 ÷ 100 = 20 (Not Leap)
# 2000 ÷ 400 = 5 (Leap!)
# So the year 2000 is a leap year.
# But the year 2100 is not a leap year because:
# 2100 ÷ 4 = 525 (Leap)
# 2100 ÷ 100 = 21 (Not Leap)
# 2100 ÷ 400 = 5.25 (Not Leap)
# Warning your output should match the Example Output format exactly, including spelling an punctuation.

# Which year do you want to check?
# year = int(input())
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇

# if year % 4 == 0:
#     if year % 100 == 0:
#         # Not a leap year, unless special case
#         if year % 400 == 0:
#             print('Leap year')
#         else:
#             print('Not leap year')
#     else:
#         print('Leap year')

# else:
#     print('Not leap year')



# Multiple If Statements in Succession
# if condition1:
#     do A
# if condition2:
#     do B
# if:
#     do C



# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0

# if height >= 120:
#     print('You can ride the rollercoaster!')
#     age = int(input('What is your age?'))
#     if age < 12:
#         bill = 5
#         print('Child tickets are $5.')
#     elif age <= 18:
#         bill = 7
#         print('Youth tickets are $7')
#     else:
#         bill = 12
#         print('Adult tickets are $12.')
        
#     wants_photo = input('Do upi want a photo taken? Y or N.')
#     if wants_photo == 'Y':
#         #Add $3 to their bill
#         bill += 3

#     print(f'Your final bill is {bill}')

# else:
#     print('Sorry you have to grow taller before you can ride.')




# Lesson 4
# Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.
# Based on a user's order, work out their final bill.
# Small pizza (S): $15
# Medium pizza (M): $20
# Large pizza (L): $25
# Add pepperoni for small pizza (Y or N): +$2
# Add pepperoni for medium or large pizza (Y or N): +$3
# Add extra cheese for any size pizza (Y or N): +$1


# print("Thank you for choosing Python Pizza Deliveries!")
# size = input() # What size pizza do you want? S, M, or L
# add_pepperoni = input() # Do you want pepperoni? Y or N
# extra_cheese = input() # Do you want extra cheese? Y or N
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇
# bill = 0

# if size == 'S':
#     bill = 15
# elif size == 'M':
#     bill = 20
# else:
#     bill += 25


# if add_pepperoni == 'Y':
#     if size == 'S':
#         bill += 2
#     else:
#         bill += 3
# if extra_cheese == 'Y':
#     bill += 1

# print(f'Your bill is ${bill}')


# Logical Operators
# And  / Or / Not
# a = 12
# a > 15
# False
# a > 10 
# True
# a > 10 and a < 13
# True
# a > 15 and a <13
# False


# # Adding additional elif conditions
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0

# if height >= 120:
#     print('You can ride the rollercoaster!')
#     age = int(input('What is your age?'))
#     if age < 12:
#         bill = 5
#         print('Child tickets are $5.')
#     elif age <= 18:
#         bill = 7
#         print('Youth tickets are $7')
#     elif age >= 45 and age 55:
#         print('Everything is going to be ok. Have a free ride on us!')
#     else:
#         bill = 12
#         print('Adult tickets are $12.')
        
#     wants_photo = input('Do upi want a photo taken? Y or N.')
#     if wants_photo == 'Y':
#         #Add $3 to their bill
#         bill += 3

#     print(f'Your final bill is {bill}')

# else:
#     print('Sorry you have to grow taller before you can ride.')




# Lesson 5
# 💪 This is a difficult challenge! 💪
# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs.
# Then check for the number of times the letters in the word LOVE occurs.
# Then combine these numbers to make a 2 digit number.
# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is *x*, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
# "Your score is *y*, you are alright together."
# Otherwise, the message will just be their score. e.g.:
# "Your score is *z*."
# e.g.
# name1 = "Angela Yu"
# name2 = "Jack Bauer"
# T occurs 0 times
# R occurs 1 time
# U occurs 2 times
# E occurs 2 times
# Total = 5
# L occurs 1 time
# O occurs 0 times
# V occurs 0 times
# E occurs 2 times
# Total = 3
# Love Score = 53
# Print: "Your score is 53."


print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count('t')
r = lower_names.count('r')
u = lower_names.count('u')
e = lower_names.count('e')
first_digit = t + r + u +e

l = lower_names.count('l')
o = lower_names.count('o')
v = lower_names.count('v')
e = lower_names.count('e')
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))
if (score < 10) or (score > 90):
    print(f'Your score is {score}, you go together like coke and mentos.')
elif (score >=40) and (score <=50):
    print(f'Your score is {score}, you are alright together.')
else:
    print(f'Your Score os {score}.')













