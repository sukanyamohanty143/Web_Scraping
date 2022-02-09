import json
import pprint
from task1 import scrape_top_list
from task4 import scrape_movie_details
from requests.exceptions import ConnectionError
t1=scrape_top_list()
with open("task1.json","r") as f:
    data = json.load(f)
top_movies = data[:10]
def get_movie_list_details():
    movies_urls=[]
    for i in top_movies:
        url_data = scrape_movie_details(i["url"])
        movies_urls.append(url_data)   
 
    with open("task5.json","w") as f:
        json.dump(movies_urls,f,indent=4) 
    return movies_urls
pprint.pprint(get_movie_list_details()) 

