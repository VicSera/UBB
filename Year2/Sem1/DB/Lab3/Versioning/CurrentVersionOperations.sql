USE ClimbingDB
GO

CREATE TABLE currentVersion (
	v int NOT NULL
)
GO

DELETE FROM currentVersion
GO

INSERT INTO currentVersion (v) VALUES (0)
GO

DROP PROCEDURE incrementVersion
GO

CREATE PROCEDURE incrementVersion AS
BEGIN
UPDATE currentVersion
SET v = v + 1
WHERE (v + 1) IN
	(SELECT versions.v FROM versions)
END
GO

DROP PROCEDURE decrementVersion
GO

CREATE PROCEDURE decrementVersion AS
BEGIN
UPDATE currentVersion
SET v = v - 1
WHERE (v - 1) IN
	(SELECT versions.v FROM versions)
END
GO

EXEC incrementVersion
GO

EXEC decrementVersion
GO
