#  Private Method that cannot be accessed from anywhere

# class Factory:
#    __a = "Pune"
   
#    def show(self):
#       print("Hello I am a Pune Factory")
      
# class Bhopal(Factory):
#    def show2(self):
#       print(super().__a)
      
# obj = Bhopal()
# obj.show2()



class Demo:
   def __init__(self):
      self.name = "Public Member"   # Public
      self._age = 21                # Protected
      self.__salary = 50000         # Private
      
   def show(self):
       print("Inside the class:")
       print("Public:", self.name)
       print("Protected:", self._age)
       print("Private:", self.__salary)