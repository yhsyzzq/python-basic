from urllib import request
import simplejson as json, pprint

urlAddress = 'http://restapi.amap.com/v3/geocode/regeo?key=04e70f978f9d7314e3ef367f5071cf6c&s=rsv3&location=116.384533,39.884568&radius=1000&extensions=all'
for line in request.urlopen(urlAddress):
    resultLine = line.decode('utf-8')
    dict1 = json.loads(resultLine)
    dict2 = dict1['regeocode']
    pprint.pprint(dict2['formatted_address'])
