USE ClimbingDB
GO

-- Delete any friendships between climber 1 and the climbers from any gym that contains Centrala in their name
DELETE FROM friendship
WHERE 
	(climber1_id = 1 OR climber2_id = 1)
	AND
	(climber1_id IN
		(SELECT climber.id
		FROM climber
		INNER JOIN gym ON climber.gym_id = gym.id
		WHERE gym.gym_name LIKE '%Centrala%')
	OR
	climber2_id IN
		(SELECT climber.id
		FROM climber
		INNER JOIN gym ON climber.gym_id = gym.id
		WHERE gym.gym_name LIKE '%Centrala%'))