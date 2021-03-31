USE ClimbingDB
GO

DELETE FROM city
GO

CREATE OR ALTER PROCEDURE populate_city AS
INSERT INTO city (code, city_name, region_code) VALUES
	(1, 'Cluj-Napoca', 2),
	(2, 'Sihla', 1),
	(3, 'Turda', 2),
	(4, 'City4', 4),
	(5, 'City5', 4),
	(6, 'City6', 5);
GO