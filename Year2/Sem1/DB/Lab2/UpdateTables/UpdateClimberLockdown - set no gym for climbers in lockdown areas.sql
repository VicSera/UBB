USE ClimbingDB
GO

-- For every climber that frequents a gym in a certain city, set his frequented gym to NULL
-- For example, this could be useful if a city goes into lockdown and the gyms currently have no clients
UPDATE climber
SET gym_id = NULL
WHERE gym_id IN
	(SELECT gym.id
	FROM gym
	WHERE gym.city_code = 5)