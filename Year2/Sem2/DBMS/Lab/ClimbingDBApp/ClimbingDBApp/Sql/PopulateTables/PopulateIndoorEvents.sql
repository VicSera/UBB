USE ClimbingDB
GO

CREATE OR ALTER PROCEDURE populate_indoorEvent AS
INSERT INTO indoorEvent(id, event_name, gym_id, begin_date, end_date) VALUES
	(1, 'Skai Open 4.0', 1, '2020-10-20', '2020-10-30'),
	(2, 'Cupa Nationala de Escalada', 1, '2020-11-12', '2020-11-12'),
	(3, 'Skai Open 3.0', 1, '2019-10-20', '2019-10-30')
GO