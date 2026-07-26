# Polymorphism  => Many Forms

# Method overriding in Python

class Animal:
   def show(self):
       print("Hello I am Alex")
       
class Human(Animal):
   def show(self):
       print("How are you")
       
obj1 = Human()
obj1.show()

# obj1.show()  # Prints How are you
# obj1.show2() # Prints Hello I am Alex