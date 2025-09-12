# strings

##escape sequence character
1.
funct="My name is mahtab.\nI am a computer science engineering."
print(funct)
2.
str="My name is mahtab.\tI am a computer science engineering."
print(str)

## basic operators

###concatenation
a="hello"
b="world"
print(a+b)

a="hello"+" "+"world"
print(a)
print(len(a))

###length of string
str="mahtab baig"
print(len(str))

###indexing
str="magtab baig"
print(str[2])
print(str[0:])

###slicing
str="mahtab"
print(str[-3:-1])

##string function
1.
str= "my name is mahtab"
print(str.endswith("ab"))
print(str.endswith("ed"))

2.
str="my name is mahtab"
print(str.capitalize())
a=str.capitalize()
print(a)
print(str)

3.
str="My name is mahtab"
print(str.replace("mahtab","shabreen"))

4.
str="My name is mahtab"
print(str.find("is"))

5.
str="My name is mahtab"
print(str.count("name"))

#conditional statements
## if
fine=1000
if(fine>=1000):
    print("fine is approved")

##elif
fine=1000
if(fine>=2000):
    print("fine not payed")
elif(fine>=800):
    print("fine is payed")    

##else
fine=1000
if(fine>=2000):
    print("not payed")
elif(fine>=2500):
    print("fine not payed")
else:
    print("payment is done")            
    
