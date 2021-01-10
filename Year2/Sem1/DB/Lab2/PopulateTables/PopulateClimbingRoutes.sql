USE ClimbingDB
GO

CREATE PROCEDURE populate_climbingRoute AS
INSERT INTO climbingRoute (id, route_name, crag_id, grade) VALUES
	(1, 'Route1', 1, 10),
	(2, 'Route2', 1, 9),
	(3, 'Route3', 2, 7),
	(4, 'Route4', 2, 10),
	(5, 'Route5', 3, 12);