import math

###################################
# OS System module
###################################


###################################
# Exception Handling
###################################
# Example 4
try:
  numerator = 10
  denominator = 40

  result = numerator/denominator

  print(result)
except:
  print("Error: Denominator cannot be 0.")
finally:
  print("Regardless of anything this block of code will always run!")

# Example 3
try:
  num = int(input("Enter a number: "))
  assert num % 2 == 0
# Error being anticipated
except:
  print("This is an odd number")
# if error isnt caught, run this
else:
  reciprocal =1/num
  print(reciprocal)

# Example 2
try: #try this code
  evenNumbers = [2, 4, 6, 8]
  print(evenNumbers[5])
except ZeroDivisionError: # if we get an error matching ZeroDivisionError then do this code
  print("Zero Division Error")
except IndexError: 
  print("Index out of bounds for list")

# Example 1
def divideFiveBy(number):
  try:
    value = 5/number
  except ZeroDivisionError:
    print("Divide by zero error")
    value = 1
  return value

print(divideFiveBy(5))

###################################
# File handlers
###################################
print("Here is my diary: \n")
f1 = open("diary.txt", "r") #opens the text file "r" for read only
print(f1.read()) # print the contents of f1
#f1.close()
print("\nNow let's create a todo list: ")
f2 = open("todo.txt", "w") # write
f2.write("Take out the trash")
f2.close()
f3 = open("diary.txt", "a") # append
f3.write("Lets hope the power doesnt go out mid class")
f3.close()

###################################
# math examples using library we imported
###################################
print(math.pi) #prints pi

print(math.floor(math.pi)) # rounds to a whole int using math.floor

print(int(math.pi)) # same as above rounds down, turning an float into a int

print(math.pow(5, 2))

print(5**2)