USE ClimbingDB
GO

-- Select all the gyms whose number of climbers is greater than the average number of climbers in a gym
CREATE VIEW aboveAverageGyms AS
SELECT a.gym_id
FROM climber a
GROUP BY a.gym_id
HAVING COUNT(*) >=
	(SELECT COUNT(b.id) / COUNT(g.id)
	FROM climber b, gym g) 
GO

SELECT *
FROM aboveAverageGyms
GO