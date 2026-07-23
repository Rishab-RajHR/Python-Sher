class Factory:
    def __init__(self,material,zips,pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets
        
reebok = Factory("Leather",3,2)

campus = Factory("Nylon",3,3)

print(reebok.pockets)
print(campus.pockets)