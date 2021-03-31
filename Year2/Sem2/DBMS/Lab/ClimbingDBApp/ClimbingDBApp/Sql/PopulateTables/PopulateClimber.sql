USE ClimbingDB
GO

DROP PROCEDURE IF EXISTS delete_from_climber;
GO
DROP PROCEDURE IF EXISTS populate_climber;
GO

CREATE PROCEDURE delete_from_climber
AS
DELETE FROM friendship
DELETE FROM climber;
GO

CREATE PROCEDURE populate_climber
AS
INSERT INTO climber (id, full_name, gym_id) VALUES
	(1, 'Victor Sera', 1),
	(2, 'Soritau Adrian', 1),
	(3, 'Chirila Ilie', 1),
	(4, 'Bogdan Sbiera', 2),
	(5, 'Marta Pali', 2),
	(6, 'Bogdan Bota', 2),
	(7, 'Akos Cosma', 3),
	(8, 'Mircea Andrau', 3);
GO
