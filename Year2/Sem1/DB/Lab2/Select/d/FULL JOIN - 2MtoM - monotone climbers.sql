USE ClimbingDB
GO

-- Select the climber id of each climber who participates only in indoor events or only in outdoor events
SELECT COALESCE(c_iE.climber_id, c_oE.climber_id) AS climber_id
FROM climber_indoorEvent c_iE
FULL JOIN climber_outdoorEvent c_oE
ON c_iE.climber_id = c_oE.climber_id
WHERE c_iE.climber_id IS NULL OR c_oE.climber_id IS NULL
GROUP BY c_iE.climber_id, c_oE.climber_id
GO