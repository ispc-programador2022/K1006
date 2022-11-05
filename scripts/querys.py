import pymysql
import csv
import pandas as pd
try:
    conexion = pymysql.connect(host='localhost',
                             user='root',
                             password="Ingrese contraseña Mysql:",
                             db='empresas')
    try:
        #genero consulta
        with conexion.cursor() as cursor:
            consulta = '''
                        Select pais, COUNT(*)  FROM empresas group by Pais;
                        '''


            cursor.execute(consulta)
            empresas = cursor.fetchall()
            for emp in empresas:
                print(emp)


    finally:
            conexion.close()
#en caso de errores los los visualizo
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
    print("Ocurrió un error al conectar: ", e)
