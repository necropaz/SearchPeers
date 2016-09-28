import urllib2
import json

command = {'command': 'getNeighbors'}

stringified = json.dumps(command)

headers = {'content-type': 'application/json'}

request = urllib2.Request(url="http://localhost:14265", data=stringified, headers=headers)
returnData = urllib2.urlopen(request).read()

neighbors = json.loads(returnData)
length=len(neighbors['neighbors'])
for i in range (0,length):
	print("IP:"+str(neighbors['neighbors'][i]['address'])+"numberOfAllTransactions: "+str(neighbors['neighbors'][i]['numberOfAllTransactions'])+"numberOfNewTransactions: "+str(neighbors['neighbors'][i]['numberOfNewTransactions']))

