import requests
import json
from collections import namedtuple

import sys

def printChild(children):
    for child in children:
        post = namedtuple('Post',child["data"].keys())(*child["data"].values())
        print(post.title)
        print("\t",post.selftext)
        # print("\033[1;32;40m Bright Green  \n")

def loadPage(url,arg,num):
    localUrl = url
    if(arg != None):
        localUrl = url+"?after="+arg
    response = requests.get(localUrl, headers = {'User-agent': 'your bot 0.1'})
    if response.status_code >=300:
        print("ERROR")
        print("The server returned a",response.status_code)
        return
    page = json.loads(response.content)
    page = namedtuple('Page',page.keys())(*page.values())
    data = namedtuple('Data',page.data.keys())(*page.data.values())
    printChild(data.children)
    try:
        loadPage(url,data.after, num+1)
    except:
        pass

webPage = "https://www.reddit.com/r/brandonsanderson.json"
loadPage(webPage, None,0)
# print(response.)