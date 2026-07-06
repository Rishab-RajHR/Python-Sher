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


n = int(input("Check your number is perfect or not :- "))
sum = 0
for i in range(1,n):
    if n%i == 0:
       sum = sum + i

if sum == n:
   print("Your number is perfect")
else:
   print("Your number is not a perfect number")
