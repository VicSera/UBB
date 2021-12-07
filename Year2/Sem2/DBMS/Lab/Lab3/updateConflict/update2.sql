set transaction isolation level snapshot
begin tran
    print 'Running update...'
    update climber set full_name = 'Update2'
    where id = 5
    print 'Update finished.'
    print 'Waiting for 10 seconds...'
    waitfor delay '00:00:10'
    print 'Wait finished.'
    print 'Committing transaction.'
commit tran
    print 'Committed transaction.'