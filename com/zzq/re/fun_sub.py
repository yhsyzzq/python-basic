import re

phone = "2004-959-559 # 这是一个电话号码"

# 删除注释
num = re.sub("#.*$", "", phone)
print(num)

# 删除任意的非数字内容
num = re.sub("\D","",phone)
print(num)