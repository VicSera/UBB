USE ClimbingDB
GO

-- Find the gyms with the lowest (non-zero) number of climbers
SELECT gym_id, climber_count
FROM 
	(SELECT c1.gym_id AS gym_id, COUNT(*) as climber_count
	FROM climber c1
	GROUP BY c1.gym_id) AS subquery
WHERE climber_count <= ALL
	(SELECT COUNT(*)
	FROM climber c2
	GROUP BY c2.gym_id)


SELECT gym_id, climber_count
FROM 
	(SELECT c1.gym_id AS gym_id, COUNT(*) as climber_count
	FROM climber c1
	GROUP BY c1.gym_id) AS subquery
WHERE climber_count =
	(SELECT MIN(cnt)
	FROM
		(SELECT COUNT(*) AS cnt
		FROM climber c2
		GROUP BY c2.gym_id) AS subquery2)