# With the help of (*args) we can pass any number of arguments

# def addition(*args):
#     sum = 0
#     for i in args:
#         sum = sum + i
        
#     print(sum)
    
# addition(12,14,16,18)




# keyword argument (**kwargs)


# def addition(**kwargs):
#     print(kwargs)
    
# addition(a=12, b=56, c=78)



def information(**kwargs):
    print("Your Information is \n\n ")
    for i in kwargs:
        print(f"{i} : {kwargs[i]}")
        
        
information(name="Alex", age=23, designation="AI/ML")