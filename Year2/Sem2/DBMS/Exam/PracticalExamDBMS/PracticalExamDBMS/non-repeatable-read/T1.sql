use PracticalExam;

set transaction isolation level read committed
-- set transaction isolation level repeatable read -- solution
begin tran
    select name from Student where registration_number = 2
    -- stop here, run update from T2.sql
    select name from Student where registration_number = 2
commit tran
go;

-- By setting the isolation level to repeatable read, the first select in this transaction
-- will keep its shared lock on the resource until the transaction is ended, so the second
-- transaction will have to wait before updating