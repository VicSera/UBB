create or alter procedure insertMN
    (@climberId int, @climberFullName varchar(255), @climberGymId int,
    @routeId int, @routeName varchar(255), @cragId int, @routeGrade int) as
begin
    begin tran;

    begin try
        insert into climber(id, full_name, gym_id)
        values (@climberId, @climberFullName, @climberGymId)
        print 'added new climber'

        insert into climbingRoute(id, route_name, crag_id, grade)
        values (@routeId, @routeName, @cragId, @routeGrade);
        print 'added new route'

        insert into climber_climbingRoute(climber_id, climbingRoute_id, completion_status)
        values (@climberId, @routeId, 'Complete');
        print 'added new relation between climber and route'

        commit tran;
    end try
    begin catch
        print 'an updateConflict failed; rolling back...'
        rollback tran;
    end catch
end
go;

-- fail
exec insertMN 1000, 'Test', 1, 1000, 'Route', 1, 5;
go;

-- pass
exec insertMN 3000, 'Test', 1, 3000, 'Route', 1, 5;
go;