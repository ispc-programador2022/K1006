import pymysql
import pandas as pd
import csv
from csv import reader
# primero cree una db llamada empresas en mysql
try:
    conexion = pymysql.connect(host='localhost',
                             user='root',
                             password="ingrese su contraseña",
                             db='empresas')
    #genero consultas, elimino tabla si existe y la creo
    try:
        with conexion.cursor() as cursor:
            consulta = '''
                        DROP TABLE IF EXISTS empresas;
                        '''


            cursor.execute(consulta)
            consulta2 ='''
            create table Empresas (
                        ID int(6),
                        Empresa varchar(15),
                        Pais Varchar(15),
                        Sector varchar(15),
                        Capitulizacion_Bursatil float(20)
                        );'''
            cursor.execute(consulta2)

            #leo csv para importar a mysql
            with open('empresas.csv', newline='', encoding='latin1') as f:
                csv_reader = csv.reader(f, delimiter=",")
                print('Importando CSV')

                #lo importo,
                for row in csv_reader:
                    print(row)
                    consulta3='INSERT INTO empresas(id, Empresa, Pais, Sector, Capitulizacion_Bursatil) VALUES( "%s", "%s", "%s", "%s", "%s")'
                    cursor.execute(consulta3, row)
        #commit db
        conexion.commit()

    finally:
        conexion.close()
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
    print("Ocurrió un error al conectar: ", e)