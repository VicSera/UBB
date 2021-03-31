USE ClimbingDB
GO

CREATE OR ALTER PROCEDURE populate_climber_outdoorEvent AS
INSERT INTO climber_outdoorEvent(climber_id, event_id) VALUES 
	(3, 1),
	(3, 2),
	(4, 1);