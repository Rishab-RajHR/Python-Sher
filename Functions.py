# Inbuilt function

# print("Hello how are you")

# def hello():
#    print("hello function")
   
# hello()


# Function parameters (The thing you accept is parameters)

# Function arguments (The thing you provide is arguments)



# def sum(a,b):   # Parameters
#     print(f"The sum of your numbers is {a + b}")
    
# sum(2,3)   # Arguments
# sum(22,43)   # Arguments



# Positional Arguments

# def hello(name,age):
#     print(f"Your name is {name} and your age is {age}")

# hello("Alex",22)


# Default arguments

# def sum(a,b=34):
#     print(f"The Sum is {a+b}")
  
# sum(12)


#  Keyword arguments

# def hello(name,age):
#     print(f"Your name is {name} and your age is {age}")

# hello(age = 22, name = "Alex")



# Palindrome function

def palindrome(st):
    rev = ""
    for i in range(len(st)-1,-1,-1):
        rev = rev + st[i]
        
    if rev == st:
        print("{st} is a Palindrome")
    else:
        print("{st} is not a Palindrome")
        
palindrome("NAMAN")
palindrome("CURSOR")