-- non repeatable read (run this and then immediately after updateName.sql)
set transaction isolation level read committed
-- set transaction isolation level repeatable read -- solution
begin tran
    print 'Running select...'
    select full_name from climber where id = 1
    print 'Select finished.'
    print 'Waiting for 10 seconds...'
    waitfor delay '00:00:10'
    print 'Wait finished.'
    print 'Running select...'
    select full_name from climber where id = 1
    print 'Select finished.'
commit tran
go;