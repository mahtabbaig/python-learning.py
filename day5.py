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


