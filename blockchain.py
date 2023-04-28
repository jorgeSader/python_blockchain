blockchain = [[1]]

def get_last_blockchain_value():
  ''' gets and returns the last value of the blockchain.'''
  if len(blockchain) < 1:
    return None 
  return blockchain[-1]


def add_transaction(transaction_amount, last_transaction=[1]):
  '''it appends a given transaction amount and last transacion to the current blockchain.
  
  Arguments:
    transaction_amount: the values of the current transaction.
    last_transaction: the transaction that was made prior to the transaction being made.
  
  '''
  if last_transaction == None:
    last_transaction = [1]
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
    
    

while True:
  print('Please Choose: ')
  print('1: Add a new transaction value.')
  print('2: Output the blockchain blocks.')
  print("x: Exit.")
  user_choice = get_user_choice()
  if user_choice == '1':
    add_transaction(get_transaction_value(), get_last_blockchain_value())
  elif user_choice=='2':
    print_blockchain_elements()
  elif user_choice == 'x':
    break
  else:
    print('Sorry please enter a valid option.')
    
print('Done!!!')