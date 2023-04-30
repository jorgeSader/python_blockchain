blockchain = [[1]]
open_transactions = []
owner = 'Jorge'


def get_last_blockchain_value():
    ''' gets and returns the last value of the blockchain.'''
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(sender, recepient, amount=1.0):
    '''it appends the sender, the receiver, the amount and the previous block's hash to the current blockchain.

    Arguments:
      sender: sender of the coins.
      recepient: recepient of the coins.
      amount: the amount of coins being transfered (default = 1.0). 

    '''

    transaction = {
        'sender': sender,
        'recepient': recepient,
        'amount': amount,
    }

    open_transactions.append(transaction)


def mine_block():
    pass


def get_transaction_value():
    ''' asks the user to input the transaction amount and returns the value provided by the user '''

    tx_sender = owner
    tx_receiver = input(
        'Please enter the ID of the person receiving the coins')
    tx_amount = float(input('Please enter your transaction amount: '))

    return {
        tx_sender,
        tx_receiver,
        tx_amount
    }


def get_user_choice():
    return input('Your choice: ')


def print_blockchain_elements():
    for block in blockchain:
        print('Outputting Block: ')
        print(block)
    else:
        print('-' * 35)


def verify_chain():
  # refactored to use range()
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
    return is_valid

  # This is how it was without range()
    # block_index = 0
    # is_valid = True
    # for block in blockchain:
    #     if block_index == 0:
    #         block_index += 1
    #         continue
    #     elif block[0] == blockchain[block_index - 1]:
    #         is_valid = True
    #     else:
    #         is_valid = False
    #         break
    #     block_index += 1
    # return is_valid


waiting_for_input = True
while waiting_for_input:
    print('-' * 35)
    print('Please Choose: ')
    print('1: Add a new transaction value.')
    print('2: Output the blockchain blocks.')
    print("h: Manipulate the chain (hack!).")
    print("q: Exit.")
    print('-' * 35)

    user_choice = get_user_choice()
    if user_choice == '1':
        add_transaction(get_transaction_value(), get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'q':
        waiting_for_input = False
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = 2
    else:
        print('Sorry please enter a valid option.')

    if not verify_chain():
        print_blockchain_elements()
        print('Invalid Blockchain!')
        print('You Have been logged out for tampering!!!')
        break

print('Goodbye ;)')
