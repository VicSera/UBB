USE ClimbingDB
GO

CREATE OR ALTER PROCEDURE populate_climber_climbingRoute AS
INSERT INTO climber_climbingRoute(climber_id, climbingRoute_id, completion_status) VALUES
	(1, 1, 'Complete'),
	(2, 1, 'In progress'),
	(1, 2, 'In progress'),
	(2, 2, 'In progress')
GO