while True:
  
  num1 = input("Enter your first number: ")
  num2 = input("Enter your second number: ")

  if num1.isnumeric() and num2.isnumeric() == True:
    if num1 == num2:
      print("Both numbers are equal")
    elif num1 > num2:
      print("The first number is greater.")
    else:
      print("The second number is greater")
  else:
    print("Please enter numbers only")