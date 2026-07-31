# a = [1,2,3,4,5]

# result = map(lambda x : x*2, a)

# print(list(result))


# Without Lambda Function

# a = [1,2,3,4,5]

# def double(x):
#     return x * 2
  
# result = map(double,a)

# print(list(double))   




#  Filter Method

# def even(x):
#     if x%2 == 0:
#         return True
#     else:
#         return False
    
# a = [1,2,3,4,5,6,7,8,9]

# result = filter(even, a)

# print(list(result))



# Filter Method with Lambda

a = [1,2,3,4,5,6,7,8,9]

result = filter(lambda x : True if x%2 == 0 else False , a)

print(list(result))