#Files I/O in python:

##file reading
1.
f=open("day1.py","r")

data=f.read()
print(data)

f.close()

2.
f=open("day1.py","r")

data=f.read()
print(data)
line1=f.readline()
line2=f.readline()
print(line1,line2)
f.close()

## file writing
with open("day1.py","w")as f:
    data=f.write("mahtab")
    



## file append
with open("day1.py","a")as f:
    data=f.write("azeez")
    
## file r+
with open("day1.py","r+")as f:
    data=f.write("brother")
    
## file w+
with open("day1.py","w+")as f:

    data=f.read()
    print(data)

#deleting file

import os
os.remove("day9.py")

    

 

