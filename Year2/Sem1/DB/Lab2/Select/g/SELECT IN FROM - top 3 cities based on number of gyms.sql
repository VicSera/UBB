USE ClimbingDB
GO

-- Select the top three cities based on number of gyms
SELECT TOP (3) gym_count_per_city.city_code AS city_code, gym_count_per_city.gym_count as gym_count
FROM 
	(SELECT gym.city_code AS city_code, COUNT(*) AS gym_count
	FROM gym
	GROUP BY gym.city_code) AS gym_count_per_city
ORDER BY gym_count_per_city.gym_count DESC