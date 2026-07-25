# Attribute are function created within the class

class Animal:
   name = "Lion"  # class attribute
   
   def __init__(self, age):
      self.age = age  # Instance attribute
      
   def show(self):  # instance method
     print(f"How are you old {self.age}")
     
    
   @classmethod
   def hello(cls):
        print("How are you Brother")
        
   @staticmethod
   def static():
       print("How are you")
       
       
obj = Animal(12)

obj.show()
# obj.hello()  