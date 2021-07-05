# num = [2,3,4,5,6,7,8,9,10,11, 12, 13,14,15,16,17,18,19,20]

# for i in (num):
#     for j in range(1, 11):
#         print(num[i]* j) 
#         a = num[i]* j
#         with open('9-CHAPTER\PRACTICE\\table.txt', 'w') as f:
#             f.write(str(a))
#         print(f)  


for i in range(2, 21):
    with open(f'9-CHAPTER/PRACTICE/tables/multiplication_table_of_{i}.txt', "w") as f:
        for j in range(1, 11):
            f.write(f"{i}X{j}={i*j}")
            if j!=10:
                f.write('\n')
    
