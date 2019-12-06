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
    stoppage = int(input('Enter page number to stop at -->'))
    print('         ------STARTING------')
    while startpage < stoppage:

        no = startpage

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

        #loop 50 times with +1 each cycle, because max entries per page is 50.
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
                page = urllib.request.urlopen("http://localhost:5555/api/classify?url=" + result).read().decode('utf-8')
                jsonify = json.loads(page)
                get_predictions = jsonify.get('predictions',{})
                pred1 = get_predictions[0]
                pred2 = get_predictions[1]
                nsfw = ["hentai", "sexy", "porn"]
                possible_class1 = pred1.get('class',{})
                possible_class2 = pred2.get('class',{})
                predict1 = pred1.get('prob',{}) * 100
                predict2 = pred2.get('prob',{}) * 100

                if possible_class1 in nsfw:
                    print('https://anilist.co/user/' + idnum)
                    print("1st guess: " + possible_class1.upper() + ": " + str(predict1) + "%")
                else:
                    pass

                if possible_class2 in 'hentai':
                    if int(predict2) > 10:
                        print('https://anilist.co/user/' + idnum)
                        print("2nd guess: " + possible_class2.upper() + ": " + str(predict2) + "%")
                    else:
                        pass
                else:
                    pass
                nq = nq+1
        time.sleep(1)
        startpage = startpage+1
        if startpage == stoppage:
            print('         ------FINISHED------')
        else:
            print('         Page: ' + str(startpage))
