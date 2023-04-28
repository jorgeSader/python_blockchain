blockchain = [[1]]

def get_last_blockchain_value():
  ''' gets and returns the last value of the blockchain.'''
  return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
  '''it appends a given transaction amount and last transacion to the current blockchain.
  
  Arguments:
    transaction_amount: the values of the current transaction.
    last_transaction: the transaction that was made prior to the transaction being made.
  
  '''
  blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
  ''' asks the user to input the transaction amount and returns the value provided by the user '''
  return float(input('Please enter your transaction value: '))


def get_user_choice():
  return input('Your choice: ')


def print_blockchain_elements():
  for block in blockchain:
    print('Outputting Block: ')
    print(block)
    
    
add_value(get_transaction_value())

while True:
  print('Please Choose: ')
  print('1: Add a new transaction value')
  print('2: Output the blockchain blocks')
  print("Press 'Ctrl + D' to exit.")
  
  user_choice = get_user_choice()
  
  if user_choice == '1':
    add_value(get_transaction_value(), get_last_blockchain_value())
  else:
    print_blockchain_elements()
  
  
  
  
  
print('Done!!!')