begin tran
    print 'Select finished.'
    insert into climber(id, full_name, gym_id)
    values (2000, 'Test', 1)
    print 'Select finished.'
    print 'Committing transaction.'
commit tran
print 'Committed transaction.'
go;