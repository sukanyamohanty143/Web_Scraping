import json

a=open("task5.json" , "r")
b=json.loads(a.read())
dic={}
def get_genre_details():
    for i in b:
        
        if "Genre" in i:
            a=i["Genre"]
            for j in a:
                if j in dic:
                    dic[j]+=1
                else:
                    dic[j] = 1
    with open("task11.json","w+") as file:
        json.dump(dic, file, indent = 4)
get_genre_details()

