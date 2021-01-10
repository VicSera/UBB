USE ClimbingDB
GO

DBCC CHECKIDENT ( 'Tables' , RESEED, 0);
DELETE FROM Tables
GO

INSERT INTO Tables (Name) VALUES
	('climber'),
	('climbingRoute'),
	('climber_climbingRoute')
GO


INSERT INTO Tests (Name) VALUES
	('Test climber insertion'),
	('Test route insertion')
GO

INSERT INTO TestTables (TestID, TableID, NoOfRows, Position) VALUES
	(7, 1, 10000, 1),
	(8, 2, 1000, 1),
	(8, 3, 500, 2)
GO

EXEC executeTest 7
GO

EXEC executeTest 8
GO

EXEC performDeletions 7
GO