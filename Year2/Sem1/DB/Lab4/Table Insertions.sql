USE ClimbingDB
GO

CREATE OR ALTER PROCEDURE insertDataInClimber (@numberOfEntries INT) AS
BEGIN
	DECLARE @index INT
	DECLARE @randomName varchar(255)
	SET @index = 1
	WHILE @index < @numberOfEntries
	BEGIN
		SET @randomName = CONVERT(varchar(255), NEWID())
		INSERT INTO climber (id, full_name) VALUES (@index, @randomName)
		SET @index = @index + 1
	END
END
GO

CREATE OR ALTER PROCEDURE insertDataInRoute (@numberOfEntries INT) AS
BEGIN
	DECLARE @index INT
	DECLARE @randomName varchar(255)
	DECLARE @randomGrade INT
	DECLARE @cragId INT
	SET @index = 1
	WHILE @index < @numberOfEntries
	BEGIN
		SET @randomName = CONVERT(varchar(255), NEWID())
		SET @randomGrade = ROUND(RAND() * 5 + 5,0)
		SET @cragId = (SELECT TOP 1 crag.id FROM crag ORDER BY NEWID())
		INSERT INTO climbingRoute(id, route_name, crag_id, grade) VALUES (@index, @randomName, @cragId, @randomGrade)
		SET @index = @index + 1
	END
END
GO

CREATE OR ALTER PROCEDURE insertDataInClimberRoute (@numberOfEntries INT) AS
BEGIN
	DECLARE @index INT
	DECLARE @climberId INT
	DECLARE @routeId INT
	DECLARE @randomGrade INT
	DECLARE @status INT
	SET @index = 1
	WHILE @index < @numberOfEntries
	BEGIN
		SET @climberId = (SELECT TOP 1 climber.id FROM climber ORDER BY NEWID())
		SET @routeId = (SELECT TOP 1 climbingRoute.id FROM climbingRoute ORDER BY NEWID())
		SET @randomGrade = ROUND(RAND() * 5 + 5, 0)
		SET @status = 'In progress'
		INSERT INTO climber_climbingRoute(climber_id, climbingRoute_id, completion_status, proposed_grade) VALUES (@climberId, @routeId, @status, @randomGrade)
		SET @index = @index + 1
	END
END
GO