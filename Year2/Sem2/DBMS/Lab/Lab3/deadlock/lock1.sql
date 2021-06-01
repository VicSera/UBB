begin tran
declare @average float
print 'Running select...'
select @average = avg(grade)
    from climbingRoute
print 'Select finished.'
print 'Running update...'
update climbingRoute
    set grade = @average
    where grade < @average;
print 'Update finished.'
go

----------------------
rollback tran
go;