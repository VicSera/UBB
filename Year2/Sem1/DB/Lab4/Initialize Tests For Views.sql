USE ClimbingDB
GO

DBCC CHECKIDENT ( 'Views' , RESEED, 0);

DELETE FROM Views
GO

INSERT INTO Views (Name) VALUES
	('climbersWithLongName'),
	('citiesInRomaniaView'),
	('climbersWithMostRoutesCompletedView')
GO

DBCC CHECKIDENT ( 'Tests' , RESEED, 0);
DELETE FROM Tests
GO

INSERT INTO Tests (Name) VALUES
	('Climbers with name length > 2'),
	('Cities in Romania'),
	('Climbers with Most Routes Completed')
GO

DELETE FROM TestViews
GO

INSERT INTO TestViews (TestID, ViewID) VALUES
	(1, 1),
	(2, 2),
	(3, 3)
GO