class Factory:
    a = 12  # attribute
    
    def hello(self): #method
        print("How are you")
        
obj = Factory()

# obj2 = Factory()   => We can make many objects

# print(obj.a)
print(obj.hello())