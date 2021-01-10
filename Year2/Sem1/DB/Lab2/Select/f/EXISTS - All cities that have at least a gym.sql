USE ClimbingDB
GO

-- Select all the cities that have at least a gym
SELECT *
FROM city
WHERE EXISTS
	(SELECT *
	FROM gym
	WHERE gym.city_code = city.code)
GO