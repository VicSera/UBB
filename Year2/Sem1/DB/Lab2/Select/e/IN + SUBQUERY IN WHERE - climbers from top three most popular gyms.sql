USE ClimbingDB
GO

-- Select the climbers who frequent the top 2 most popular gyms
SELECT *
FROM climber
WHERE gym_id IN 
	(SELECT TOP (2) gym_id
	FROM climber
	GROUP BY gym_id
	ORDER BY COUNT(*) DESC)