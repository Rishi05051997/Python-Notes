myDict = {
    "fast" : "In a Quick maneer",
    "vrushabh": "A coder",
    "marks": [25,30,35,40],
    1: 5,
    "anotherDict": {
        "name":"Ravi",
        "rollNo": 52
    }
}

# for returning keys in a dictionary then used dictionary.keys() method
print(myDict.keys()) # --->>> dict_keys(['fast', 'vrushabh', 'marks', 1, 'anotherDict'])

# for converting dict_keys into list we used typecasting list(myDict.keys())
print(list(myDict.keys())) # --->>> ['fast', 'vrushabh', 'marks', 1, 'anotherDict']

# for getting values in a dictionary then used dictionary.values()
print(myDict.values()) # --->>> dict_values(['In a Quick maneer', 'A coder', [25, 30, 35, 40], 5, {'name': 'Ravi', 'rollNo': 52}])

# for getting tuple from a dictionary then used dictionary.items() method --->>> for all items in a dictionary the returning format (key, value)
print(myDict.items()) # --->>> dict_items([('fast', 'In a Quick maneer'), ('vrushabh', 'A coder'), ('marks', [25, 30, 35, 40]), (1, 5), ('anotherDict', {'name': 'Ravi', 'rollNo': 52})])

# for updating any key in a dictionary used dictionary.update('key':'updated value')
myDict.update({
    'vrushabh':'A Programmer',
    'newKey':'newValue'
    })
print(myDict) # --->>> {'fast': 'In a Quick maneer', 'vrushabh': 'A Programmer', 'marks': [25, 30, 35, 40], 1: 5, 'anotherDict': {'name': 'Ravi', 'rollNo': 52}, 'newKey': 'newValue'}

# alternating a way for myDict["fast"]
print(myDict.get('fast')) # --->>> In a Quick maneer # --->>> prints value assciated with key "fast"

print(myDict['fast']) # ---->>>  prints value assciated with key "fast"


# The difference between .get() and [] in dictionaries ?
# print(myDict.get('fast2')) # --->>> In a Quick maneer # --->>> returns as fast2 is not present in the dictionary

# print(myDict['fast2']) # ---->>> as it throws an error bcoz fast2 is not present in dictionary




