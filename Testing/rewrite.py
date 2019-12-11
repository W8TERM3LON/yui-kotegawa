#import lib
import requests, json, os, re, time, urllib.request

#define REST API server
url = "https://graphql.anilist.co/"

#Get Access Token.
accessToken = json.loads(open(os.path.join('', 'api.json')).read())

#User input
startpage = int(1)
stoppage = int(2)

#Print Starting prompt.
print('         ------STARTING------')

#While startpage is smaller than stoppage loop.
while startpage < stoppage:
    payload = "{\"query\":\"query ($p: Int) {\\n  Page(page: $p) {\\n    users(sort: ID_DESC) {\\n      id\\n      avatar{\\n        large\\n      }\\n      \\n    }\\n  }\\n}\",\"variables\":{\"p\":" + str(startpage) + "}}"
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer " + accessToken
    }

    #POST request parameters.
    response = requests.request("POST", url, data=payload, headers=headers)
    response = response.json()
    response = response.get('data', {})
    response = response.get('Page', {})
    response = response.get('users', {})
#    print(response)
    for person in response:
        avatar = person.get('avatar').get('large')
        if avatar == "https://s4.anilist.co/file/anilistcdn/user/avatar/large/default.png":
            pass
        else:
            id = person.get('id', {})
            print(avatar, id)
    
   
   
   
   
    #response = json.loads(response)
    #response = json.dumps(response, indent=4, sort_keys=True)
    