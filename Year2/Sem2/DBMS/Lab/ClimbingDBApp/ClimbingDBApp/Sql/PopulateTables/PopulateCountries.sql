USE ClimbingDB
GO

CREATE OR ALTER PROCEDURE populate_country AS
INSERT INTO country (code, country_name) VALUES
	(1, 'Romania'),
	(2, 'Spain'),
	(3, 'Bulgaria');
GO