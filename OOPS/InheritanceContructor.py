class Animal:
   def __init__(self,name):
       self.name = name
  
   def show(self):
       print(f"Hello Your name is {self.name}")
       
class Human(Animal):
   pass      
 
person1 = Human("Alex")

person1.show()