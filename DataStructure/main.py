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
