numberList = []
for i in range(1, 1000 + 1):
    numberList.append(i)

it = iter(numberList)

for element in it:
    print(str(element))

mytuple = (3, 5, 7, 9, 1, 6, 4)
iterator = iter(mytuple)
iterator2 = mytuple.__iter__()
for i in iterator2:
    print(i)
