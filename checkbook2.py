import os



# function to get the overall balance if txt file exists by adding and subtracting from the deposit or withdrawal category for the overall total
# if txt file does not exist, it returns a balance of none
def get_balance():
    balance = 0

    if os.path.exists('cb_txt.txt'):
        with open('cb_txt.txt', 'r') as f:
            for line in f:
                #takes a transaction from deposit or withdrawal functions
                trans = line.strip().split(',')
                # if the transaction is 'withdraw', then the transaction is subtracted from the running balance total
                if trans[0] == 'withdraw':
                    balance -= float(trans[1])
                # if the transaction is "deposit", then the transaction is added fro the running balance total
                elif trans[0] == 'deposit':
                    balance += float(trans[1])
        return balance
            
    

# calls to the get_balance function to output the users balance
def check_balance():
    balance = get_balance()
    print(f' YOUR BALANCE IS: $ {balance}')
    


# if txt file does not exist, this will create one and save as 'withdraw, amount'
def withdrawal():
    try:
        amount = float(input('How much would you like to withdraw'))
        if os.path.exists('/Users/click/codeup-data-science/py-checkbook-project/cb_txt.txt'):
            
            with open('cb_txt.txt', 'a') as f:
                f.write(f' withdraw, {amount}\n')
        else:
            # if no txt file exists ---> gets created 
            with open('cb_txt.txt', 'w') as f:
                f.write(f' withdraw, {amount}\n')
    except ValueError:
        print('This is not a valid number')


# if txt file does not exist, this will create one and save as 'deposit, amount'
def deposit():
    # the try, except argument is so that the program doesnt break due to a string
    try:
        amount = float((input('How much?')))
    
        if os.path.exists('/Users/click/codeup-data-science/py-checkbook-project/cb_txt.txt'):
            with open('cb_txt.txt', 'a') as f:
                f.write(f'deposit,{amount}\n')
            # if no txt file exists ---> gets created        
        else:
            with open('cb_txt.txt', 'w') as f:
                f.write(f'deposit, {amount}\n')
    except ValueError:
        print('This is not a valid number')
    



# used for an invalid input from the choice option
def invalid_response():
    print('Invalid Response, choose 1 through 4')



# exit the app, break app
def exit_app():
    print('Thanks, have a great day!')
    




# #Main Menu
print('~~~ Welcome to your Terminal Checkbook! ~~~')

#amount will be the input variable
amount = 0
#balance will be the placeholder variable
balance = 0
# need a continuous loop until exit
while True:

    # asks the question as per the assignment
    print('')
    print('What would you like to do?')
    print('')
    # gives a menu
    print('1) Current Balance')
    print('2) Withdraw Funds')
    print('3) Deposit Funds')
    print('4) Exit')
    print('')

    # user input
    choice = input('Your choice?')

    # user chooses '1' and the check_balance function runs
    if (choice == '1'):
        check_balance()
    
    # user chooses '2' and the withdrawal function runs
    elif (choice == '2'):
        withdrawal()

    # user chooses '3' and the deposit function runs
    elif (choice == '3'):
        deposit()

    # will give the invalid statement as per project
    elif (choice > '4'):
        invalid_response()
        
    # will exit the app
    else: 
        choice == '4'
        exit_app()
        break








