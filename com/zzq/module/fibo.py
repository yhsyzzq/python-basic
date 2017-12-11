# 斐波拉契数列
def fibo(n):
    fiboList = [0, 1]
    print(fiboList[0])
    print(fiboList[1])
    for i in range(2, n):
        c = fiboList[i - 1] + fiboList[i - 2]
        fiboList.append(c)
        print(c)


fibo(10)
