# Creating an empty set
b = set()

## ADD
# adding values to an empty set
b.add(4)
b.add(5)
b.add(5) # set cannot add  values which is repeatative as it is non repeatative

# b.add([4,5,6]) # --->>> we cannot add list to a set -->>> TypeError: unhashable type: 'list'

b.add((4, 5, 6)) # --->> {4, 5, (4, 5, 6)} --->>> we can add tuples to set

# b.add({4:5}) # --->>> we cannot add dictionary to a set -->>> TypeError: unhashable type: 'dict'

print(b) # --->>> {4, 5}

## LENGTH
print(len(b)) # len() it will return then length of the set  --->>> 3

## REMOVAL
b.remove(5) # removes 5 from the set b
# b.remove(15) # throws an error as 15 is not present inside set b
print(b)

## POP
print(b.pop()) # Pop will remove one element from list and returns remaining element
print(b) # --->>> {(4, 5, 6)}

