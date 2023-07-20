








print('~~~ Welcome to your terminal checkbook! ~~~')

#Main Menu

#amount will be the input variable
amount = 0
#balance will be the placeholder variable
balance = 0
# need a continuous loop until exit
while True:

    # asks the question as per the assignment
    print('What would you like to do?')

    # gives a menu
    print('1) current balance')
    print('2) withdraw funds')
    print('3) deposit funds')
    print('4 exit')

    # user input
    choice = input('Your choice?')

    # will give your balance (gotta figure out how to get it to save)
    if (choice == '1'):
        print(f'Your current balance is $ {float(balance)}')

    # will subtract the amount input in from the balance
    elif (choice == '2'):
        amount = float(input('How much?'))
        balance -= amount

    # will add the amount input to the balance
    elif (choice == '3'):
        amount = float(input('What amount?'))
        balance += amount

    # will give the invalid statement as per project
    elif (choice > '4'):
        print('Invalid choice')
        
    # will exit the app
    else: 
        choice == '4'
        print('Thanks, have a great day!')
        break









