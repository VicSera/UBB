USE ClimbingDB
GO

-- Select all climbers who go to Skai Urban Crag or Centrala De Escalada
SELECT *
FROM climber
WHERE gym_id = 1 OR gym_id = 2
GO