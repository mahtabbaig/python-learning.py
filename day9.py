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