file = open("D:\ip2.txt", 'w')
file.write("Process finished with exit code 0\r\nhahaha\r\n")
file.close()

f = open("D:\ip2.txt", 'r')
str = f.readlines()
print(str)


f2 = open("D:\ip2.txt", 'r')
for line in f2:
    print(line,end='')