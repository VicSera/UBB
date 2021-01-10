USE ClimbingDB
GO

EXEC goToVersion 0
GO

-- Op 1
EXEC addCandidateKeyForGym -- 1
GO

EXEC dropCandidateKeyForGym -- 0
GO

-- Op 2
EXEC addCompetitionClimberTable -- 1
GO

EXEC dropCompetitionClimberTable -- 0
GO

-- Op 3
EXEC addCountryPK -- 1
GO

EXEC dropCountryPK -- 0
GO

-- Op 4
EXEC addCragFK -- 0
GO

EXEC dropCragFK -- 1
GO

-- Op 5
EXEC addDefaultCompletionStatusToClimber_ClimbingRoute -- 1
GO

EXEC dropDefaultCompletionStatusToClimber_ClimbingRoute -- 0
GO

-- Op 6
EXEC addClimbingRouteLength -- 1
GO

EXEC removeClimbingRouteLength -- 0
GO

-- Op 7
EXEC changeGradeToInt -- 1
GO

EXEC changeGradeToString -- 0
GO