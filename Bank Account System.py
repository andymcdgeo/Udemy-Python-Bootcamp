#Create a bank account that has two attributes: Owner and Balance
# two methods required are deposit and withdraw

class current_account():

    def __init__(self, owner, balance, accountid):
        self.owner = owner
        self.balance = balance
        self.acctid = accountid

    def __str__(self):
        return f' Account ID:       {self.acctid}\n Account Owner:    {self.owner}\n Current Balance:  £{self.balance}'

    def owner(self):
        return self.owner

    def account_id(self):
        return self.acctid

    def balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f'Deposited Accepted \n New balance £{self.balance}')
        return self.balance



    def withdraw(self, amount):
        if self.balance - amount <0:
            print(f'You are overdrawn and cannot remove any more funds.\nYou currently have {self.balance}')
            return self.balance

        else:
            self.balance = self.balance - amount
            print(f'Withdrawl Accepted \n New balance £{self.balance}')
            return self.balance


def add_account():
    account_id_list = []
    owner_list = []
    amount_list = []

    AddAccounts = True

    while AddAccounts is True:
        x = input('Do you want to create an a new account?:  ')
        #check to see if values already exist in account ID. If so, append 1
        if not account_id_list:
            count = 1
        else:
            count = account_id_list[-1] + 1

        if x.lower() == 'y':

            account_id_list.append(count)
            owner_list.append(input('Enter your Name: '))
            amount_list.append(input('Enter your initial balance: '))
            AddAccounts = True
        else:
            AddAccounts = False

    for account_id_list, owner_list, amount_list in zip(account_id_list,owner_list, amount_list):
        return account_id_list, owner_list, amount_list
        print(f'Account ID: 000{account_id_list}\nAccount Owner: {owner_list}\nTotal Balance:  £{amount_list}\n')


    print('Your final accounts are: ')
    print(owner_list)
    print(amount_list)


acct1 = current_account('Andy', 100, '001')


option = True
while option is True:

##### section needs sorting
     account_id_list, owner_list, amount_list = add_account()

    id_check = int(input('Please enter your account ID Number: '))

    while id_check not in account_id_list:
        acct_exist = print('Your account does not exist. Would you like to create one? [y/n]: ')
        if acct_exist.lower() == 'y':
            add_account()

######

    print('\n')
    print('Please make a selection from:\n 1 - View Account Details \n 2 - Withdraw Funds\n 3 - Make Deposit \n 0 - Quit')
    selection = input('Enter Selection Number:  ')


    if selection == '1':
        print(f'\n{acct1}')
    elif selection == '2':
        amount = int(input('Please enter withdrawl amount:  £  '))
        acct1.withdraw(amount)
    elif selection == '3':
        amount = int(input('Please enter deposit amount:  £  '))
        acct1.deposit(amount)
    elif selection == '4':
        add_account()
    elif selection == '0':
        option = False

print('Thank you for using our system. Have a good day.')



class savings_account():
    pass
