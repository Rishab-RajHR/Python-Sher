# class Animal:
#     def __init__(self,name):
#        pass
   
# class Human:
#   def __init__(self,name,age):
#      pass
   
# class Robots(Animal,Human):
#     name3 = "Alex1213"
    
# obj = Robots()



# Multilevel Inheritance

class Factory:
   def __init__(self,material,zips):
       self.material = material
       self.zips = zips
       
class BhopalFactory(Factory):
    def __init__(self, material, zips, color):
        super().__init__(material, zips)
        self.color = color
        
class PuneFactory(BhopalFactory):
    def __init__(self, material, zips, color, pockets):
        super().__init__(material, zips, color)
        self.pockets = pockets
        
