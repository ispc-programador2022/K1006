# Top 5 capitalización bursátil
SELECT * FROM empresas.empresas order by "Capitalización Bursatil" LIMIT 5;

# Cantidad de empresas por país
SELECT pais, COUNT(*) as cantidad_empresas FROM empresas group by Pais order by cantidad_empresas desc;

#Cantidad de empresas por sector
SELECT sector, COUNT(*) as cantidad_empresas_sector FROM empresas group by sector order by cantidad_empresas_sector desc;
