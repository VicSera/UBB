--T2
use PracticalExam;
-- set transaction isolation level read uncommitted;
set transaction isolation level repeatable read ;
begin tran
    select *
    from TennisPlayer
    Where PlayerID = 1
    go;

    ---

    update TennisPlayer
    set Points = Points + 200
    Where PlayerID = 1
    commit tran
    go;