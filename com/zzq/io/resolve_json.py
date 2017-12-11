import simplejson as json, pprint

f = open("D:/PyCharm Community Edition 2017.2/workspaces/python-basic/com/zzq/io/data.json", 'r', encoding='UTF-8')
line = f.readlines()
dict1 = json.loads(line[0])
personList = dict1['personList']
for dict in personList:
    print(dict['psnname'])
