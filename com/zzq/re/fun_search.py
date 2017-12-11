import re

print(re.search("www","www.baidu.com").span())
print(re.search("com","www.baidu.com").span())

line = "Cats are smarter than dogs";

searchObj = re.search( '(.*) are (.*?) .*', line, re.M|re.I)

if searchObj:
   print ("searchObj.group() : ", searchObj.group())
   print ("searchObj.group(1) : ", searchObj.group(1))
   print ("searchObj.group(2) : ", searchObj.group(2))
else:
   print ("No match!!")