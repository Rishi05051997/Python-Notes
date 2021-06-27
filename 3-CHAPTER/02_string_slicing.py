name = "Vrushabh"

greeting = " Good Morning"

# concatinating two strings 
c = name + greeting
print(c)

print(name[0], name[1])

# name[2] = "k" --->>> doest not work
print(type(name))


# string slicing
print(name[:3]) ### is same as name[0:3]

print(name[1:]) # same as print(name[1:8])

print(name[-5:-2]) # same as print(name[2:5])


print(len(name))

# Skip value

word = name[1:8:2]
print(word)

sent = 'RishiIsGood'

d = sent[0::3]
print(d)

