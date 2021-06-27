# Create a list using []
a = [1, 2, 3, 4, 5]

# print the list using print() function
print(a)

# Access index using a[0], a[1], a[3]
print(a[0])

# Change the value of list using a[0] = 15
a[2] = 55
print(a)

# We can create a list with items of different data types
newlist = ['Vrushabh', 2, True, None, 6.666777]

print(newlist[0])
print(newlist[1])
print(newlist[2])
print(newlist[3])
print(newlist[4])


# List Slicing
friends = ['Vrushabh', 'Akash', 'Jayesh', 'Vaibhav']

# Addition of new value to list using list.append(value)
appendedList = friends.append('Rakesh')
print(friends)

# insert new value to perticular index in a list using list.insert(index, value)
friends.insert(1, 'Nilesh')
print(friends)

# remove perticular index value in a list using list.pop(index)
friends.pop(3)
print(friends)

# reverse the list using list.reverse()
friends.reverse()
print(friends)

# for printing perticular range in list using friends[0:3]
print(friends[0:3])

