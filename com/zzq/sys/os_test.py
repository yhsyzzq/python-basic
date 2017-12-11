import os, time, glob, math, random
from datetime import date, datetime

'''系统处理'''
print(os.getcwd())

'''通配符查询'''
for file in glob.glob('*.py'):
    print(file)

'''时间处理'''
now = date.today()

nowtime = datetime.now()
print(nowtime)

curTime = time.time()
print(curTime)

formatCurTime = time.strftime('%Y-%m-%d %H:%M:%S')
print(formatCurTime)

'''数学函数'''
print(math.pi)
print(int(math.pow(2, 3)))

'''随机数'''
print(random.randint(100001, 999999))
print(random.sample(range(100), 10))
print(str(random.random() * 1000000).split(".")[0].zfill(6))

'''截取字符串'''
str = 'goodgoogle'
print(str[0:3])
print(str[::-1])
