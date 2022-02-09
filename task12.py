import requests
from bs4 import BeautifulSoup
import json
url="https://www.rottentomatoes.com/m/toy_story_4"
def movie_actor_details(url):
    sample=requests.get(url)
    soup=BeautifulSoup(sample.text,"html.parser")

    div=soup.find("div",class_ = "castSection")
    d1=div.find_all("div",class_="cast-item media inlineBlock")
    d2=div.find_all("div",class_="cast-item media inlineBlock moreCasts hide")

    list=[]
    for i in d1:
        dic={}
        a=i.find("a")["href"][11:]
        dic["actor_name"]=a
        list.append(dic)

    for j in d2:
        dic1={}
        a1=j.find("a")["href"][11:]
        dic1["actor_name"]=a1
        list.append(dic1)
    
    with open("task12.json","w+") as file:
        json.dump(list, file,indent=4)
        return list

movie_actor_details(url)

