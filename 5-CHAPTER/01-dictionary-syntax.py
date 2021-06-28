myDict = {
    "Fast" : "In a Quick maneer",
    "Vrushabh": "A coder",
    "Marks": [25,30,35,40],
    "anotherDict": {
        "name":"Ravi",
        "rollNo": 52
    }
}

print(myDict.get("Fast")) # ---->>> print(myDist["Fast"])
print(myDict["Vrushabh"])
print(myDict["Marks"]) # ----->>> [25, 30, 35, 40]

print(myDict["anotherDict"]["name"]) # ----->>> Ravi

# Dictionary is mutable
myDict["Marks"] = [75, 80, 45, 23]

print(myDict["Marks"])