this = "    Vrushabh is a god     "
print(this)
print(this.strip())


def removeSpaces(string, word):
    newStr = string.replace(word, '')
    return newStr.strip()
line1 = "   hello hoe     are     you   "
a = removeSpaces(line1, 'are')
print(a)