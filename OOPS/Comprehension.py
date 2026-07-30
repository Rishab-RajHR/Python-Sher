# List Comprehension --> Gets the result in one line

l = []
for i  in range(1,21):
    if i % 2==0:
        l.append(i)
        
print(l)