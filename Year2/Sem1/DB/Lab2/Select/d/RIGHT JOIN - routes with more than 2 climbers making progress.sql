USE ClimbingDB
GO

SELECT cR.route_name, COUNT(climber_id) AS working_climbers
FROM climber_climbingRoute c_cR
RIGHT JOIN climbingRoute cR ON c_cR.climbingRoute_id = cR.id
WHERE completion_status = 'In progress' OR completion_status IS NULL
GROUP BY cR.route_name
HAVING COUNT(climber_id) >= 2
GO