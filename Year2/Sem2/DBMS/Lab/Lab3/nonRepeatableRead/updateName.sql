begin tran
print 'Running update...'
update climber
    set full_name = 'Victor Updated'
    where id = 1
commit tran
print 'Update finished.'
go;