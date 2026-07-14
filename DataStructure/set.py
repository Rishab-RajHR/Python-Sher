# A set in Python is an unordered, mutable collection of unique elements. It automatically removes duplicate values and is commonly used for membership testing and mathematical set operations.

s = {1,2,3,4,4,5}

print(s)


# Hashing of string
b = hash("Hello")
print(b)

# Hashing a tuple
c = hash((1,2,334))
print(c)


# Integer will be sorted automatically
a = {1,8,9,2,3,4,5}

for i in a:
    print(i)
    
    
# Remove the set value

k = {1,2,3,4}

k.remove(2)

print(k)



# Set OPerations

l = {1,2,3,4,5}
m = {4,5,6,7,8}

t = l|m  # Union
q = l.intersection(m)  # Intersection
r = l&m  # And
u = l.difference(m)   # Difference (l-m)
i = l.symmetric_difference(m) # Symmetric Difference (l^m)
m -= l
 
print(t)
print(q)
print(r)
print(u)
print(i)
print(l)