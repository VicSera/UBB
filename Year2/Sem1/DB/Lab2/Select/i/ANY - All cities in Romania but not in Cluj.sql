USE ClimbingDB
GO

-- Select all the cities that are in a region in Romania but not in Cluj
SELECT *
FROM city
WHERE city.region_code = ANY
	(SELECT region.code
	FROM region
	WHERE region.region_name <> 'Cluj' AND region.country_code = 1)

SELECT *
FROM city
WHERE city.region_code IN
	(SELECT region.code
	FROM region
	WHERE region.region_name <> 'Cluj' AND region.country_code = 1)