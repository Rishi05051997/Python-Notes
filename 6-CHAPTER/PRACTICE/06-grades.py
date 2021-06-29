m1 = int(input('Enter the marks for subject 1 \n'))
m2 = int(input('Enter the marks for subject 2 \n'))
m3 = int(input('Enter the marks for subject 3 \n'))
m4 = int(input('Enter the marks for subject 4 \n'))
m5 = int(input('Enter the marks for subject 5 \n'))

avg = (m1 + m2 + m3 + m4 + m5)/500

percentAvg = avg * 100

print(percentAvg)

if(percentAvg <= 100 and percentAvg > 90):
    print('Excellent')
elif(percentAvg <= 90 and percentAvg > 80):
    print('A Grade')
elif(percentAvg <= 80 and percentAvg > 70):
    print('B Grade')
elif(percentAvg <= 70 and percentAvg > 60):
    print('C Grade')
elif(percentAvg <= 60 and percentAvg > 50):
    print('D Grade')
else:
    print('F Grade')