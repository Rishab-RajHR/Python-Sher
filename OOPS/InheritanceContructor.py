class Animal:
   def __init__(self,name):
       self.name = name
  
   def show(self):
       print("Hello Your name is {self.name}")
       
class Human(Animal):
   pass      
 
person1 = Human("Akarsh")

person1.show()