USE ClimbingDB
GO

CREATE OR ALTER PROCEDURE insertDataIntoTable (@tableName varchar(255), @numberOfEntries INT) AS
BEGIN
	IF @tableName = 'climber'
	BEGIN
		EXEC insertDataInClimber @numberOfEntries
	END

	IF @tableName = 'route'
	BEGIN
		EXEC insertDataInRoute @numberOfEntries
	END

	IF @tableName = 'climberRoute'
	BEGIN
		EXEC insertDataInClimberRoute @numberOfEntries
	END
END
GO