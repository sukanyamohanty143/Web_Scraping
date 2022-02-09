import requests
from bs4 import BeautifulSoup
import json
import pprint
def scrape_movie_details(url1):
    a = (url1)
    movie_page = requests.get(a)
    soup=BeautifulSoup(movie_page.text,'html.parser')
    dict={}
    one_div = soup.find('div',class_='container')
    body = one_div.find("div",class_="media-body")
    li= body.find_all("li") 
    movie_name=one_div.find("h1", slot="title").get_text()
    dict["movie_name"]=movie_name
    for i in li:
        data=i.text
        var=data.split()
        if 'Rating:' in var:
            dict['rating']=var[1]
        elif "Genre:" in var:
            dict['Genre']=var[1:]
        elif 'Language:' in var:
            dict['Languagre']=var[2:]
        elif 'Director:' in var:
            a=var[1:]
            d=" "
            for k in a:
                d+=k
            d=d.split(",")

            dict['Director']=d
        elif 'Runtime:' in var:
            run=var[1:]
            for j in range (len(run)):
                if "h" in run[j]:
                    hour=int(run[j][ :-1])*60
                elif "m" in run[j]:
                    min=int(run[j][ :-1])
            time = hour+min 
            dict['Runtime'] = time
        # elif 'Distributor:' in var: 
            # dict['Distributor']=var[2:]
    # with open("task4.json","w+") as file: 
    #     json.dump(dict,file,indent=4) 
            return (dict)
    # return(dict) 
# url1="https://www.rottentomatoes.com/m/spider_man_into_the_spider_verse" 
# (scrape_movie_details(url1))