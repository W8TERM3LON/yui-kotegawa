import requests
import json, os, re, time
import urllib.request


url = "https://graphql.anilist.co/"


# To get access token please visit: https://anilist.co/api/v2/oauth/authorize?client_id=2861&response_type=token
accessToken = json.loads(open(os.path.join('', 'api.json')).read())
if accessToken in "REPLACE WITH ACCESS TOKEN":
    print("Please add your access token.")
else:
    #user specified page number
    startpage = int(input('Enter start page number -->'))
    stoppage = int(input('Enter page number to stop after -->'))
    stoppage = stoppage + 1
    print('         ------STARTING------')
    while startpage < stoppage:

        no = startpage

        #POST request data
        payload = "{\"query\":\"query ($p: Int) {\\n  Page(page: $p) {\\n    users(sort: ID_DESC) {\\n      id\\n      about\\n    }\\n  }\\n}\",\"variables\":{\"p\":" + str(no) + "}}"
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
        for info in response:
            about = info.get('about')
            about = str(about)
            ident = info.get('id')
            ident = str(ident)
            if about == "None":
                pass
            else:
                print('https://anilist.co/user/' + ident)
                print(about)
                print()
                print()
                time.sleep(2)

        startpage = startpage+1
        if startpage == stoppage:
            print('         ------FINISHED------')
        else:
            print()
            print('         Page: ' + str(startpage))
            print()
            time.sleep(3)
