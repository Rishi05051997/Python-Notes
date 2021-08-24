a = [3, 5, 7, 8, 9, 10, 12, 45, 67, 66]

# b = []

# for item in a:
#     if(item%2 ==0):
#         b.append(item)

# print(b)
#Shortcut to write the same
b = [i for i in a if i%2 ==0]
print(b)

t = [1, 4, 2, 4, 1, 2, 3]
s = {i for i in t}
print(s)