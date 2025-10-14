# oop in Python

 ## class and objects:
class student: #class
    name="mahtab"
    age=18
s1=student() #object
print(s1.age,s1.name)

##__init__functions:
class bank:
    
  def __init__(self,branch,acc):
    self.branch=branch
    self.acc=acc
cat1=bank("canara","current")
print(cat1.branch,cat1.acc)   

## methods:
class Student:
   def __init__(self,name,roll,achivement):
      self.name=name
      self.roll=roll
      self.achivement=achivement
   def greeting(self):
        print("welcome to my college",self.name)
   def record(self):

    print("student name:",self.name,"\nroll no:",self.roll)
    print("I am gold medalist in",self.achivement)
s1=Student("mahtab",240,"cricket")
s1.greeting()
s1.record()

## static method
class student:
   @staticmethod
   def college():
      print("nie")
   college()      

##del key:
class rent:
   def __init__(self,name,roll):
      self.name=name
      self.roll=roll
s1=rent("mahtab",240)
del s1.name
print(s1.roll)      

##Private:
class home: 
   def __init__(self,name):
      self.__name=name
   def __hello(self):
      print("welcome",self.__name)
   def welcome(self):
     self.__hello()  
s1=home("mahtab") 
s1.welcome()  

## inheritance:
class report:
   @staticmethod
   def blood():
      print("blood is A+")
   @staticmethod
   def cancer():
      print("cancer test is -ve")
class haemoglobin(report):
   def __init__(self,name):
      self.name=name

            
repo1=haemoglobin("TB")
print(repo1.name,repo1.cancer())

## super method:              
class report:
   @staticmethod
   def blood():
      print("blood is A+")
   @staticmethod
   def cancer():
      print("cancer test is -ve")
class haemoglobin(report):
   def __init__(self,name):
      self.name=name
class result(haemoglobin):
   def __init__(self, colour,name):
      super().__init__(name)
      self.colour=colour
      super().blood()
            
repo1=result("TB","black")
print(repo1.name,repo1.colour,repo1.cancer())

## classmethod:
class person:
   name="mahtab"
   @classmethod
   def change(cls,name):
      cls.name=name
s1=person()
s1.change("shabreen")
print(person.name)     

class nie:
   def __init__(self,phy,che,math):
      self.phy=phy
      self.che=che
      self.math=math
   @property
   def percentage(self):
      return str((self.phy+self.che+self.math)/3) +"%"
stud1=nie(95,94,98)
print(stud1.percentage )
stud1.phy=100
print(stud1.percentage)

#3 polymorphism:
class complex:
   def __init__(self,real,image):
      self.real=real
      self.image=image
   def __add__(self,other):
      real1=self.real+other.real
      real2=self.image+other.image
      return complex(real1,real2)
   def show(self):
      print(self.real,"i +",self.image,"j")
num1=complex(2,4)
num2=complex(1,3)
num3=num1+num2
num3.show()                   