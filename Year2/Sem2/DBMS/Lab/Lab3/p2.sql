create or alter procedure insertMNRecover
    (@climberId int, @climberFullName varchar(255), @climberGymId int,
    @routeId int, @routeName varchar(255), @cragId int, @routeGrade int) as
begin
    insert into climber(id, full_name, gym_id)
    values (@climberId, @climberFullName, @climberGymId)
    print 'added new climber'

    insert into climbingRoute(id, route_name, crag_id, grade)
    values (@routeId, @routeName, @cragId, @routeGrade);
    print 'added new route'

    insert into climber_climbingRoute(climber_id, climbingRoute_id, completion_status)
    values (@climberId, @routeId, 'Complete');
    print 'added relation between climber and route'
end
go;

-- fail
exec insertMNRecover 1500, 'Test', 1, 1000, 'Route', 1, 5;
go;

-- pass
exec insertMNRecover 3001, 'Test', 1, 3001, 'Route', 1, 5;
go;