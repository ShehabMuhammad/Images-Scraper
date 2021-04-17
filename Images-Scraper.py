import requests, time 
import re , random
import tkinter as t
root = t.Tk();root.title("Images Scraper")

ent = t.Entry(root)

def bolo():
    url = ent.get()
    # connect to the url
    website = requests.get(url)
    # read html
    html = website.text
    # use re.findall to grab all the links
    #links = re.findall('"((http|ftp)s?://.*?(.jpg|.png))"' , html);
    arr=[".jpeg",".jpg",".png",".tiff"];SFX = "|".join(arr)
    links = re.findall("([^\s'\"]+("+ SFX+"))" , html)
    #links = re.findall("([^\s'\"]+("+ +"))" , html)
    for link in links:
        File = link[0].replace("\\","");parts=File.split("."); suffix=parts[len(parts)-1]
        print("Processing",File)
        try:
            i = requests.get(File) if File.startswith("http") else requests.get(url+File)
            with open('F:/Python projects/Images/Image'+str(random.random())+str(time.strftime("%Y_%m_%d_%H_%M_%S"))+ (suffix if suffix in arr else ".jpg"), 'wb') as Hola:
                Hola.write(i.content)    
                print("Wrote : ", File)
        except Exception as e:
            raise e;
            print("Continuing..");
            continue;        
    print("[FINISHED!]")
        
b = t.Button(root, text='GET', command=bolo).pack()

ent.pack()

q = t.Button(root, text='Quit', command=root.destroy).pack()

