USE ClimbingDB
GO

DROP PROCEDURE _addClimbingRouteLength
GO

CREATE PROCEDURE _addClimbingRouteLength AS
BEGIN
ALTER TABLE climbingRoute
ADD route_length INT
END
GO

DROP PROCEDURE _removeClimbingRouteLength
GO

CREATE PROCEDURE _removeClimbingRouteLength AS
BEGIN
ALTER TABLE climbingRoute
DROP COLUMN route_length
END
GO

DROP PROCEDURE addClimbingRouteLength
GO

CREATE PROCEDURE addClimbingRouteLength AS
BEGIN
EXEC _addClimbingRouteLength
EXEC newVersion '_addClimbingRouteLength', '_removeClimbingRouteLength' 
END
GO

DROP PROCEDURE removeClimbingRouteLength
GO

CREATE PROCEDURE removeClimbingRouteLength AS
BEGIN
EXEC _removeClimbingRouteLength
EXEC newVersion '_removeClimbingRouteLength', '_addClimbingRouteLength'
END
GO