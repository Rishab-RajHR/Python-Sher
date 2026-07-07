# Print Hello World n number of times by taking the innput

# n = int(input("Please tell your number:-"))

# for i in range(n):
#     print("Hello World")



# Print natural number upto n

# n = int(input("Please tell your number:-"))

# for i in range(1,n+1):
#     print(i)




# Reverse for loop

# n = int(input("Please tell your number:-"))

# for i in range(n,0,-1):
#     print(i)




# Print the table by taking the input

# n = int(input("Which Table you want:-"))

# for i in range(1,11):
#    print(f"{n} * {i} = {n*1}")




# sum upto n terms

# a = 10
# a = a + 5  => a += 5
# print(a)


# n = int(input("Please tell your number:-"))

# sum = 0

# for i in range(1,n+1):
#    sum = sum + i
# print(f"Your sum is {sum}")






# Factorial of a number

# n = int(input('Enter the number:-'))

# fact = 1

# for i in range(1,n+1):
#     fact = fact * i

# print(f"Your factorial is {fact}")




#  Print the sum of all even & odd numbers in a range separately.

# n = int(input("Tell Your number:- "))
# even = 0
# odd = 0
# for i in range(1,n+1):
#     if i%2 == 0:
#         even = even + i
#     else:
#         odd = odd + i

# print(f"Your even and odd sum are {even} , {odd}")





#  Print all the factors of a number


# n = int(input("Which number factors you want :- "))

# for i in range(1,n+1):
#     if n%i == 0:
#        print(i)






#  Accept the number and check if it is a perfect number or not.


# n = int(input("Check your number is perfect or not :- "))
# sum = 0
# for i in range(1,n):
#     if n%i == 0:
#        sum = sum + i

# if sum == n:
#    print("Your number is perfect")
# else:
#    print("Your number is not a perfect number")




# Check whether the number is prime or not

# n = int(input("Check your number is prime or not:-"))

# count = 0

# for i in range(1,n+1):
#     if n%i == 0:
#         count = count + 1

# if count == 2:
#    print("Your number is prime")
# else:
#    print("Your number is not prime")




# Reverse string without using the build function

# a = "PANDIAN"

# b = ""
# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]

# print(b)




# Check string is Palindrome or not

# a = "MADAM"

# b = ""
# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]
   
# if b == a:
#    print("Your String is Palindrome")
# else:
#    print("Its not a Palindrome")





# Count all letters, digits, and special symbols from a given string

a = "sdfibs@#%^&&*()1231"

char = 0
dig = 0
spchar = 0

for i in a:
    if i.isdigit():
       dig += 1
    elif i.isalpha():
        char += 1
    else: 
       spchar += 1
       
print(f"Your digits are {dig}\nYour alphabets are {char}\nYpur special characters are {spchar}")          
       

