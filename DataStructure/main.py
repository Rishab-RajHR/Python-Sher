# a = 12, 13, 14 ,16
# print(a)

# A list in Python is an ordered, mutable (changeable) collection that can store multiple items of different data types.

a = [12,13,14,15,16,34.5,True,print()]

print(a[0:5:1])  # slicing [start:end:steps] 
print(a[-1])   # Last Index

print(a[1])


# Run a loop over list

b = [12,13,14,15,16,34.5]

# 1st way using index

for i in range(len(a)):
    print(a[i])
    
# 2nd way directly on values

for i in a:
   print(i)    
   
   
# List of methods

# print(dir(list))


# Append => Add the value at the last

l = [1,2,3,4,5]

l.append(6)
l.append(7)

print(l)



# insert the value at the position

k = [1,3,4,5]

k.insert(1,2)
# l.remove(3)  => removes the first occurence

print(k)


# Accessing the index value and updating the value
m = [1,2,3,2,4,5]

m[0] = 10
print(m)




# Using the for loop to access the value

g = [-45,67,12,-68,-69,34]

print("Positive elements are")
for c in g:
    if c >= 0:
        print(c)
        
print("Negative elements are")

for c in g:
    if c < 0:
        print(c)