from sqlite3 import Cursor
from tkinter import INSERT
import pymysql
conexion = pymysql.connect(host='localhost',
                             user='root',
                             password="ingrese su contraseña asociada a Mysql",
                             db='empresas')
Cursor= conexion.cursor()
Cursor.execute("CREATE TABLE IF NOT EXISTS Ranking_por_sector (id INT AUTO_INCREMENT PRIMARY KEY, Sector VARCHAR(255), Total FLOAT(20))")
#seleccionamos los distintos sectores
consulta = "SELECT DISTINCT Sector FROM Empresas"
Cursor.execute(consulta)
sectores = Cursor.fetchall()
ranking=[]
for sector in sectores :
    consulta = "SELECT SUM(Capitulizacion_Bursatil) FROM Empresas WHERE Sector = '%s' " %sector
    #sumo la capitalizacion burzatil por sector
    Cursor.execute(consulta)
    #Guardo la consulta. 
    total= Cursor.fetchone()
    #Como devuelve una tupla, para poder guardarlo mas adelante, accedemos al dato con la instruccion total[0] 
    registro=(sector,total[0])
    ranking.append(registro)
Cursor.executemany("INSERT INTO Ranking_por_sector VALUES (?,?)", ranking)  
conexion.commit()
Cursor.close()
conexion.close()


  
    
     
