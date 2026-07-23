from pathlib import Path
import os

def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
       print(f"{i+1} : {items} ")
    

def createfile():
    try:
       readfileandfolder()
       name = input("Please Tell your File Name :- ")
       p = Path(name)
       if not p.exists():
           with open(p,"w") as fs:
             data = input("What you want to write in this file :- ")
           fs.write(data)
       
           print(F"FILE CREATED SUCCESSFULLY")
       else:
          print("This file already exist")
       
    except Exception as err:
        print(f"An error occured as {err}")   
        
        
def readFile():
    try:
       readfileandfolder()
       name = input("Which file you want to read")
       p = Path(name)
       if p.exists() and p.is_file():
           with open(p,'r') as fs:
               data = fs.read()
               print(data)
          
           print("Readed Successfully")
       else:
          print("The File doesnot exist")
    except Exception as err:
       print("An error occured as {err}")
       

def updateFile():
    try:
        readfileandfolder()
        name = input("Tell which file you want to update :- ")
        p = Path(name)
        if p.exists() and p.is_file():
                 print("Press 1 for changing the name of your file :- ")
                 print("Press 2 for overwriting the data of your file :- ")
                 print("Press 3 for appending some context in your file :- ")
                
                 res = int(input("Tell your response :- "))
                
                 if res == 1:
                    name2 = input("Tell your new file name :- ")
                    p2 = Path(name2)
                    p.rename(p2)
                   
                 if res == 2:
                    with open(p, 'w') as fs:
                        data = input("Tell what you want to write this is overwrite the data")
                        fs.write(data)
                        
                 if res == 3:
                     with open(p, 'a') as fs:
                         data = input("Tell what you want to append :- ")
                         fs.write(" "+data)
                         
    except Exception as err:
         print("An error occured as {err}")
                
def deleteFile():
    try:
       readfileandfolder()
       name = input('Which File you want to delete :- ')
       p = Path(name)
       
       if p.exists() and p.is_file():
          os.remove(p)
          
          print('File removed successfully')

       else:
           print("No such file exist")
           
    except Exception as err:
      print("An error occured as {err}")

  
print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deletion a file")

check = int(input("Please Tell Your Response :- "))

if check == 1:
    createfile()
    
if check == 2:
    readFile()
    
if check == 3:
    updateFile()
    
if check == 4:
    deleteFile()