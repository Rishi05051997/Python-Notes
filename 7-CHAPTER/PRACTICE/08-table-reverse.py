num = int(input("Enter a no to print table in reverse order: "))
table = []
for i in range(1, 11):
    table.append(i*num)
table.reverse()
print(table)
# print(table.reverse())