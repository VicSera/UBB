USE ClimbingDB
GO

DROP PROCEDURE _changeGradeToInt
GO

CREATE PROCEDURE _changeGradeToInt AS
BEGIN
ALTER TABLE climbingRoute
	ALTER COLUMN grade int
END
GO

DROP PROCEDURE _changeGradeToString
GO

-- Use case: climbing grades aren't graded using just numbers, but also letters. E.g: 7A+, 6C-
-- However, it might be a better idea to keep the column as an integer
CREATE PROCEDURE _changeGradeToString AS
BEGIN
ALTER TABLE climbingRoute
	ALTER COLUMN grade varchar(255)
END
GO

DROP PROCEDURE changeGradeToInt
GO

CREATE PROCEDURE changeGradeToInt AS
BEGIN
EXEC _changeGradeToInt
EXEC newVersion '_changeGradeToInt', '_changeGradeToString' 
END
GO

DROP PROCEDURE changeGradeToString
GO

CREATE PROCEDURE changeGradeToString AS
BEGIN
EXEC _changeGradeToString
EXEC newVersion '_changeGradeToString', '_changeGradeToInt'
END
GO