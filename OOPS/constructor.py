class Factory:
    def __init__(self,material,zips,pockets):
        print(self)
        self.material = material
        self.zips = zips
        self.pockets = pockets
        
    def show(self):
        print(f"Your object details are {self.material}, {self.pockets}, {self.zips}")
        
reebok = Factory("Leather",3,2)

campus = Factory("Nylon",3,3)

print(reebok.pockets)
print(campus.pockets)

reebok.show()