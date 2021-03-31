USE ClimbingDB
GO

DELETE FROM friendship
GO

CREATE OR ALTER PROCEDURE populate_friendship AS
INSERT INTO friendship(climber1_id, climber2_id) VALUES
	(1, 2),
	(1, 3),
	(4, 5);
