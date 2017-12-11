import requests, re
import simplejson as json, pprint

data = {
    'callback': 'angular.callbacks._6',
    'loginName': 'MDI3KYW0',
    'password': 'YWJjOTU2OEAxMjM=',
    't': '1512726685437'
}
s = requests.session()
s.post(url='http://www.baidu.com/login/login.action', data=data)
limit = 18
newList = []
for i in range(1, 58):
    page = i
    start = (i - 1) * 18

    url = 'http://www.baidu.com/realtime/searchCorePersonList.action?_dc=1512726685437&params.updateTime=20171207&params.deptName=&page={page}&start={start}&limit=18'.format(
        page=page, start=start)
    r = s.get(url)
    dict1 = json.loads(r.text)
    personList = dict1['personList']
    for dict in personList:
        personName = dict['nativeplace'] + "-" + dict['age'] + "-" + dict['psnname']
        # print(personName)
        newList.append(personName)
        print(personName)

# newList.sort()
# for info in newList:
#     print(info)

# for name in newList:
#     count = newList.count(name)
#     if count > 1:
#         print('name='+name + ', count='+str(count))




# urlAddress = 'http://192.168.218.44:8480/login/login.action'
# for line in request.urlopen(urlAddress):
#     resultLine = line.decode('utf-8')
#     dict1 = json.loads(resultLine)
#     dict2 = dict1['regeocode']
#     pprint.pprint(dict2['formatted_address'])
