# Without Encapuslation we can do changes

# class Factory:
#    a = 'Pune'
   
#    def show(self):
#        print("Hello I am from Pune Factory")
       
# obj = Factory()

# print(obj.a)



# With Encapsulation data cannot be modified

class Factory:
   _a = "Pune"
   
   def show(self):
       print('Hello I am a Pune Factory')
       
class Bhopal(Factory):
    def show2(self):
        print(super()._a)
        
obj = Bhopal()
obj.show2()