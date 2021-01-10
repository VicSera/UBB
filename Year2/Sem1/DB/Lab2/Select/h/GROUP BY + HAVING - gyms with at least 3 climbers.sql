USE ClimbingDB
GO

-- Select the ids of the gyms that have at least 3 people frequenting them
SELECT gym_id
FROM climber
GROUP BY gym_id
HAVING COUNT(*) > 2
GO