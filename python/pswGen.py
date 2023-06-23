# Create variables for letters, digits and special chars
# while loop when password

import secrets
import string

def createPassword():
  letters = string.ascii_letters
  digits = string.digits
  specialChars = string.punctuation
  alphabet = letters + digits + specialChars
  password = ""
  
  while len(password) < passLength:
    
    for i in range(passLength):
      password += ''.join(secrets.choice(alphabet))
  return password

while True:
  
  passLength = int(input("Length of password to generate: "))
  
  if passLength > 7:
    print(createPassword())
    cont = input("Press Enter to continue or type STOP to exit: ").lower()
    if cont == "stop":
      print("see you next time")
      break
  else:
    print("Passwords under 8 is unsecure\nPlease try again")