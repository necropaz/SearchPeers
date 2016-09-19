import urllib2
import json

command = {'command': 'getPeers'}

stringified = json.dumps(command)

headers = {'content-type': 'application/json'}

request = urllib2.Request(url="http://localhost:14265", data=stringified, headers=headers)
returnData = urllib2.urlopen(request).read()

neighbors = json.loads(returnData)
print(neighbors)

