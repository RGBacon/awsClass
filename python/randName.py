import random

classNames = []
collectingNames = True


def collectNames():
  while True:
    name = input("When done entering names enter 'done'\nEnter name: ").lower()
    if name == "done":
      break
    classNames.append(name)


def menu():
  print("Random name selector")
  print("1: Enter names")
  print("2: Choose a random name")
  print("3: Remove a name")
  print("4: List names in list")

  choice = input("Choose an option: ")
  return choice


def randName():
  return random.choice(classNames)


def removeName(a):
  try:
    classNames.remove(a)
  except:
    print("ERROR: Name not in list")


while True:
  a = menu()
  if a == "1":
    collectNames()
  elif a == "2":
    try:
      a = randName()
      print(a)
    except:
      print("Enter some names first")
  elif a == "3":
    removeName(input("What name to remove?").lower())
