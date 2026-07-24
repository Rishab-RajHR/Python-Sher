# Syntax for Inheritance

class FactoryMumbai: #parent class / superclass
   a = "I am an attribute mentioned inside Factory"
   def hello(self):
       print("Hello I am a method mentioned inside Factory")
       
class FactoryPune(FactoryMumbai): #Child class / subclass
  pass

obj = FactoryMumbai()

obj2 = FactoryPune()

print(obj2.hello())

print(obj.a)
    