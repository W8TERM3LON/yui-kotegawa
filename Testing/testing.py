import requests
import json, os, re, time
import urllib.request

result ="https://pbs.twimg.com/media/EKAZS8wUEAA1UUj.jpg"
page = urllib.request.urlopen("http://localhost:5555/api/classify?url=" + result).read().decode('utf-8')
jsonify = json.loads(page)
#print()
#jsonify = json.dumps(jsonify, indent=4, sort_keys=True)
#print(jsonify)
#print()
#print()
abc = jsonify.get('predictions',{})
print(abc)
query1 = abc[0]
query2 = abc[1]
nsfw = ["hentai", "sexy", "porn"]

output1 = query1.get('class',{})
output2 = query2.get('class',{})
predict1 = query1.get('prob',{}) * 100
predict2 = query2.get('prob',{}) * 100

if output1 in nsfw:
    print(output1 + " at " + str(predict1) + "%")
else:
    pass

if output2 in nsfw:
    print(output2 + " at " + str(predict2) + "%")
else:
    pass