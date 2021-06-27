sentence = "I am  Rohit Sharma  .  I won 5   trophies in  IPL"

doubleSpaces = sentence.find("  ")
if doubleSpaces:
    print('Double spaces found at index ', doubleSpaces)
else :
    print('No Double spaces ')



# print(doubleSpaces)
replaceDoubleSpaces = sentence.replace("  ", " ")

print(replaceDoubleSpaces)