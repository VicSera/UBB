USE ClimbingDB
GO

CREATE OR ALTER PROCEDURE executeTest (@testId INT) AS
BEGIN
	DECLARE @startTime DATETIME
	DECLARE @endTime DATETIME
	DECLARE @testRunId INT
	DECLARE @description VARCHAR(255)

	-- record starting time
	SET @startTime = SYSDATETIME()
	SET @description = (SELECT Name FROM Tests WHERE TestID = @testId)

	INSERT INTO TestRuns (Description, StartAt) VALUES (@description, @startTime)

	SET @testRunId = (SELECT TOP 1 TestRunID FROM TestRuns ORDER BY TestRunID DESC)

	---- Case where the test is for tables
	-- first, perform deletions in reverse order
	EXEC performDeletions @testId

	-- secondly, perform insertions in order
	EXEC performInsertions @testId, @testRunId


	---- Case where the test is for views
	EXEC performSelectOnView @testId, @testRunId

	-- record ending time
	SET @endTime = SYSDATETIME()

	-- update ending time for the test run
	UPDATE TestRuns SET EndAt = @endTime WHERE TestRunID = @testRunId
END
GO

CREATE OR ALTER PROCEDURE performDeletions (@testId INT) AS
BEGIN
	DECLARE deletionCursor CURSOR
	FOR SELECT t.Name 
		FROM TestTables tt INNER JOIN Tables t ON tt.TableID = t.TableID
		WHERE tt.TestID = @testId ORDER BY Position DESC

	DECLARE @tableName VARCHAR(255)

	OPEN deletionCursor
	FETCH NEXT FROM deletionCursor INTO @tableName
	
	WHILE @@FETCH_STATUS = 0
	BEGIN
		EXEC ('DELETE FROM ' + @tableName)
		FETCH NEXT FROM deletionCursor INTO @tableName
	END

	CLOSE deletionCursor
	DEALLOCATE deletionCursor
END
GO

CREATE OR ALTER PROCEDURE performInsertions (@testId INT, @testRunId INT) AS
BEGIN
	DECLARE insertionCursor CURSOR
	FOR SELECT t.Name, t.TableID, tt.NoOfRows
		FROM TestTables tt INNER JOIN Tables t ON tt.TableID = t.TableID
		WHERE tt.TestID = @testId ORDER BY Position

	DECLARE @tableId INT
	DECLARE @tableName VARCHAR(255)
	DECLARE @noOfRows INT
	DECLARE @startTime DATETIME
	DECLARE @endTime DATETIME

	OPEN insertionCursor
	FETCH NEXT FROM insertionCursor INTO @tableName, @tableId, @noOfRows

	WHILE @@FETCH_STATUS = 0
	BEGIN
		SET @startTime = SYSDATETIME()
		EXEC insertDataIntoTable @tableName, @noOfRows
		SET @endTime = SYSDATETIME()

		-- insert data about this insertion
		INSERT INTO TestRunTables (TestRunID, TableID, StartAt, EndAt) VALUES (@testRunId, @tableId, @startTime, @endTime)
		FETCH NEXT FROM insertionCursor INTO @tableName, @tableId, @noOfRows
	END

	CLOSE insertionCursor
	DEALLOCATE insertionCursor
END
GO

CREATE OR ALTER PROCEDURE performSelectOnView (@testId INT, @testRunId INT) AS
BEGIN
	DECLARE @viewName VARCHAR(255)
	DECLARE @viewId INT
	DECLARE @startTime DATETIME
	DECLARE @endTime DATETIME

	SELECT @viewName = v.Name, @viewId = v.ViewID 
	FROM Views v INNER JOIN TestViews tv ON v.ViewID = tv.ViewID WHERE tv.TestID = @testId

	IF @@ROWCOUNT > 0
	BEGIN
		SET @startTime = SYSDATETIME()
		EXEC ('SELECT * FROM ' + @viewName)
		SET @endTime = SYSDATETIME()

		INSERT INTO TestRunViews (TestRunID, ViewID, StartAt, EndAt) VALUES (@testRunId, @viewId, @startTime, @endTime)
	END
END

EXEC executeTest 1
GO

EXEC executeTest 2
GO

EXEC executeTest 3
GO