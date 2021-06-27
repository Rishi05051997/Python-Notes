# a = input('Enter your name ')

# b = input("Enter date ")

# letter = f''' Dear {a}

#             you are selected
#             Date:{b}'''

# print(letter)



### Another Approach
letter = ''' Dear <|NAME|>
            Greeting from ABC conding house. I am happy to tell you about your selcection
            You are selected!
            Have a great day ahead!
Thanks & Regards
ABC Company
DATE: <|DATE|>
'''

name = input('Enter Your Name \n')
date = input('Enter date\n')

letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)

print(letter)