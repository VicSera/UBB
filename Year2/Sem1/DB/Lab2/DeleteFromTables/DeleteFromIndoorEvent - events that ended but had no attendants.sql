USE ClimbingDB
GO

-- Delete indoor events that ended and had no attendants
DELETE FROM indoorEvent
WHERE indoorEvent.id IN
	(SELECT ev.id
	FROM indoorEvent ev
	LEFT JOIN climber_indoorEvent c_iE ON ev.id = c_iE.event_id
	WHERE c_iE.climber_id IS NULL AND end_date < GETDATE())