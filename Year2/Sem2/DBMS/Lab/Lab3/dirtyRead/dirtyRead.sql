-- dirty read (first execute updateWithRollback.sql in a separate console)
set transaction isolation level read uncommitted;
-- set transaction isolation level read committed; -- solution
begin tran
print 'Running select...'
select grade from climbingRoute where id = 1
print 'Select finished.'
commit tran
go;
