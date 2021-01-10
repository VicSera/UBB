USE ClimbingDB
GO

-- Postpone events starting in 2020 or 2021 by one year (haha... :( )
UPDATE indoorEvent
SET begin_date = DATEADD(year, 1, begin_date),
	end_date = DATEADD(year, 1, end_date)
WHERE YEAR(begin_date) BETWEEN 2020 AND 2021