count = 0

while count < 10:
    print(count)
    count += 1

for eachLetter in "Names":
    print("current letter:" + eachLetter)

nameList = []
for i in range(0, 1000):
    nameList.append(str(i))

for eachName in nameList:
    print(eachName)

for i, eachName in enumerate(nameList):
    print("%d : %s" % (i + 1, eachName))

