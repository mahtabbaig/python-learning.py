#Files I/O in python:
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