#first class 

firstName = "Jeremy"
lastName = "McConkey"
age = 23

print("Next year's age equals: ", age + 1, type(age))
print("First name equals: ", firstName, type(firstName))
print("Last name equals: ", lastName, type(lastName))

class Person:
  firstName = "Jeremy"
  lastName = "McConkey"
  age = 23

jeremy0 = Person()
print(jeremy0.firstName,jeremy0.lastName,jeremy0.age)

class Instructor
  def __init__(self, firstName, lastName, age):
    self.firstName = firstName
    self.lastName = lastName
    self.age = age

instruct = Instructor("Brandon", "Steel", 28)