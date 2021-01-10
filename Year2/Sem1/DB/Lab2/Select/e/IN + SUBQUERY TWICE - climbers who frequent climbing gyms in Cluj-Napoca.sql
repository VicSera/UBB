USE ClimbingDB
GO

SELECT *
FROM climber
WHERE gym_id IN
	(SELECT gym.id
	FROM gym
	WHERE gym.city_code IN
		(SELECT city.code
		FROM city
		WHERE city_name = 'Cluj-Napoca'))
GO