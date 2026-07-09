# Print from 1 to 10

# a = 1

# while a <= 30:
#      print(a)
#      a = a + 1


# Separate each digit of a number and print it on the new line.

# a = 256

# while a > 0:
#     print(a % 10)
#     a = a // 10




# Accept a number and print its reverse.

# a = int(input("Tell your number:-"))

# rev = 0

# while a > 0:
#     rev = rev * 10 + a % 10
#     a = a // 10
    
# print(rev)




# Accept a number and check if it is a palindromic number (If number and its reverse are equal)


# a = int(input("Tell your number:-"))

# copy = a
# rev = 0

# while a > 0:
#     rev = rev * 10 + a % 10
#     a = a // 10
    
# if copy == rev:
#     print("Palindromic Number")
# else:
#     print("Not a Palindromic Number")




# Create a random number guessing game with python

import random

num = random.randint(1,10)

tries = 0

while True:

     guess = int(input("Please guess your number :- "))

     if num == guess:
        tries += 1
        print("You are right")
        break
        
     elif num < guess:
        print("You are right you guessed the number in {tries} tries")
        tries += 1
        
     elif num > guess:
        print("Go a little higher")
        tries += 1
        
     else:
        tries += 1
        print("Sorry you are wrong")