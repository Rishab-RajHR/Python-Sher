class Factory:
    a = 12 # attribute
    
    def hello(self): #method
        print("How are you")
        
    print("Hello how are you I am getting intialized")
    
print(Factory().a)

Factory().hello()