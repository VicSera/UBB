USE ClimbingDB
GO

-- Get all climbers who have completed any route that is not among the first three
SELECT DISTINCT climber_id
FROM climber_climbingRoute
WHERE climbingRoute_id NOT IN (1, 2, 3)
AND completion_status = 'COMPLETED'
GO