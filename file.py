import requests
url = 'https://www.flipkart.com/amp/watches/fastrack~brand/pr?otracker=nmenu_sub_Men_0_Fastrack&sid=r18&start='
import pandas as pd

links = []

for i in range(11):
    links.append(url + str(60*i))
    

r = requests.get(url)

pr = []
pn = []
pp = []

from bs4 import BeautifulSoup

for link in links:
    r = requests.get(link)
    soup = BeautifulSoup(r.content)
    data = soup.find_all("div", {"class":"_1jJGh"})
    for item in data:
        name = item.find_all('p', {"class":"_2qAcZ"})
        rating = item.find_all('div', {"class":"_1sd66"})
        price = item.find_all('p', {"class":"_2lKKI"})
        if len(rating) == 0:
            pr.append(0)
        for j in rating:
            pr.append(j.text)
        if len(price) == 0:
            pp.append(0)
        for j in price:
            pp.append(j.text)
        if len(name) == 0:
            pn.append(0)
        for j in name:
            pn.append(j.text)
        

df1 = pd.DataFrame(pr)
df2 = pd.DataFrame(pp)
df3 = pd.DataFrame(pn)
        
result = pd.concat([df1,df2,df3], axis=1, sort=False)

result.to_csv("phones.csv")
