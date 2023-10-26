commaSepNumbers = input("Write comma separated numbers: ")

numbersList = list()
numbersTupple = tuple()

for i in 0..len(commaSepNumbers):
  if type(i)==int | type(i)==float:
    numbersList.append(i)
    numbersTupple.append(i)

print(numbersList)
print(numbersTupple)