# Top 5 capitalización bursátil
SELECT * FROM empresas.empresas order by "Capitalización Bursatil" LIMIT 5;

# Cantidad de empresas por país
SELECT pais, COUNT(*) as cantidad_empresas FROM empresas group by Pais order by cantidad_empresas desc;

#Cantidad de empresas por sector
SELECT sector, COUNT(*) as cantidad_empresas_sector FROM empresas group by sector order by cantidad_empresas_sector desc;

#Cuáles son los distintos sectores
SELECT DISTINCT(sector)
FROM empresas
ORDER BY sector;

#Empresa con mayor Capitalzación bursátil por sector
WITH empresas AS (
  SELECT *,
    row_number() OVER (PARTITION BY sector ORDER BY cap_bursatil) as row_num
  FROM empresas
)
SELECT *
FROM empresas
WHERE row_num = 1;
