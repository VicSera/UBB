use Mock
go

-- b
create or alter procedure insertDelivery @customerId int, @shopId int, @droneSerialNumber int, @dateAndTime datetime
as
begin
insert into Delivery (customerId, pizzaShopId, droneSerialNumber, dateAndTime) values
	(@customerId, @shopId, @droneSerialNumber, @dateAndTime)
end
go

--c 
create or alter view favouriteManufacturers
as
select man.name
from Manufacturer man
inner join 
(select m.id
from Manufacturer m
inner join Drone d on m.id = (select model.manufacturerId from DroneModel model where model.id = d.modelId)
group by m.id
having count(*) = 
	(select top 1 count(*) as nr
	from Manufacturer m2
	left join Drone d2 on m2.id = (select model2.manufacturerId from DroneModel model2 where model2.id = d2.modelId)
	group by m2.id
	order by nr desc)) favMan on favMan.id = man.id
go

select * from favouriteManufacturers;

insert into Manufacturer values ('M1'), ('M2'), ('M3');
insert into DroneModel values (1, 'm1', 1, 1), (2, 'm2', 2, 2), (3, 'm3', 3, 3);
insert into Drone values (1), (1), (1), (2), (2), (2), (2), (3), (3), (3), (3); 
insert into Customer values ('C1', 1), ('C2', 1), ('C3', 1); 
insert into PizzaShop values ('P1', 'a1');
insert into Delivery values (1, 1, 1, GETDATE()), (1, 1, 1, GETDATE()), (1, 1, 1, GETDATE()), (2, 1, 1, GETDATE()), (2, 1, 1, GETDATE());
go

create or alter function minDeliveries (@D int)
returns table
as
return (select c.name
from Customer c
left join Delivery d on c.id = d.customerId
group by c.name
having count(*) >= @D)

select * from minDeliveries(3);