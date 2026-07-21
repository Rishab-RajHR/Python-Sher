# try, except, else, finally , raise



# Without Exception Handling

# a = int(input("Tell your Number :- "))
# print(10/a)
# print("Ok I have done the division")


# With Exception Handling

a = int(input("Tell your Number :- "))

try:
   print(10/a)
  
except Exception as err:
   print(f"Sorry there is an err as {err}")
   
print("Ok I have done the division")


# Another Example

b = input("Tell your Number :- ")

try:
   print(10/b)

except Exception as err:
   print(f"Sorry there is an err as {err}")
   
print("Ok I have done the division")



# Use of else block

c = int(input("Tell your number :- "))

try:
   print(10/c)
   
except Exception as err:
  print(f"sorry there is an err as {err}")
  
else:
   print("Good there is no exception")
   
print("Ok I have done the division")


# Finally block will execute no matter what

d = int(input("Tell Your Number :- "))

try:
   print(10/d)
  
except Exception as err:
   print(f"Sorry there is an err as {err}")
   
else:
   print("Good there is no exception")
  
finally:
   print("I will run no matter what")
   
   
   
# raise -> Manually throws an exception

age = int(input("Tell your Age :- "))

try:
  
   if age < 10 or age > 18:
     raise ValueError("Your age must be between 10 and 18")
   else:
     print("Welcome to the club")
    
except Exception as err:
    print(f"An error occured as {err}")
   
print("The club will start soon")

