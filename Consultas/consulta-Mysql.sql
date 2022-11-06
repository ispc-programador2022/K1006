SELECT * FROM empresas.empresas order by "Capitalización Bursatil" LIMIT 5;
SELECT pais, COUNT(*) as cantidad_empresas FROM empresas group by Pais order by cantidad_empresas desc;
