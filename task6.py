from task5 import*
import json
with open("task5.json","r") as file:
    movie_language=json.load(file)
def analyse_movies_directors():
    dic={}
    for i in movie_language:
        if "Languagre" in i:
            for j in i["Languagre"]:
                if j in dic:
                    dic[j]=dic[j]+1
                if j not in dic:
                    dic[j]=1
    with open("task6.json","w+") as file:
        json.dump(dic,file,indent=4)
analyse_movies_directors() 