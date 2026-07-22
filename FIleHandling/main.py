from pathlib import Path

def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
       print(f"{i+1} : {items} ")
    

def createfile():
    pass
  
print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deletion a file")

check = int(input("Please Tell Your Response :- "))

if check == 1:
    createfile()