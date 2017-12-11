import pprint


def square(x):
    return x * x


map1 = map(square, [y for y in range(10)])

for value in map1:
    print(value)

map2 = map(lambda x: x * x, [y for y in range(10)])
for value2 in map2:
    print(value2)
