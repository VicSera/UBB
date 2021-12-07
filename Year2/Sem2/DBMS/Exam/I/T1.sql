use PracticalExam;

create table TennisPlayer (
    PlayerID int primary key,
    Name varchar(255),
    Points int
)

delete from TennisPlayer;
insert into TennisPlayer values (1, '', 6000);


-- T1
-- set transaction isolation level read committed;
set transaction isolation level read uncommitted ;
begin tran
    update TennisPlayer
    set Points = Points + 100
    where PlayerID = 1
    go;

    ---

    rollback tran