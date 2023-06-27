# Challenge 1 Capital indexes
def capital_indexes(string):
  seperate = list(string)
  capital = []
  for i in range(len(seperate)):
    if seperate[i].isupper():
      capital.append(i)
  return capital
print(capital_indexes("HeLlO"))

# Challenge 2 Middle letter
def mid(string):
  length = len(string)
  if length % 2 == 0:
    return ""
  else:
    middle = length // 2
    return string[middle]
print(mid("abcde"))