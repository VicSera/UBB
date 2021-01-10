USE ClimbingDB
GO

-- Change a specific climber's frequented gym
UPDATE climber
SET gym_id = 3
WHERE id = 6