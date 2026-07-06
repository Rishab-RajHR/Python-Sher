#  Which number is greater


# num1 = int(input("Please tell your first number "))
# num2 = int(input("Please tell your second number "))

# if num1 > num2:
#     print(f"{num1} is greater than {num2}")
# elif num2 > num1:
#     print(f"{num2} is greater than {num1}")
# else:
#     print("Both the numbers are same")




# Greet on the basis of Gender

# gen = input("Please tell your gender as character (M or F):-")

# if gen == 'M' or gen == 'f':
#    print("Good morning SIR")
# elif gen == 'F' or gen == 'f':
#    print("Good morning MAM") 
# else:
#     print("Unidentified")



# Check which number is Even or Odd

# num = int(input("Please tell your Number :- "))

# if num%2 == 0:
#   print("Even Number")

# else:
#   print("Odd Number")




# Check whether the user is valid voter or not

# name = input("Please tell your name : - ")
# age = int(input("Now tell your age : - "))

# if age >=18:
#     print(f"Hello {name} you are a valid voter")

# else:
#     print(f"Hello {name} you are not a valid voter")





# Check Leap year 

# year = int(input("Tell Your Year :- "))

# if year %100 == 0 and year % 400 == 0:
#     print("Its a leap year")

# elif year %100 != 0 and year %4 == 0:
#     print("Its a leap year")
    
# else:
#    print("It's a normal year")




# If elif ladder

t = int(input("Please tell the temperature :- "))

if t < 0:
   print("Freezing cold")
   
elif t >= 0 and t < 10:
  print("Very Cold")
  
elif t >= 10 and t < 20:
  print("Cold")
  
elif t >= 20 and t < 30:
  print("Pleasant")
  
elif t >= 30 and t < 40:
  print("Hot")
  
else:
   print("Temperature is very Hot")

