begin tran
print 'Running update...'
update climbingRoute
    set grade = grade - 2
    where grade > 1
print 'Update finished.'
print 'Running select...'
select * from climbingRoute
    where grade > 1
print 'Select finished.'
go;

----------------------
rollback tran
go;