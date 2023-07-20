import os




def get_balance():
    balance = 0

    if os.path.exists('cb_txt.txt'):
        with open('cb_txt.txt', 'r') as f:
            for line in f:
                trans = line.strip().split(',')
                if trans[0] == 'withdraw':
                    balance -= float(trans[1])
                elif trans[0] == 'deposit':
                    balance += float(trans[1])
        return balance
            

    # else:
    #     print(f'Your current balance is $ 0')
    


# if no txt file is made return 0 balance
def check_balance():
    balance = get_balance()
    print(f'Your balance is {balance}')
    


# if no txt file is there, make one, and withdraw amount from balance
def withdrawal():
    amount = float(input('How much would you like to withdraw'))
    if os.path.exists('/Users/click/codeup-data-science/py-checkbook-project/cb_txt.txt'):
        
        with open('cb_txt.txt', 'a') as f:
            f.write(f' withdraw, {amount}\n')
    else:
        
        with open('cb_txt.txt', 'w') as f:
            f.write(f' withdraw, {amount}\n')
    


# if no txt file is there, make one, and deposit amount to balance
def deposit():
    amount = float((input('How much?')))

    if os.path.exists('/Users/click/codeup-data-science/py-checkbook-project/cb_txt.txt'):
        with open('cb_txt.txt', 'a') as f:
            f.write(f'deposit,{amount}\n')
    else:
        with open('cb_txt.txt', 'w') as f:
            f.write(f'deposit, {amount}\n')






# exit the app, break app
def exit_app():
    print('Thanks, have a great day!')
    










# #Main Menu
print('~~~ Welcome to your terminal checkbook! ~~~')

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

    # if file is there read
    # if not balance is 0
    if (choice == '1'):
        check_balance()
    
    



    # will subtract the amount input in from the balance
    elif (choice == '2'):
        withdrawal()


    
    # will add the amount input to the balance
    elif (choice == '3'):
        deposit()

    # will give the invalid statement as per project
    elif (choice > '4'):
        print('Invalid choice')
        
    # will exit the app
    else: 
        choice == '4'
        exit_app()
        break








