myDict = {
    "pankha" : "Fan",
    "dabba" : "box",
    "vastu": "item"
}

print("Options are :", myDict.keys())


a = input("enter the hindi word \n")

# print('The meaning of your word is: ', myDict[a])

# below line will not throw an error if key is not present in dictionary
print('The meaning of your word is: ', myDict.get(a))