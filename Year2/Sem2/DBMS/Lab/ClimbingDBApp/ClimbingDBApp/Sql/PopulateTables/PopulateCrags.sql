USE ClimbingDB
GO

CREATE OR ALTER PROCEDURE populate_crag AS
INSERT INTO crag (id, crag_name, region_code) VALUES
	(1, 'Cheile Turzii', 2),
	(2, 'Cheile Tureni', 2),
	(3, 'Rimetea Crag', 2)
GO