from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd


url = "https://www.top500.org/list/2017/06/"
data = requests.get(url)

soup = BeautifulSoup(data.content, "lxml")

lists = []
links = []
Rank = []
Site = []
System = []
Cores = []
RmaxTFlops = []
RpeakTFlops = []
PowerkW = []

for j in soup.find_all('ul', class_='pagination'):
    for i in j.find_all('a'):

        if i.text == 'previous' or i.text == 'next':
            pass
        else:
            link = str(url) + str(i.get('href'))
            links.append(link)
    break

for i in links:
    new = requests.get(i)
    soup_new = BeautifulSoup(new.content.decode(encoding='UTF-8'), "lxml")
    table = soup_new.find_all('table')[0]

    for j in table.findAll("td"):
        lists.append(j.text)

for i in lists[::7]:
    Rank.append(i)
for i in lists[1::7]:
    Site.append(i)
for i in lists[2::7]:
    System.append(i)
for i in lists[3::7]:
    Cores.append(i)
for i in lists[4::7]:
    RmaxTFlops.append(i)
for i in lists[5::7]:
    RpeakTFlops.append(i)
for i in lists[6::7]:
    PowerkW.append(i)

df = pd.DataFrame()
df = pd.DataFrame(Rank, columns=['Rank'])

df1 = pd.DataFrame()
df1 = pd.DataFrame(Site, columns=['Site'])

df2 = pd.DataFrame()
df2 = pd.DataFrame(System, columns=['System'])

df3 = pd.DataFrame()
df3 = pd.DataFrame(Cores, columns=['Cores'])

df4 = pd.DataFrame()
df4 = pd.DataFrame(RmaxTFlops, columns=['Rmax[TFlop/s]'])

df5 = pd.DataFrame()
df5 = pd.DataFrame(RpeakTFlops, columns=['Rpeak[TFlop/s]'])

df6 = pd.DataFrame()
df6 = pd.DataFrame(PowerkW, columns=['Power[kW]'])

df7 = pd.DataFrame()
df7 = pd.concat([df, df1, df2, df3, df4, df5, df6], axis=1)


df7.to_csv(r'Top500List_GayatriNambiar.csv', header='True', index='False', encoding='utf-8')

