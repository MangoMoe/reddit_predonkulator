import requests
import json


response = requests.get("https://www.reddit.com/r/brandonsanderson.json", headers = {'User-agent': 'your bot 0.1'})
# response = requests.get("https://www.reddit.com/r/brandonsanderson.json")




# def printChildren(list):
#     for(child in ) 

def loadPage(url,arg):
    if(arg != None):
        url = url+"?after="+arg
    response = requests.get(url, headers = {'User-agent': 'your bot 0.1'})
    if response.status_code >=300:
        print("ERROR")
        print("The server returned a",response.status_code)
        return;
    else:
        page = json.loads(response.content)
        print(page["data"]["children"])
        # printChildren(page["data"]["children"])
        loadPage(url,page["data"]["after"])



webPage = "https://www.reddit.com/r/brandonsanderson.json"
loadPage(webPage, None)
# print(response.)