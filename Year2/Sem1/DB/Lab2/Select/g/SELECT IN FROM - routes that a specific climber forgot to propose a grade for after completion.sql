USE ClimbingDB
GO

-- Get all the routes for which a specific climber hasn't proposed a grade, but only if he completed the route
SELECT route_id
FROM 
	(SELECT climber_climbingRoute.climbingRoute_id AS route_id, climber_climbingRoute.climber_id AS climber_id
	FROM climber_climbingRoute
	WHERE climber_climbingRoute.completion_status = 'Complete' AND climber_climbingRoute.proposed_grade IS NULL) AS subquery
WHERE climber_id = 1
GO
