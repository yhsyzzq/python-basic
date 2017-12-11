import pickle
import pprint

#写入对象
data1 = {'a': 'ss', 'b': [1, 3, 6, 7], 'c': ('a', 'c', 3)}

output = open('d:\data.pkl', 'wb')
pickle.dump(data1, output)
output.close()

#读取对象
ppkOutput = open('d:\data.pkl', 'rb')
data1 = pickle.load(ppkOutput)
pprint.pprint(data1)
ppkOutput.close()