"data extraction from web pages"

wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

import requests

from bs4 import BeautifulSoup

source = requests.get(wiki).text

soup = BeautifulSoup(source,"lxml")

right_table = soup.find('table',class_='wikitable')

A = []
B = []
C = []
D = []
E = []
F = []

for row in right_table.findAll('tr'):
    cells = row.findAll('td')
    states = row.findAll('th')
    
    # if it is first roww, th(count)=7 and td(count)=0
    #for rest of the rows th(count)=1 and td(count)=6
    
    if len(cells) == 6:
        A.append(cells[1].text.strip())
        B.append(states[0].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        F.append(cells[5].text.strip())
        
        
import pandas as pd

df = pd.DataFrame()
df['State_UT'] = B
df['Admin_cap'] = A
df['Legis_cap'] = C
df['Judi_cap'] = D
df['Year'] = E
df['Former_cap'] = F

df.to_csv('states.csv',index=False)