USE ClimbingDB
GO

SELECT begin_date
FROM indoorEvent
INTERSECT
SELECT begin_date
FROM outdoorEvent
GO