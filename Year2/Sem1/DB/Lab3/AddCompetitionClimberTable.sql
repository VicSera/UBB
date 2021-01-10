USE ClimbingDB
GO

DROP PROCEDURE _dropCompetitionClimberTable
GO

DROP PROCEDURE _addCompetitionClimberTable
GO

CREATE PROCEDURE _dropCompetitionClimberTable AS
BEGIN
DROP TABLE competitionClimber
END
GO

CREATE PROCEDURE _addCompetitionClimberTable AS
BEGIN
CREATE TABLE competitionClimber (
	climberId int NOT NULL,
	careerStartDate date,
	CONSTRAINT FK_competitionClimber_climber FOREIGN KEY (climberId) REFERENCES climber(id),
	CONSTRAINT id_unique UNIQUE (climberId)
)
END
GO

DROP PROCEDURE addCompetitionClimberTable
GO

CREATE PROCEDURE addCompetitionClimberTable AS
BEGIN
EXEC _addCompetitionClimberTable
EXEC newVersion '_addCompetitionClimberTable', '_dropCompetitionClimberTable' 
END
GO

DROP PROCEDURE dropCompetitionClimberTable
GO

CREATE PROCEDURE dropCompetitionClimberTable AS
BEGIN
EXEC _dropCompetitionClimberTable
EXEC newVersion '_dropCompetitionClimberTable', '_addCompetitionClimberTable'
END
GO