m1 = int(input('enter marks for subject - 1 \n'))
m2 = int(input('enter marks for subject - 2 \n'))
m3 = int(input('enter marks for subject - 3 \n'))

avg = (m1 + m2 + m3)/3
averagePercentForAllSub = avg * 100

if((m1 >=33 and m2 >= 33 and m3 >= 33) and averagePercentForAllSub > 40):
    print('Pass')
else:
    print('Fail')