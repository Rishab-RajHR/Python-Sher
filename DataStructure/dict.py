d = {1:'Hello',2:34}
print(type(d))

# Keys must be unique and values are not unique

# Keys and values can be of any type


d = {10:100, 20:200, 30:300, 40:400}

# d[10] = 100
# print(d)


# Updating the value
# d.update({50:500})
# print(d)

# d[10] = 100  # updating
# d[50] = 500  # creating
# del d[30]  # deleting


# For iterating over dict

# d = {10:100,20:200,30:300,40:400}

# for i in d:
#     print(i)
#     print(d[i])   # For accessing the value
    
    
# Another Method
# for i in d.values():
#     print(i)


# print(d[10])


# help(dict)  => Dictionary Methods


# d = {10:100,20:200,30:300,40:400}

# d.clear()



# Shallow Copy and Deep Copy

# Shallow Copy
# a = [1,2,3,4,5]

# b = a

# b[0] = 100

# print(a)


# Deep Copy
# a = [1,2,3,4,5]

# b = a.copy()

# b[0] = 100

# print(a)


d = {10: 100, 20: 200, 30:300, 40:400}

print(d.items())

