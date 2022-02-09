import json
import requests 
import os 
with open("task1.json","r+") as file8:
    data=json.load(file8) 
def txt(a):
    for i in a: 
        path=("/home/admin123/Desktop/mycode/task8"+i["movie_name"]+".text")
        if os.path.exists(path):
            pass
        else:
            create=open("/home/admin123/Desktop/mycode/task8"+i["movie_name"]+".text","w")
            url=requests.get(i["url"])
            create1=create.write(url.text)
            create.close()
txt(data)  