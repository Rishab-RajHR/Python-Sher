class Animal:
   def __init__(self,name):
       self.name = name
  
   def show(self):
       print(f"Hello Your name is {self.name}")
       
class Human(Animal):
   pass      
 
anima1 = Animal("Lion")  # Instance of main class
person1 = Human("Alex")  # Instance of child class

person1.show()