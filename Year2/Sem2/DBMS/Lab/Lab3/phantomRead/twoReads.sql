-- phantom read (run this and immediately after insertClimber.sql)
set transaction isolation level read committed
-- set transaction isolation level serializable -- solution
begin tran
    print 'Running select...'
    select full_name from climber
    print 'Select finished.'
    print 'Waiting for 10 seconds...'
    waitfor delay '00:00:10'
    print 'Wait finished.'
    print 'Running select...'
    select full_name from climber
    print 'Select finished.'
    print 'Committing transaction...'
commit tran
    print 'Committed transaction...'
go;