USE ClimbingDB

DROP PROCEDURE _addCandidateKeyForGym
GO

CREATE PROCEDURE _addCandidateKeyForGym AS
BEGIN
ALTER TABLE gym
ADD CONSTRAINT gymCandidate UNIQUE(gym_name, city_code)
END
GO

DROP PROCEDURE _dropCandidateKeyForGym
GO

CREATE PROCEDURE _dropCandidateKeyForGym AS
BEGIN
ALTER TABLE gym
DROP gymCandidate
END
GO

DROP PROCEDURE addCandidateKeyForGym
GO

CREATE PROCEDURE addCandidateKeyForGym AS
BEGIN
EXEC _addCandidateKeyForGym
EXEC newVersion '_addCandidateKeyForGym', '_dropCandidateKeyForGym' 
END
GO

DROP PROCEDURE dropCandidateKeyForGym
GO

CREATE PROCEDURE dropCandidateKeyForGym AS
BEGIN
EXEC _dropCandidateKeyForGym
EXEC newVersion '_dropCandidateKeyForGym', '_addCandidateKeyForGym'
END
GO