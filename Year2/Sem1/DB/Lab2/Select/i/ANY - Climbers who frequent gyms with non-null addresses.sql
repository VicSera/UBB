USE ClimbingDB
GO

-- Select all the climbers who frequent a gym with a non-null address (so that you can visit them :D)
SELECT *
FROM climber
WHERE climber.gym_id = ANY
	(SELECT gym.id
	FROM gym
	WHERE gym.local_address IS NOT NULL)

SELECT *
FROM climber
WHERE climber.gym_id IN
	(SELECT gym.id
	FROM gym
	WHERE gym.local_address IS NOT NULL)