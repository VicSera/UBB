USE ClimbingDB
GO

DELETE FROM friendship
GO

CREATE PROCEDURE populate_friendship AS
INSERT INTO friendship(climber1_id, climber2_id) VALUES
	(1, 2),
	(1, 3),
	(4, 5);


-- Fails because of the foreign key constraint - there's no climber with ID 9
INSERT INTO friendship(climber1_id, climber2_id) VALUES
	(3, 9);