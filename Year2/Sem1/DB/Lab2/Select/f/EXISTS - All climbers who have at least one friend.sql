USE ClimbingDB
GO

-- Select all climbers that have at least a friend
SELECT *
FROM climber
WHERE EXISTS
	(SELECT *
	FROM friendship
	WHERE climber.id IN (friendship.climber1_id, friendship.climber2_id))
GO