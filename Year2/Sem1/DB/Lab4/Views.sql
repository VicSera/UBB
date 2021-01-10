USE ClimbingDB
GO

CREATE OR ALTER VIEW climbersWithLongName 
AS 
	SELECT id, full_name FROM climber WHERE LEN(climber.full_name) > 2
GO

CREATE OR ALTER VIEW citiesInRomaniaView AS
	SELECT DISTINCT c.city_name
	FROM city c
	INNER JOIN region r ON c.region_code = r.code
	INNER JOIN country ctr ON r.country_code = ctr.code
	WHERE ctr.country_name = 'Romania'
GO

CREATE OR ALTER VIEW climbersWithMostRoutesCompletedView AS
	SELECT c_cR.climber_id
	FROM climber_climbingRoute c_cR
	WHERE completion_status = 'Complete'
	GROUP BY c_cR.climber_id
	HAVING COUNT(*) = 
		(SELECT MAX(routes_completed)
		FROM 
			(SELECT climber_id, COUNT(*) AS routes_completed
			FROM climber_climbingRoute
			WHERE completion_status = 'Complete'
			GROUP BY climber_id) AS subquery)
GO