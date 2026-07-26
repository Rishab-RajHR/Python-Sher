#  Private Method that cannot be accessed from anywhere

class Factory:
   __a = "Pune"
   
   def show(self):
      print("Hello I am a Pune Factory")
      
class Bhopal(Factory):
   def show2(self):
      print(super().__a)
      
obj = Bhopal()
obj.show2()