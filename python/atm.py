import csv

accountBalance = 500
loginCheck = False
accountName = "null"
accounts_file = 'accounts.csv'

def login():
  accountYN = input("Do you have an account with Bank of America? y/n: ")

  if accountYN in ["y", "Y", "Yes", "yes"]:
    accountName = input("Please Enter your Account Name (case sensitive)")
    accountPin = input("Please Enter your PIN: ")
    authAccount(accountName, accountPin)
  elif accountYN in ["n", "N", "No", "no"]:
    print("Welcome to Bank of America")
    accountName = input("Please enter your name:")
    accountPin = input("Please enter a pin code: ")
    saveAccount(accountName, accountPin)

def menu():
	print("ATM for Bank of America")
  print("Account: " + accountName)
  print("1. Check Balance")
  print("2. Deposit")
  print("3. Withdraw")
  print("4. Logout")

def checkBalance():
  print("Your balance is: $" + accountBalance)
  
def withdraw():
  withdrawAmount = input("Enter amount to withdraw: ")
  if accountBalance >= withdrawAmount:
    accountBalance -= withdrawAmount
    print("Please retreive your money below")
    print("Your updated account balance is: $" + accountBalance)
  else:
    print("You are broke! ha ha")
    print("Your current balance is: $" + accountBalance)

def deposit():
  depositAmount = input("Amount to deposit: ")
  accountBalance += depositAmount
  print("Deposit Sucessful!")
  print("Current Balance is: $" + accountBalance)

def easterEgg():
  accountBalance *= 0.25
  print("For being a loyal Bank of America Customer," + str(accountBalance*0.25) + "was added to your account.")
  print("Current Balance: $" + accountBalance)

def saveAccount(accountName, accountPin):
  with open(accounts_file, 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([accountName, accountPin, accountBalance])

def authAccount(accountName, accountPin)
  asd

while True:
  if loginCheck:
    menu()
    choice = input("Select a choice: ")

    if choice == 1:
      checkBalance()
    elif choice == 2:
      deposit()
    elif choice == 3:
      withdraw()
    elif choice == 4:
      loginCheck = False
      print("Successfully logged out. See you next time.")
    elif choice == 623:
      easterEgg()
    else:
      print("Incorrect Choice, 1-4 Please: ")
  else:
    login()
  input("Press Enter to Continue...")