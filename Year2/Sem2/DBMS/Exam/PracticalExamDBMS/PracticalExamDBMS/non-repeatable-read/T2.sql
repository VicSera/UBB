use PracticalExam;

begin tran
update Student
    set name = 'Updated in a clandestine manner'
    where registration_number = 2
commit tran
go;