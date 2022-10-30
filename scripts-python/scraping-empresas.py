import pandas as pd
from bs4 import BeautifulSoup
url="https://economipedia.com/actual/empresas-mas-grandes-del-mundo-2022.html"
aa=pd.read_html(url)
#print(aa)
print("cantidad de tablas detectadas",len(aa))
print(aa[0])
tabla_total =aa[0]
#print(tabla_total)
#exportar tabla
tabla_total.to_excel("tabla_prueba.xlsx")
