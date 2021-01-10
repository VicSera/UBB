USE ClimbingDB
GO

SELECT DISTINCT c.city_name
FROM city c
INNER JOIN region r ON c.region_code = r.code
INNER JOIN country ctr ON r.country_code = ctr.code
WHERE ctr.country_name = 'Romania'
GO