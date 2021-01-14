use PracticalExam
go

-- a
create table Country (
	id int primary key identity(1, 1),
	name varchar(255),
	area int,
	population int
)

create table MountainRangeSystem (
	id int primary key identity(1, 1),
	name varchar(255),
	length int,

)

create table MountainRangeSystem_Country (
	countryId int foreign key references Country(id),
	mountainRangeSystemId int foreign key references MountainRangeSystem(id),
	primary key (countryId, mountainRangeSystemId)
)

create table MountainGroup (
	id int primary key identity(1, 1),
	name varchar(255),
	mountainRangeSystemId int foreign key references MountainRangeSystem(id)
)

create table Peak (
	id int primary key identity(1, 1),
	name varchar(255),
	height int,
	latitude float,
	longitute float,
	mountainGroupId int foreign key references MountainGroup(id)
)
go

-- populate the tables
insert into Country values ('Romania', 10000, 10000);
insert into MountainRangeSystem values
	('MRS1', 100),
	('MRS2', 200),
	('MRS3', 300);
insert into MountainGroup values
	('MG1_1', 1),
	('MG2_1', 1),
	('MG3_1', 1),
	('MG4_1', 1),
	('MG5_1', 1),
	('MG6_1', 1),
	('MG7_1', 1),
	('MG8_1', 1),
	('MG9_1', 1),
	('MG10_1', 1),
	('MG11_1', 1),
	('MG1_2', 2),
	('MG2_2', 2),
	('MG3_2', 2),
	('MG4_2', 2),
	('MG5_2', 2),
	('MG6_2', 2),
	('MG7_2', 2),
	('MG8_2', 2),
	('MG9_2', 2),
	('MG10_2', 2),
	('MG11_2', 2),
	('MG1_3', 3),
	('MG2_3', 3),
	('MG3_3', 3),
	('MG4_3', 3),
	('MG_delete', 3);
insert into Peak values
	('P1', 3000, 45, 45, 1),
	('P2', 3001, 45, 45, 2),
	('P3', 3002, 45, 45, 3),
	('P4', 3003, 45, 45, 4),
	('P5', 3004, 45, 45, 5),
	('P6', 3002, 45, 45, 12),
	('P7', 3003, 45, 45, 13),
	('P8', 3004, 45, 45, 14),
	('P_delete1', 1, 1, 1, 27),
	('P_delete2', 1, 1, 1, 27),
	('P_delete2', 1, 1, 1, 27);
go

-- b
create or alter procedure deleteGroupAndPeaks @mountainGroupName varchar(255)
as
begin
-- obtain the id from the name
declare @mountainGroupId int
set @mountainGroupId = (select id from MountainGroup where name = @mountainGroupName)

-- first delete corresponding peaks
delete from Peak
where mountainGroupId = @mountainGroupId

-- then delete the peak itself
delete from MountainGroup
where id = @mountainGroupId
end
go

exec deleteGroupAndPeaks 'MG_delete'
go

-- c
create or alter view mountainRangeSystemView 
as
select mrs.name
from MountainRangeSystem mrs
inner join -- first condition
	(select mg.mountainRangeSystemId
	from MountainGroup mg
	group by mg.mountainRangeSystemId
	having count(*) >= 10 -- only take groups with at least 10 mountains
	) with10Mountains on mrs.id = with10Mountains.mountainRangeSystemId 
	-- at this point, moutain range systems will surely follow the first condition
inner join
	(select mg.mountainRangeSystemId
	from MountainGroup mg
	inner join 
		(select p.id, p.mountainGroupId
		from Peak p
		where p.height > 2000 -- only take peaks taller than 2000m
		) tallerThan2000 on mg.id = tallerThan2000.mountainGroupId
	group by mg.mountainRangeSystemId
	having count(*) >= 5 -- only take groups with at least 5 such peaks
	) with5PeaksTallerThan2000 on with5PeaksTallerThan2000.mountainRangeSystemId = mrs.id
	-- at this point, mountain range systems will surely follow both conditions
go

-- only one mountainRangeSystem is selected -> MRS1, since it satisfies both conditions
-- MRS2 has enough mountain ranges, but not enough tall peaks
-- MRS3 doesn't have enough mountain ranges, and also not enough tall peaks
select * from mountainRangeSystemView
go

-- d
create or alter function mgWithPPeaksOverMMetersHigh (@P int, @M int)
returns table
as
return 
	(select mtnGr.name
	from MountainGroup mtnGr
	left join -- left join is required for the @P = 0 case, because inner join would not create a row at all, whereas left join will create a row with verified.id being NULL
		(select mg.id
		from MountainGroup mg
		inner join -- join each mountain group to its verified peaks (height > @M)
			(select p.id, p.mountainGroupId
			from Peak p
			where p.height > @M) tallerThanM on mg.id = tallerThanM.mountainGroupId
		group by mg.id -- group them by the id of the mountain group
		having count(*) >= @P -- only take groups which have the required number of peaks
		) verified on verified.id = mtnGr.id 
	where verified.id is not null or @P = 0 -- either the mountain group passed the verification, or @P is 0 so it passes automatically
	)
go

-- no results since no mountain group has that many peaks in the first place
select * from mgWithPPeaksOverMMetersHigh(3, 1000)

-- multiple results since the peaks are all tall enough, and each mountain range has to have only one peak
select * from mgWithPPeaksOverMMetersHigh(1, 2000)

-- fewer results since the height this time is higher
select * from mgWithPPeaksOverMMetersHigh(1, 3001)

-- all mountain groups have at least 0 peaks of any height, so this returns everything
select * from mgWithPPeaksOverMMetersHigh(0, 10000)