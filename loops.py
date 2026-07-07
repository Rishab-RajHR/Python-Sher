# for loop

# a = range(1,20,1)
# for i in a:
#   print(i)
  
# for i in range(21):
#     print(i)


# for loop in reverse order

# for i in range(16,0,-1):
#    print(i)


# Print the table of 5

# for i in range(5,51,5):
#     print(i)


# Taking the input from the user

# n = int(input("Which table you want ? "))

# for i in range(n,(n*10)+1,n):
#    print(i)



# For loops for strings

# a = "PANDIAN"

# for i in range(7):
#     print(a[i])




# a = "ALEX PANDIAN FROM TANJAVUR"
# print(len(a))

# for i in range(len(a)):
#     print(a[i])


# Run over the string directly

# a = "ALEX IS FROM SOUTH"

# for i in a:
#    print(i)



# Break , Continue and  Pass

# If break runs then else doesn't
# If break does not runs then else runs

for i in range(1,21):
    if i == 15:
      print("Break statement is executed")
      break
    print(i)

else:
   print("Break statement is not executed")