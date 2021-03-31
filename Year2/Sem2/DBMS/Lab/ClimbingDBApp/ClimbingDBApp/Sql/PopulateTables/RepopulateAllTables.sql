USE ClimbingDB

DELETE FROM friendship
DELETE FROM climber_indoorEvent
DELETE FROM climber_outdoorEvent
DELETE FROM indoorEvent
DELETE FROM outdoorEvent
DELETE FROM climber_climbingRoute
DELETE FROM climbingRoute
DELETE FROM climber
DELETE FROM gym
DELETE FROM crag
DELETE FROM city
DELETE FROM region
DELETE FROM country

EXEC populate_country
EXEC populate_region
EXEC populate_city
EXEC populate_crag
EXEC populate_gym
EXEC populate_climber
EXEC populate_climbingRoute
EXEC populate_climber_climbingRoute
EXEC populate_outdoorEvent
EXEC populate_indoorEvent
EXEC populate_climber_outdoorEvent
EXEC populate_climber_indoorEvent
EXEC populate_friendship
GO
