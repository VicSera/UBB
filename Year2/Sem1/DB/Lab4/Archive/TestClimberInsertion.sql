USE ClimbingDB
GO

INSERT INTO Tests (Name) VALUES ('Test insertion of data into climber table') 
GO

INSERT INTO Tables (Name) VALUES ('climber')
GO

INSERT INTO TestTables (TestID, TableID, NoOfRows, Position) VALUES
	(1, 1, 1000, 1)
GO

--------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------
DROP PROCEDURE insertDataInClimber
GO
--------------------------------------------------------------------------------------------------
CREATE PROCEDURE insertDataInClimber (@numberOfEntries INT) AS
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
--------------------------------------------------------------------------------------------------
CREATE OR ALTER PROCEDURE testClimberDataInsertion AS
BEGIN
	DELETE FROM climber
	DECLARE @begin DATETIME
	DECLARE @end DATETIME
	SET @begin = GETDATE()
	EXEC insertDataInClimber 1000
	SET @end = GETDATE()
	INSERT INTO TestRuns (Description, StartAt, EndAt) VALUES ('Insert 1000 values into climber', @begin, @end)
	INSERT INTO TestRunTables (TestRunID, TableID, StartAt, EndAt) VALUES (1, 1, @begin, @end)
END
GO
--------------------------------------------------------------------------------------------------
EXEC testClimberDataInsertion
GO
--------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------