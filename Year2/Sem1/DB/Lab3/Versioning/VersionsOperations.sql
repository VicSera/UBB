USE ClimbingDB
GO

-- versions table deletion, creationg and data insertion
DROP TABLE versions
GO

CREATE TABLE versions (
	v int UNIQUE NOT NULL,
	nextProc varchar(255),
	prevProc varchar(255)
)
GO

INSERT INTO versions (v, nextProc, prevProc) VALUES
	(0, NULL, NULL)
GO

DROP PROCEDURE newVersion
GO

-- create a new version using the given procedure and its inverse
CREATE PROCEDURE newVersion(@proc VARCHAR(255), @inverseProc VARCHAR(255)) AS
BEGIN

DECLARE @currentVersion int
SET @currentVersion = (SELECT v FROM currentVersion)

-- delete any versions that come after this one, because they are unretrievable
DELETE FROM versions
WHERE v > @currentVersion

-- set the current version's next to @proc
UPDATE versions
SET nextProc = @proc
WHERE v = @currentVersion

SET @currentVersion = @currentVersion + 1

-- add the next version
INSERT INTO versions(v, nextProc, prevProc) VALUES
	(@currentVersion, NULL, @inverseProc)

-- increment current version
EXEC incrementVersion
END
GO

EXEC newVersion 'a', 'b'
GO

DROP PROCEDURE goToPreviousVersion
GO

CREATE PROCEDURE goToPreviousVersion AS
BEGIN
-- get current version
DECLARE @currentVersion int
SET @currentVersion = (SELECT v FROM currentVersion)

-- execute 'previous' procedure
DECLARE @procedure VARCHAR(255)
SET @procedure = (SELECT prevProc FROM versions WHERE v = @currentVersion)
EXEC @procedure

-- go to previous version
EXEC decrementVersion
END

DROP PROCEDURE goToNextVersion
GO

CREATE PROCEDURE goToNextVersion AS
BEGIN
-- get current version
DECLARE @currentVersion int
SET @currentVersion = (SELECT v FROM currentVersion)

-- execute 'next' procedure
DECLARE @procedure VARCHAR(255)
SET @procedure = (SELECT nextProc FROM versions WHERE v = @currentVersion)
EXEC @procedure

-- go to previous version
EXEC incrementVersion
END
GO

CREATE PROCEDURE goToVersion (@targetVersion int) AS
BEGIN
-- get current version
DECLARE @currentVersion int
SET @currentVersion = (SELECT v FROM currentVersion)

IF @currentVersion > @targetVersion 
	WHILE (SELECT v FROM currentVersion) <> @targetVersion
		EXEC goToPreviousVersion
ELSE IF @currentVersion < @targetVersion
	WHILE (SELECT v FROM currentVersion) <> @targetVersion
		EXEC goToNextVersion
END
GO