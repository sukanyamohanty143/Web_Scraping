import pprint
from task1 import scrape_top_list 
import json
detail=scrape_top_list()
def group_by_year(movies):
    unic_year=[]
    for i in movies:
        year=i["year"]
        if year not in unic_year:
            unic_year.append(year)
            unic_year.sort()
    
    dic_of_movie={i:[] for i in unic_year}
    for i in movies:
        year=i["year"]
        for j in dic_of_movie:
            if str(j)==str(year):
                dic_of_movie[j].append(i)
    with open ("task2.json","w+") as file:
        json.dump(dic_of_movie,file,indent=4)
    return (dic_of_movie)
group_by_year(detail)   
