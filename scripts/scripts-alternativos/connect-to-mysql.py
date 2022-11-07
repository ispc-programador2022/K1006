#importo las librerias necesarias
import mysql.connector
import pandas as pd
"""
primero cree una db llamada empresas em mysql
"""
#conectar a la base de datos
con = mysql.connector.connect(host='localhost', user='root', password='123456789', database='empresas') #poner la contraseña de mysql
cursor = con.cursor()

#creo la tabla con id auto incrementado, empresa, pais, sector y capital bursatil
cursor.execute("CREATE TABLE IF NOT EXISTS empresas (id INT AUTO_INCREMENT PRIMARY KEY, empresa VARCHAR(255), pais VARCHAR(255), sector VARCHAR(255), cap_bursatil FLOAT(10))")

#creo el sql para insertar los datos
sql = "insert into empresas(empresa, pais, sector, cap_bursatil) values (%s, %s, %s, %s)"

#leer los datos del csv con pandas
df = pd.read_csv('empresas2022.csv') #el csv debe estar en la misma carpeta que el script

#convertir el dataframe en una lista
lista = df.values.tolist()

#insertar los datos en la tabla
cursor.executemany(sql, lista)
con.commit()

#cierro la conexion
cursor.close()
