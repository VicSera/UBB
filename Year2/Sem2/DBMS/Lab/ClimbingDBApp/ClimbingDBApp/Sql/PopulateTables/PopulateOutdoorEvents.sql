USE ClimbingDB
GO

CREATE OR ALTER PROCEDURE populate_outdoorEvent AS
INSERT INTO outdoorEvent(id, event_name, crag_id, begin_date, end_date) VALUES
	(1, 'Herculane Climbing Open', 1, '2020-7-15', '2020-7-18'),
	(2, 'RICO', 1, '2020-6-12', '2020-6-14')
GO