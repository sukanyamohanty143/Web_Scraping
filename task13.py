import json
from task4 import scrape_movie_details
from task12 import movie_actor_details

url="https://www.rottentomatoes.com/m/toy_story_4"
list=[]
def movie_full_details():
    dic={}
    details=scrape_movie_details(url)
    cast=movie_actor_details(url)
    details["cast"]=cast
    list.append(details)

    with open("task13.json","w+") as file:
        json.dump(list,file,indent=4)
    return list

movie_full_details()

