USE ClimbingDB
GO

-- Retrieve all events (both indoor and outdoor) that happen in 2020
SELECT *
FROM indoorEvent
WHERE begin_date >= '2020-01-01' AND end_date <= '2020-12-31'
UNION
SELECT *
FROM outdoorEvent
WHERE begin_date >= '2020-01-01' AND end_date <= '2020-12-31'