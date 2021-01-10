USE ClimbingDB
GO

CREATE PROCEDURE populate_gym AS
INSERT INTO gym (id, gym_name, city_code, local_address) VALUES
	(1, 'Skai Urban Crag', 1, 'Calea Baciului 1-3'),
	(2, 'Centrala de Escalada', 1, 'Strada Horea'),
	(3, 'Gravity', 1, 'Strada Frunzisului'),
	(4, 'Freewall', 1, 'Zona Platinia'),
	(5, 'Gym5', 2, 'Address5'),
	(6, 'Gym6', 2, 'Address6'),
	(7, 'Gym7', 3, 'Address7'),
	(8, 'Gym8', 4, 'Address8'),
	(9, 'Gym9', 4, 'Address9');
GO