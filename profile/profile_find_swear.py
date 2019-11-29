import requests
import json, os

url = "https://graphql.anilist.co/"


# To get access token please visit: https://anilist.co/api/v2/oauth/authorize?client_id=2861&response_type=token
accessToken = json.loads(open(os.path.join('', 'api.json')).read())

no = input('Enter page number ->')
print()

payload = "{\"query\":\"query($p: Int) {\\n  Page(page:$p) {\\n    pageInfo {\\n      total\\n      perPage\\n      currentPage\\n      lastPage\\n      hasNextPage\\n    }\\n    users(sort:ID_DESC) {\\n      id\\n        name\\n        about\\n        siteUrl\\n    }\\n  }\\n}\",\"variables\":{\"p\":" + str(no) + "}}"
headers = {
    'content-type': "application/json",
    'authorization': "Bearer " + accessToken
    }

response = requests.request("POST", url, data=payload, headers=headers)

#query data
qdata = response.text

#casefold all
cdata = qdata.casefold()
#cdata but array (split and removed '},{' )
rdata = cdata.split('},{')


keyword_list = json.loads(open(os.path.join('profile', 'words.json')).read())


listOfStrings = rdata

all_text = keyword_list


for item in listOfStrings:
  for keyworditem in keyword_list:
      if keyworditem in item:
            split = item.split(',')
            idstring = split[1]
            #idstring = idstring.replace('"id":','')
            print(idstring)
            #for useritem in split:
              #print(useritem) 