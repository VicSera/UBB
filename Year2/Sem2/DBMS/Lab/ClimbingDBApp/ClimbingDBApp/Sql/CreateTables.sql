CREATE DATABASE ClimbingDB
GO

USE ClimbingDB
GO

CREATE TABLE climber (
  id int PRIMARY KEY,
  full_name varchar(255) NOT NULL,
  gym_id int,
)
GO

CREATE TABLE friendship (
  climber1_id int,
  climber2_id int,
  PRIMARY KEY (climber1_id, climber2_id),
)
GO

CREATE TABLE country (
  code int PRIMARY KEY,
  country_name varchar(255) NOT NULL
)
GO

CREATE TABLE region (
  code int PRIMARY KEY,
  region_name varchar(255) NOT NULL,
  country_code int NOT NULL
)
GO

CREATE TABLE city (
  code int PRIMARY KEY,
  city_name varchar(255) NOT NULL,
  region_code int NOT NULL
)
GO

CREATE TABLE crag (
  id int PRIMARY KEY,
  crag_name varchar(255) NOT NULL,
  region_code int NOT NULL
)
GO

CREATE TABLE gym (
  id int PRIMARY KEY,
  gym_name varchar(255) NOT NULL,
  city_code int NOT NULL,
  local_address varchar(255)
)
GO

CREATE TABLE climbingRoute (
  id int PRIMARY KEY,
  route_name varchar(255) NOT NULL,
  crag_id int NOT NULL,
  grade int
)
GO

CREATE TABLE climber_climbingRoute (
  climber_id int,
  climbingRoute_id int,
  completion_status varchar(255) NOT NULL,
  proposed_grade int,
  PRIMARY KEY (climber_id, climbingRoute_id)
)
GO

CREATE TABLE indoorEvent (
  id int PRIMARY KEY,
  event_name varchar(255),
  gym_id int,
  begin_date date,
  end_date date
)
GO

CREATE TABLE outdoorEvent (
  id int PRIMARY KEY,
  event_name varchar(255),
  crag_id int,
  begin_date date,
  end_date date
)
GO

CREATE TABLE climber_indoorEvent (
  climber_id int,
  event_id int,
  PRIMARY KEY (climber_id, event_id)
)
GO

CREATE TABLE climber_outdoorEvent (
  climber_id int,
  event_id int,
  PRIMARY KEY (climber_id, event_id)
)
GO

ALTER TABLE friendship ADD FOREIGN KEY (climber1_id) REFERENCES climber (id)
GO

ALTER TABLE friendship ADD FOREIGN KEY (climber2_id) REFERENCES climber (id)
GO

ALTER TABLE friendship ADD CONSTRAINT climbers_are_different_check CHECK (climber1_id <> climber2_id)
GO

ALTER TABLE climber ADD FOREIGN KEY (gym_id) REFERENCES gym (id)
GO

ALTER TABLE region ADD FOREIGN KEY (country_code) REFERENCES country (code)
GO

ALTER TABLE city ADD FOREIGN KEY (region_code) REFERENCES region (code)
GO

ALTER TABLE crag ADD FOREIGN KEY (region_code) REFERENCES region (code)
GO

ALTER TABLE gym ADD FOREIGN KEY (city_code) REFERENCES city (code)
GO

ALTER TABLE climbingRoute ADD FOREIGN KEY (crag_id) REFERENCES crag (id)
GO

ALTER TABLE climber_climbingRoute ADD FOREIGN KEY (climber_id) REFERENCES climber (id)
GO

ALTER TABLE climber_climbingRoute ADD FOREIGN KEY (climbingRoute_id) REFERENCES climbingRoute (id)
GO

ALTER TABLE indoorEvent ADD FOREIGN KEY (gym_id) REFERENCES gym (id)
GO

ALTER TABLE outdoorEvent ADD FOREIGN KEY (crag_id) REFERENCES crag (id)
GO

ALTER TABLE climber_indoorEvent ADD FOREIGN KEY (climber_id) REFERENCES climber (id)
GO

ALTER TABLE climber_indoorEvent ADD FOREIGN KEY (event_id) REFERENCES indoorEvent (id)
GO

ALTER TABLE climber_outdoorEvent ADD FOREIGN KEY (climber_id) REFERENCES climber (id)
GO

ALTER TABLE climber_outdoorEvent ADD FOREIGN KEY (event_id) REFERENCES outdoorEvent (id)
GO

