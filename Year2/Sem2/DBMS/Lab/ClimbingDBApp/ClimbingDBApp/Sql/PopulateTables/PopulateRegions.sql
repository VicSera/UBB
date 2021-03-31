USE ClimbingDB
GO

DELETE FROM region
GO

CREATE OR ALTER PROCEDURE populate_region AS
INSERT INTO region (code, region_name, country_code) VALUES
	(1, 'Neamt', 1),
	(2, 'Cluj', 1), 
	(4, 'Community of Madrid', 2),
	(5, 'Lukovit', 3);
GO