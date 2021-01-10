USE ClimbingDB
GO

DELETE FROM climber_indoorEvent
GO

CREATE PROCEDURE populate_climber_indoorEvent AS
INSERT INTO climber_indoorEvent (climber_id, event_id) VALUES 
	(1, 1),
	(1, 2),
	(2, 1),
	(3, 1),
	(4, 1);