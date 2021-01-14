create table Manufacturer (
	id int primary key identity(1, 1),
	name varchar(255)
)

create table DroneModel (
	id int primary key identity(1, 1),
	manufacturerId int foreign key references Manufacturer(id),
	name varchar(255),
	batteryLife int,
	maximumSpeed int
)

create table Drone (
	serialNumber int primary key identity(1, 1),
	modelId int foreign key references DroneModel(id)
)

create table PizzaShop (
	id int primary key identity(1, 1),
	name varchar(255) unique,
	address varchar(255)
)

create table Customer (
	id int primary key identity(1, 1),
	name varchar(255) unique,
	loyaltyScore int
)

create table Delivery (
	id int primary key identity(1, 1),
	customerId int foreign key references Customer(id),
	pizzaShopId int foreign key references PizzaShop(id),
	droneSerialNumber int foreign key references Drone(serialNumber),
	dateAndTime datetime
)

USE [Mock]
GO
ALTER TABLE [dbo].[DroneModel] DROP CONSTRAINT [FK__DroneMode__manuf__2C3393D0]
GO
ALTER TABLE [dbo].[Drone] DROP CONSTRAINT [FK__Drone__modelId__2F10007B]
GO
ALTER TABLE [dbo].[Delivery] DROP CONSTRAINT [FK__Delivery__pizzaS__38996AB5]
GO
ALTER TABLE [dbo].[Delivery] DROP CONSTRAINT [FK__Delivery__droneS__398D8EEE]
GO
ALTER TABLE [dbo].[Delivery] DROP CONSTRAINT [FK__Delivery__custom__37A5467C]
GO
/****** Object:  Table [dbo].[R]    Script Date: 1/13/2021 12:17:46 AM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[R]') AND type in (N'U'))
DROP TABLE [dbo].[R]
GO
/****** Object:  Table [dbo].[PizzaShop]    Script Date: 1/13/2021 12:17:46 AM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[PizzaShop]') AND type in (N'U'))
DROP TABLE [dbo].[PizzaShop]
GO
/****** Object:  Table [dbo].[Manufacturer]    Script Date: 1/13/2021 12:17:46 AM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Manufacturer]') AND type in (N'U'))
DROP TABLE [dbo].[Manufacturer]
GO
/****** Object:  Table [dbo].[InsertLog]    Script Date: 1/13/2021 12:17:46 AM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[InsertLog]') AND type in (N'U'))
DROP TABLE [dbo].[InsertLog]
GO
/****** Object:  Table [dbo].[DroneModel]    Script Date: 1/13/2021 12:17:46 AM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[DroneModel]') AND type in (N'U'))
DROP TABLE [dbo].[DroneModel]
GO
/****** Object:  Table [dbo].[Drone]    Script Date: 1/13/2021 12:17:46 AM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Drone]') AND type in (N'U'))
DROP TABLE [dbo].[Drone]
GO
/****** Object:  Table [dbo].[Delivery]    Script Date: 1/13/2021 12:17:46 AM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Delivery]') AND type in (N'U'))
DROP TABLE [dbo].[Delivery]
GO
/****** Object:  Table [dbo].[Customer]    Script Date: 1/13/2021 12:17:46 AM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Customer]') AND type in (N'U'))
DROP TABLE [dbo].[Customer]
GO
