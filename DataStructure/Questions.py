# Print positive and negative elements of an list


g = [-45,67,12,-68,-69,34]

print("Positive elements are")
for c in g:
    if c >= 0:
        print(c)
        
print("Negative elements are")

for c in g:
    if c < 0:
        print(c)




# Mean of list elements

l = [12,435,67,89,23,25,69]

sum = 0

for i in l:
    sum = sum + i
    
print(sum/len(l))




# Find the greatest element and print its index too

t = [4, 67, 128, 34, 88, 6, 20]

largest = t[0]
index = 0

for i in range(len(t)):
    if t[i] > largest:
        largest = t[i]
        index = i
        
print(f"Your largest number is {largest} at index {index}")






# Find the second greatest element
 
 
p = [12,16,13,19]

largest = p[0]
sec_largest = p[0]

for m in p:
    if m > largest:
        sec_largest = largest
        largest = m
    elif m > sec_largest:
        sec_largest = m
        
print(sec_largest, largest)





# Check if List is sorted or not


g = [12,13,14,15,16]

for h in range(len(g)-1):
    if g[h] < g[h+1]:
        continue
    else:
        print("Your list is not sorted")
        break
else:
    print("Your list is sorted")