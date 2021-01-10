USE ClimbingDB
GO

SELECT *
  FROM versions
GO

SELECT *
  FROM currentVersion
GO

EXEC goToVersion 6
GO

EXEC goToVersion 1
GO

SELECT *
FROM CompetitionClimber
GO