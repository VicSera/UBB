USE ClimbingDB
GO

-- Select crags with more routes than the average amount of routes completed by a climber
SELECT crag_id
FROM climbingRoute
GROUP BY crag_id
HAVING COUNT(*) > 
	(SELECT AVG(routes_completed)
	FROM 
		(SELECT climber_id, COUNT(*) AS routes_completed
		FROM climber_climbingRoute
		WHERE completion_status = 'Complete'
		GROUP BY climber_id) AS subquery)

	