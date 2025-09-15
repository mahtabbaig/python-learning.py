#list

list=["mahtab", "mohit", "manoj", "paksh"]
print(list)
print(type(list))
print(list[1])
list[1]="prem"
print(list)

## length of list
list=["mahtab", "mohit", "manoj", "paksh"]
print(len(list))

## list slicing
list=["mahtab", "mohit", "manoj", "paksh"]
print(list[0:3])
print(list[:4])
print(list[0:])
print(list[-4:-1])

## list method

###list.append:
list=["mahtab", "mohit", "manoj", "paksh"]

list.append("prem")
print(list)

###list.sort:
list==["mahtab", "mohit", "manoj", "paksh"]
list.sort()
print(list)

###list.sort(reverse=True):
list=["mahtab", "mohit", "manoj", "paksh"]
list.sort(reverse=True)
print(list)

###list.reverse:
list=["mahtab", "mohit", "manoj", "paksh"]
list.reverse()
print(list)

###list.insert:
list=["mahtab", "mohit", "manoj", "paksh"]
list.insert(4,"rahul")
print(list)

###list.remove:
list=["mahtab", "mohit", "manoj", "paksh", "mohit"]
list.remove("mohit")
print(list)

###list.pop:
list=["mahtab", "mohit", "manoj", "paksh"]
list.pop(3)
print(list)

#tuples
tuples=("mahtab","manoj","prem")
print(type(tuples))
print(tuples)



##slicing in tuples
tuples=("mahtab","manoj","prem")
print(tuples[0:2])

## tuples methods:
 ###tup.index:
tuples=("mahtab","manoj","prem")
print(tuples.index("prem"))

###tup.count:
tuples=("mahtab","manoj","prem")
print(tuples.count('manoj'))


 





