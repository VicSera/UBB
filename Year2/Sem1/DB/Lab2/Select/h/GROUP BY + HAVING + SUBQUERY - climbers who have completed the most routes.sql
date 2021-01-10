USE ClimbingDB
GO

-- Select all the climbers who have completed the most routes
SELECT c_cR.climber_id
FROM climber_climbingRoute c_cR
WHERE completion_status = 'Complete'
GROUP BY c_cR.climber_id
HAVING COUNT(*) = 
	(SELECT MAX(routes_completed)
	FROM 
		(SELECT climber_id, COUNT(*) AS routes_completed
		FROM climber_climbingRoute
		WHERE completion_status = 'Complete'
		GROUP BY climber_id) AS subquery)