from task1 import scrape_top_list
details=scrape_top_list()
def group_by_decade(movies):
    unique_year=[]
    movie_dic={} 
    for i in movies:
        for j in i:
            if j=="year":
                if (i[j]) not in unique_year:
                    unique_year.append(i[j])
        unique_year.sort() 
    decate_list=[] 
    for j in unique_year:
        mod=int(j)%10 
        decode=int(j)-mod 
        if decode not in decate_list: 
            decate_list.append(decode)
    for x in decate_list:
        movie_dic[x]=[]

    for x in movie_dic:
        dec10=int(x)+9
        for i in movies:
            for j in i:
                if  j=="year":
                    if (int(i[j]))<=dec10 and (int(i[j]))>=x:
                        movie_dic[x].append(i)
    import json
    with open("task3.json","w+") as file: 
        json.dump(movie_dic,file,indent=4) 
    return(movie_dic) 
group_by_decade(details)