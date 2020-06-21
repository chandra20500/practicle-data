# practicle-data

these were the library i used

import requests
import pandas as pd
from bs4 import BeautifulSoup

created three empty lists

p_name = []
p_rating = []
p_price = []

scraping data

r = requests.get(url)
soup = BeautifulSoup(r.content)
name = soup.find_all("p", {"class":"_2qAcZ"})
for item in name:
    p_name.append(item.string)

r = requests.get(url)
soup = BeautifulSoup(r.content)
price = soup.find_all("p", {"class":"_2lKKI"})
for item in price:
    p_price.append(item.string)
        
r = requests.get(url)
soup = BeautifulSoup(r.content)
rating = soup.find_all("div", {"class":"_1sd66"})
for item in rating:
    p_rating.append(item.string)

pasting data to flipkart.csv

df2 = pd.DataFrame(p_price)
df1 = pd.DataFrame(p_rating)
df0 = pd.DataFrame(p_name)

result = pd.concat([df0,df1,df2], axis=1, sort=False)

print(result)

result.to_csv('flipkart.csv') 
