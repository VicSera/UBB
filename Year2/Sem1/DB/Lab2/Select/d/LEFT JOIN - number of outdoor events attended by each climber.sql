USE ClimbingDB
GO

-- For each climber, count number of outdoor events he is attending or has attended
SELECT c.full_name, COUNT(c_oEv.climber_id) AS number_of_attended_events
FROM climber c
LEFT JOIN climber_outdoorEvent c_oEv ON c_oEv.climber_id = c.id
GROUP BY c.full_name
GO