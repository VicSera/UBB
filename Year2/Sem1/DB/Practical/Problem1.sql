use PracticalExam
go

create table S (
	id1 int,
	id2 int,
	a int,
	b int,
	c int,
	d int, 
	e int,
	f int,
	primary key (id1, id2)
)

insert into S values
	(1, 2, 10, 3, 0, 1, 200, 2),
	(2, 1, 2, 4, 1, 2, 100, 4),
	(2, 2, 2, 5, 1, 2, 110, 5),
	(2, 4, 3, 6, 1, 2, 100, 7),
	(4, 1, 3, 7, 2, 1, 200, 7),
	(4, 2, 3, 8, 2, 1, 300, 7),
	(5, 1, 3, 10, 3, 2, 100, 9),
	(5, 2, 3, 11, 4, 2, 100, 2),
	(6, 1, 10, 4, 1, 1, 100, 3),
	(6, 2, 2, 6, 1, 2, 120, 6),
	(6, 3, 3, 9, 3, 2, 100, 9),
	(7, 1, 10, 2, 0, 1, 100, 1);
go

select s1.a, count(*) numrows
from S s1 inner join S s2 on s1.id1 > s2.id1
	and s1.id2 > s2. id2
group by s1.a
having min(s2.c) > 0 -- a, c


select distinct s1.id2
from S s1
where s1.b not in
	(select s2.d from S s2 where s2.id2 >= 3)
	union
	select distinct s3.id1 from S s3


create table UpdateLog(
	id1 int, id2 int, n int, datetimeop datetime
)

create or alter trigger TrOnUpdate
on S
for UPDATE
as
insert UpdateLog(id1, id2, n, datetimeop)
select i.id1, i.id2, d.d - i.d, getdate()
from inserted i inner join deleted d on i.id1 = d.id1 and i.id2 = d.id2
where d.d > i.d

update S
set D = 0
where id1 between 5 and 7

select * from UpdateLog;