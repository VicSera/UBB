-- updateConflict that gets rolled back
begin tran
print 'Running update...'
update climbingRoute
    set grade = 5
    where id = 1
print 'Update finished'
print 'Waiting for 10 seconds...'
waitfor delay '00:00:10'
print 'Wait finished.'
print 'Rolling back...'
rollback tran
print 'Rollback finished.'
go;