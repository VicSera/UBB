USE ClimbingDB
GO

DROP PROCEDURE testFriendshipInsertion
GO

CREATE PROCEDURE testFriendshipInsertion(@numberOfRows int)
AS
BEGIN
DELETE FROM friendship
DECLARE @check int
DECLARE @currentRow int
DECLARE @firstId int
DECLARE @secondId int
SET @currentRow = 0
WHILE @currentRow <> @numberOfRows
	BEGIN
	-- generate a pair of random climber ids
	SET @firstId = (SELECT TOP 1 climber.id FROM climber ORDER BY NEWID())
	SET @secondId = (SELECT TOP 1 climber.id FROM climber WHERE climber.id <> @firstId ORDER BY NEWID())

	-- check if the pair is not already included in the friendship table
	SET @check = (SELECT COUNT(*) FROM friendship WHERE (climber1_id = @firstId AND climber2_id = @secondId) OR (climber1_id = @secondId AND climber2_id = @firstId))
	IF @check = 0
		BEGIN
		-- if the check passes, insert the pair and increment the current row
		SET @currentRow = @currentRow + 1
		INSERT INTO friendship (climber1_id, climber2_id) VALUES (@firstId, @secondId)
		END
	END
END
GO

EXEC testFriendshipInsertion 5
GO