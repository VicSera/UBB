USE ClimbingDB
GO

-- get all the climbers who frequent gym 1, except for climber 1
SELECT *
FROM climber
WHERE climber.gym_id = 1
EXCEPT
SELECT *
FROM climber
WHERE climber.id = 1
GO