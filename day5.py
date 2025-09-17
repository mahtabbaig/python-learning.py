# Dictionary:
dict = {
    "Name" :"mahtab",
    "college":["nie"],
    "learning": ["python"],
    "age":19,

}

dict["Name"]="shabreen"
dict["surname"]="taj"
print(dict)

##nested dictionary:
student={
    "name":"mahtab",
    "subject":{
        "phy":95,
        "chem":94,
        "maths":98,
    }
}

print( student["subject"]["chem"])

##dictionary methods:
### 1.keys:
student={
    "name":"mahtab",
    "subject":{
        "phy":95,
        "chem":94,
        "maths":98,
    }
}
print(list(student.keys())) # we canignore list
           #or
print(student.keys())           

### 2. values:
student={
    "name":"mahtab",
    "subject":{
        "phy":95,
        "chem":94,
        "maths":98,
    }
}
print(list(student.values()))

### 3.items:
student={
    "name":"mahtab",
    "subject":{
        "phy":95,
        "chem":94,
        "maths":98,
    }
}
print(list(student.items()))

### 4.get:
student={
    "name":"mahtab",
    "subject":{
        "phy":95,
        "chem":94,
        "maths":98,
    }
}
print(student.get("name"))

### 5.update:
student={
    "name":"mahtab",
    "subject":{
        "phy":95,
        "chem":94,
        "maths":98,
    }
}
new_dict={"name":"jaffar",}
student.update(new_dict)
print(student)


# Sets :

collection={"mahtab",1,2}
print(type(collection))
print(collection)
print(len(collection))

##empty set:
collection=set()
print(collection)
print(type(collection))

## methods of set:
### 1.add:

collection={"mahtab",1,2}
collection.add(4)
print(collection)

### 2. remove:

collection={"mahtab",1,2}
collection.remove("mahtab")
print(collection)

### 3. clear:

collection={"mahtab",1,2}
collection.clear()
print(collection)

### 4. pop:

collection={"mahtab",1,2}
collection.pop()
print(collection)
print(collection.pop())

### 5.union:

collection1={"mahtab",1,2}
collection2={2,3,1}
print(collection1.union(collection2))

### 6.intersection:


collection1={"mahtab",1,2}
collection2={1,1,2}
print(collection1.intersection(collection2))








