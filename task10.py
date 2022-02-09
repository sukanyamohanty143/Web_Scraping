import json

a=open("task5.json","r")
b=json.loads(a.read())

def movie_direc_lang(k):
    list=[]
    dict={}
    for i in k:
        direc = i["Director"]
        for j in direc:
            if j not in list:
                list.append(j)
    # dict={}
    for y in list:
        dic={}
        for x in k:
            
            if y in x["Director"]:
                if "Languagre" in x:
                    for z in x['Languagre']:
                        if z in dic:
                            dic[z]=dic[z]+1
                        if z not in dic:
                            dic[z]=1
        dict[y]=dic
      
        with open("task10.json","w+") as file:
            json.dump(dict,file, indent=4)
movie_direc_lang(b)

