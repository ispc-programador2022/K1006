from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://economipedia.com/actual/empresas-mas-grandes-del-mundo-2022.html'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

rows = soup.find('table').find('tbody').find_all('tr')
# print(rows[0].find_all('td')[1].get_text())
# print(rows[0].find_all('td')[2].get_text())
# print(rows[0].find_all('td')[3].get_text())
# print(rows[0].find_all('td')[4].get_text())

empresa = []
pais = []
sector = []
cap_bursatil = []
for row in rows:
  empresa.append(row.find_all('td')[1].get_text())
  pais.append(row.find_all('td')[2].get_text())
  sector.append(row.find_all('td')[3].get_text())
  cap_bursatil.append(row.find_all('td')[4].get_text())
  # print(empresa, pais, sector, cap_bursatil)
  # print(len(empresa))

df = pd.DataFrame({"Empresa" : empresa, "Pais" : pais, "Sector" : sector, "Capitalización Bursatil": cap_bursatil})
df