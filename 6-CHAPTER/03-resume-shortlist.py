branch = input('enter your branch \n')

exp = int(input('enter the experience in years \n'))

if((branch == 'CS' or branch == 'IT') and exp >= 2):
    print('Your are eligible')
else :
    print('Not eligible')