from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://economipedia.com/actual/empresas-mas-grandes-del-mundo-2022.html'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
#busco la tabla y la etiqueta tr
rows = soup.find('table').find_all('tr')

#genero las listas
empresa = []
pais = []
sector = []
cap_bursatil = []


#busco los contenidos de las etiquetas y los coloco en las lists, si hay un error continuo
for row in rows:
    try:
        empresa.append(row.find_all('td')[1].get_text())
        pais.append(row.find_all('td')[2].get_text())
        sector.append(row.find_all('td')[3].get_text())
        cap_bursatil.append(row.find_all('td')[4].get_text())
    except:
        print("1 error ignorado")
    continue

#genero el DataFrame con Pandas
df = pd.DataFrame({"Empresa" : empresa, "Pais" : pais, "Sector" : sector, "Capitalización Bursatil": cap_bursatil})
print(df)
#lo exporto a formato xlsx para el cargado a la base de datos
df.to_excel("empresas1.xlsx")
