while(True):
    print('Press q to quit')
    a = input("Enter a number ")
    if a == 'q':
        break
    try:
        print('Trying.......')
        a = int(a)
        if a>6:
            print('you entered a value which is greater than 6')
    except Exception as e:
        print(f"Your input resulted in the error {e}") 
print("Thanks for playing this game")