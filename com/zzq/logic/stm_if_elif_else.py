x, y = 3, 5

if x > y:
    print("x比y大")
elif x == y:
    print("x与y相等")
else:
    print("y比x大")

m, n = 1, 9
smaller = m if m > n else n
print("smaller=" + str(smaller))
