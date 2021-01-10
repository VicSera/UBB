USE ClimbingDB
GO

-- Find climbers who completed the most routes
SELECT climber_id
FROM 
	(SELECT c1.id AS climber_id, COUNT(*) as routes_completed
	FROM climber c1
	INNER JOIN climber_climbingRoute c_cR1 ON c1.id = c_cR1.climber_id
	WHERE c_cR1.completion_status = 'Complete'
	GROUP BY c1.id) AS subquery
WHERE routes_completed >= ALL
	(SELECT COUNT(*)
	FROM climber c2
	INNER JOIN climber_climbingRoute c_cR2 ON c.id2 = c_cR2.climber_id
	WHERE c_cR2.completion_status = 'Complete'
	GROUP BY c2.id)


SELECT climber_id
FROM 
	(SELECT c1.id AS climber_id, COUNT(*) as routes_completed
	FROM climber c1
	INNER JOIN climber_climbingRoute c_cR1 ON c1.id = c_cR1.climber_id
	WHERE c_cR1.completion_status = 'Complete'
	GROUP BY c1.id) AS subquery
WHERE routes_completed = 
	(SELECT MAX(cnt) 
	FROM
		(SELECT COUNT(*) as cnt
		FROM climber c2
		INNER JOIN climber_climbingRoute c_cR2 ON c2.id = c_cR2.climber_id
		WHERE c_cR2.completion_status = 'Complete'
		GROUP BY c2.id) AS subquery2)