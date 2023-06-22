


robert = AdvancedPerson("Robert", "Doe",
"68", "423", "Chattanooga", "1954", "37403",
"hotmail")

Christopher = AdvancedPerson("Christopher", "Barnes",
"67", "510", "Commerce", "1956", "90040",
"hotmail")
femi = AdvancedPerson("Femi",
"Oluwaleye", "31", "651", "StPaul", "1991",
"11212", "gmail")

def emailGenerator(val1, val2, val3, favEmail):

  email = val1 + val2 + val3 + "@" + favEmail + ".com"

  return email

print(emailGenerator(robbert.firstName, robbert.city, robert.birthYear, robert.favEmail))