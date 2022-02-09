from task5 import*
import json
with open("task5.json","r") as file:
    movie_language=json.load(file)
def analyse_movies_directors():
    dic={}
    for i in movie_language:
        if "Director" in i:
            for j in i["Director"]:
                if j in dic:
                    dic[j]=dic[j]+1
                if j not in dic:
                    dic[j]=1
    with open("task7.json","w+") as file:
        json.dump(dic,file,indent=4)
analyse_movies_directors()