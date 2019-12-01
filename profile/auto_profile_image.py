import requests
import json, os, re, time
import urllib.request


url = "https://graphql.anilist.co/"


# To get access token please visit: https://anilist.co/api/v2/oauth/authorize?client_id=2861&response_type=token
accessToken = json.loads(open(os.path.join('', 'api.json')).read())

#user specified page number
staticnumber = int(input('Enter start page number -->'))
userinput = int(input('Enter page number to stop at -->'))
print('         ------STARTING------')
while staticnumber < userinput:

    no = staticnumber

    #POST request data
    payload = "{\"query\":\"query ($p: Int) {\\n  Page(page: $p) {\\n    users(sort: ID_DESC) {\\n      id\\n      avatar{\\n        large\\n      }\\n      \\n    }\\n  }\\n}\",\"variables\":{\"p\":" + str(no) + "}}"
    headers = {
        'content-type': "application/json",
        'authorization': "Bearer " + accessToken
     }

    #POST request parameters.
    response = requests.request("POST", url, data=payload, headers=headers)

    #Output - query data
    qdata = response.text
    #remove backslashes.
    qdata = qdata.replace('\\','')
    #remove square brackets.
    qdata = qdata.replace('[', '')
    qdata = qdata.replace(']', '')
    #Remove default image profiles.
    qdata = qdata.replace('"https://s4.anilist.co/file/anilistcdn/user/avatar/large/default.png"', 'null')
    #remove "large":"
    qdata = qdata.replace('"large":"','')
    #remove quotation marks
    qdata = qdata.replace('"','')

    #DO NOT CASEFOLD. IMAGE URL IS CASE SENSITIVE
    #Turn qdata into an array at each },{
    rdata = qdata.split('},{')

    #print(rdata)

    #loop 50 times with +1 each time
    nq = 1
    while nq < 49:
        #set image as rdata
        image = rdata[nq]
        idnum = rdata[nq].split(',')
        match = re.search("{(.+?)}", image,flags=re.IGNORECASE)
        result = match.group(1)

        if result == 'large:null':
            nq = nq+1
        else:
            idnum = idnum[0].replace('id:','')
            print('https://anilist.co/user/' + idnum)
            page = urllib.request.urlopen("http://127.0.0.1:7981/" + result).read().decode('utf-8')
            page = page.replace("b''","")
            #page = page.replace('.','')
            floatscore = float(page)
            floattwo = round(floatscore, 2) * 100
            floattwo = int(floattwo)
            if floattwo >= 70:
                print("^^IS MOST LIKELY NSFW AT " + str(floattwo) + "%!!^^")
            else:
                print("^^Is " + str(floattwo) + "% NSFW.^^")
            nq = nq+1
    time.sleep(1)
    staticnumber = staticnumber+1
    if staticnumber == userinput:
        print('         ------FINISHED------')
    else:
        print('         Page: ' + str(staticnumber))
