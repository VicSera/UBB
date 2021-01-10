USE ClimbingDB
GO

DROP PROCEDURE _addCountryPK
GO

CREATE PROCEDURE _addCountryPK AS
BEGIN
ALTER TABLE country
ADD CONSTRAINT PK_country PRIMARY KEY (code)
ALTER TABLE region
ADD CONSTRAINT FK_region_country FOREIGN KEY (country_code) REFERENCES country(code)
END
GO

DROP PROCEDURE _dropCountryPK
GO

CREATE PROCEDURE _dropCountryPK AS
BEGIN
ALTER TABLE region
DROP CONSTRAINT FK_region_country
ALTER TABLE country
DROP CONSTRAINT PK_country
END
GO

DROP PROCEDURE addCountryPK
GO

CREATE PROCEDURE addCountryPK AS
BEGIN
EXEC _addCountryPK
EXEC newVersion '_addCountryPK', '_dropCountryPK' 
END
GO

DROP PROCEDURE dropCountryPK
GO

CREATE PROCEDURE dropCountryPK AS
BEGIN
EXEC _dropCountryPK
EXEC newVersion '_dropCountryPK', '_addCountryPK'
END
GO
