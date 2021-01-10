USE ClimbingDB
GO

-- Select every climber that frequents a gym in Cluj
SELECT *
FROM climber
WHERE climber.gym_id IN
	(SELECT id
	FROM gym
	WHERE city_code = 1)
GO