account_id_list = [1,2,3]
owner_list = ['John','Bob','Simon']
amount_list = [200,3000,500]

def add_account(account_id_list, owner_list, amount_list):
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
            amount_list.append(int(input('Enter your initial balance: ')))
            AddAccounts = True
        else:
            AddAccounts = False

    for account_id_list, owner_list, amount_list in zip(account_id_list, owner_list, amount_list):
        print(f'Account ID: {account_id_list}\nAccount Owner: {owner_list}\nTotal Balance:  £{amount_list}\n')

    return account_id_list, owner_list, amount_list


def account_details():
    #checks to see if an ID is in the ID list
    correct_id = True

    while correct_id is True:
        id_num = int(input('Please enter your ID number:   '))
        if id_num in account_id_list:
            print(f'Account ID: {account_id_list[id_num-1]}\nAccount Owner: {owner_list[id_num-1]}\nTotal Balance:  £{amount_list[id_num-1]}\n')
            correct_id = False
            return id_num
        elif id_num == 0:
            correct_id = False
        else:
            print('Your ID is not recognised and you will not be able to proceed until the correct ID is entered')

option = True

id_num = account_details()

while option is True:

    print('\n')
    print(
        'Please make a selection from:\n 1 - View Account Details \n 2 - Withdraw Funds\n 3 - Make Deposit \n 9 - Add Account \n 0 - Quit')
    selection = input('Enter Selection Number:  ')

    if selection == '1':
        print(f'Account ID: {account_id_list[id_num-1]}\nAccount Owner: {owner_list[id_num-1]}\nTotal Balance:  £{amount_list[id_num-1]}\n')

    elif selection == '2':
        print(f'You currently have: {amount_list[id_num-1]}')
        amount = int(input('Please enter withdrawl amount:  £  '))
        print('\n')
        amount_list[id_num - 1] = amount_list[id_num - 1] - amount
        print(f'Your current balance is now: £{amount_list[id_num-1]}')

    elif selection == '3':
        print(f'You currently have: {amount_list[id_num-1]}')
        amount = int(input('Please enter deposit amount:  £  '))
        print('\n')
        amount_list[id_num - 1] = amount_list[id_num - 1] + amount
        print(f'Your current balance is now: £{amount_list[id_num-1]}')

    elif selection == '9':
        password = '123'
        x = input('Please enter the password:  ')

        if x == password:
            add_account(account_id_list,owner_list,amount_list)
        else:
            print('Incorrect Details')

        id_num = account_details()

    elif selection == '0':
        option = False

print('Thank you for using our system. Have a good day.')



